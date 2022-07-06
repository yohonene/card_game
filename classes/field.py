import pygame
from classes.cardsObject import cards, PlayCard
from classes.enemyObj import enemyGroup, Enemy


class Playfield(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.image = pygame.Surface((600, 250))
        self.rect = self.image.get_rect(midbottom = (position))
        self.textObjectCreated = False
        #Match background, otherwise black will be left
        self.image.fill((100,100,100))
        self.setup()
        #Text surface
    
    def setup(self):
        #Draw border where card can be played
        self.border = pygame.draw.rect(self.image, 'darkgrey', self.image.get_rect(), 10, 20)


    def produceHighlight(self):
        #When card is hovering over field
        if pygame.sprite.groupcollide(fieldGroup, cards, False, False):
            if pygame.mouse.get_pressed()[0]:
                if (self.rect.collidepoint(pygame.mouse.get_pos())):
                    #draw border
                    self.highlight_border = pygame.draw.rect(self.image, 'gold', self.image.get_rect(), 5, 20)
                    card_list = cards.get_sprites_at(self.rect.center)
                    if len(card_list) > 0:
                        #Draw gold border
                        self.highlight_border = pygame.draw.rect(self.image, 'gold', self.image.get_rect(), 5, 20)
        else:
            #Reset it
            self.image = pygame.Surface((600, 250))
            self.image.fill((100,100,100))
            self.border = pygame.draw.rect(self.image, 'darkgrey', self.image.get_rect(), 10, 20)

    def collision_sprite(self, event_list):
        #Collision detection between card and field
        if pygame.sprite.groupcollide(fieldGroup, cards, False, False):
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    if (self.rect.collidepoint(pygame.mouse.get_pos())):
                        #Get card object and place it in field
                        card_list = cards.get_sprites_at(pygame.mouse.get_pos())
                        #If list isn't empty
                        if len(card_list) > 0:
                            #Assign to variable for clarity
                            dropped_card = card_list[len(card_list)-1]
                            #Makes sure you cannot click card in field
                            if not dropped_card.__getattribute__("fieldCollision"):
                                #Change Attribute to stop glowing when card is dropped
                                #Change attribute to allow card to be dropped (rather than reset position)
                                dropped_card.__setattr__("fieldCollision", True)
                                #Remove highlight around field
                                self.image = pygame.Surface((600, 250))
                                self.image.fill((100,100,100))
                                self.border = pygame.draw.rect(self.image, 'darkgrey', self.image.get_rect(), 10, 20)
                                #Make image smaller in field, hover method in card object will use updated surface
                                new_scale = [100,175]
                                dropped_card.image = pygame.transform.scale(dropped_card.image, new_scale)
                                #Set card in middle of field
                                dropped_card.rect = dropped_card.image.get_rect()
                                dropped_card.rect.center = self.rect.center
                                dropped_card.__setattr__("surfaceScaled", new_scale )
                                #Start Timer to Play Animation
                                PlayCard.cardKillTimer(dropped_card)
                                #Check if normal card or number card
                                number = getattr(dropped_card, "number")
                                cardtype = getattr(dropped_card, "type")
                                #Apply card effects to enemy    
                                self.affectEnemy(number, cardtype)
                                ##
                                text_position = list(self.position)
                                #Create text to display
                                test_display = str(number) + " " + cardtype
                                #Give text position below field
                                text_position = text_position[0]-25, text_position[1]+150
                                #If no text object exists for this field
                                if not self.textObjectCreated:
                                    #Draw number and type screen
                                    textFieldGroup.add(fieldText(test_display, tuple(text_position)))
                                    #Stop any more text objects being created
                                    self.textObjectCreated = True
                                if self.textObjectCreated:
                                    #Remove if object exists
                                    textFieldGroup.remove(fieldText(test_display, tuple(text_position)))
                                    #Set bool to false, allow text to be created
                                    self.textObjectCreated = False
    
    def affectEnemy(self, number, cardtype):
        #Update enemy object with damage
            #If enemy still exists
        if enemyGroup.sprite:
            Enemy.updateHealth(enemyGroup.sprite, number)
    def update(self, event_list):
        self.collision_sprite(event_list)
        self.produceHighlight()

fieldGroup = pygame.sprite.Group()
textFieldGroup = pygame.sprite.Group()



class fieldText(pygame.sprite.Sprite):
    def __init__(self, text, position):
        super().__init__()
        self.position = position
        self.image = pygame.Surface((400, 200))
        self.rect = self.image.get_rect(midbottom = position)
        self.image.fill((100,100,100))
        self.text = str(text)
        self.createText()


    def createText(self):
        font = pygame.font.SysFont(None, 80)
        img = font.render(self.text, True, 'white')
        self.image.blit(img, (100,100))

