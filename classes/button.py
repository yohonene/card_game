from random import randint
from secrets import choice
import pygame
import classes.cardsObject

class Buttons(pygame.sprite.Sprite):
    #Size must be a tuple
    def __init__(self,colour,x,y, position, text="No Text"):
        super().__init__()
        #Attributes
        self.x = x
        self.y = y
        self.colour = colour
        self.position = position
        self.image = pygame.Surface((self.x,self.y))
        self.image.fill(self.colour)
        self.rect = self.image.get_rect(midbottom = self.position)
        #Optional Text for Button
        self.text = text
        self.createText()
    def buttonPressed(self, event_list):
        #If button is hovered over and pressed - do action
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (self.rect.collidepoint(pygame.mouse.get_pos())):
                    #Spawns card with Number, Letter or Nothing
                    if self.text == "Number":
                        classes.cardsObject.cards.add(classes.cardsObject.Number(randint(1,10)))
                    elif self.text == "Letter":
                        letter_list = ['A', 'B', 'C']
                        classes.cardsObject.cards.add(classes.cardsObject.Number(choice(letter_list)))
                    else:
                        classes.cardsObject.cards.add(classes.cardsObject.Card())
                    #Highlight Button when Clicked
                    self.highlight = pygame.draw.rect(self.image, 'black', self.image.get_rect())
            if event.type == pygame.MOUSEBUTTONUP:
                #When user lets go of mouse, return button looks to normal
                self.image = pygame.Surface((self.x,self.y))
                self.image.fill(self.colour)
                self.createText()

    def createText(self):
        if self.text != "No Text":
            font = pygame.font.SysFont(None, 35)
            img = font.render(self.text, True, 'teal')
            self.image.blit(img, (5,25))

    def update(self, event_list):
        self.buttonPressed(event_list)
        
class DealButton(Buttons):
    def __init__(self,colour,x,y, position, text="No Text"):
        #Important to keep positionals in this init below
        super().__init__(colour, x, y, position)
        self.text = text
        self.createText()

    def buttonPressed(self, event_list):
        #If button is hovered over and pressed - do action
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (self.rect.collidepoint(pygame.mouse.get_pos())):
                    #Spawns card with Number, Letter or Nothing
                    #Calls card avaliableSpot() method
                    #Has a limit of cards that can be called
                    try:
                        pos = classes.cardsObject.CardPositions.avaliableSpot(classes.cardsObject.cardPositionObject)
                        if pos == None:
                            print("Limit of cards reached")
                            #Print in terminal, then stop pos from going forward and breaking object call
                            break
                    except:
                        print("Limit of cards reached")
                    else:
                        if self.text == "Number":
                            classes.cardsObject.cards.add(classes.cardsObject.Number(randint(1,10), (pos)))
                        elif self.text == "Letter":
                            letter_list = ['A', 'B', 'C']
                            ##Planned - call cardsObject.postionm whatever to return an avaliable position
                            classes.cardsObject.cards.add(classes.cardsObject.Number(choice(letter_list), (pos)))
                        else:
                            classes.cardsObject.cards.add(classes.cardsObject.Card((pos)))
                        #Highlight Button when Clicked
                        self.highlight = pygame.draw.rect(self.image, 'black', self.image.get_rect())
            if event.type == pygame.MOUSEBUTTONUP:
                #When user lets go of mouse, return button looks to normal
                self.image = pygame.Surface((self.x,self.y))
                self.image.fill(self.colour)
                self.createText()

#Debug
buttonGroup = pygame.sprite.Group()
#Level
levelbuttonGroup = pygame.sprite.Group()