from random import randint, choice
import pygame

#Parent Card Class
class Card(pygame.sprite.Sprite):
    def __init__(self,position=0, number=0, icontype=""):
        super().__init__()
        self.image = pygame.Surface((150, 250))
        self.image.fill('grey')
        #Surface Scaling Var
        self.surfaceScaled = [150, 250]
        #Random Spawn for Testing Purposes
        self.position = position
        self.type = icontype
        self.fieldCollision = False

        #Assign position if supplied
        if position != 0:
            self.rect = self.image.get_rect(midbottom = self.position)
        else:
            self.rect = self.image.get_rect(midbottom = (randint(50,750),randint(50,550)))
        self.number = number
        #Extra Optional Details
        #Colours to iterate through for variety in aesthetics
        card_colours = ["red", "green", "teal", "beige", "gold"]
        self.colour = choice(card_colours)
        self.createCardDetails()

    def createCardDetails(self):
        #Draws Art On Card
        self.cardart = pygame.draw.circle(self.image, self.colour, (100,50), 50, 20)
        self.cardart2 = pygame.draw.circle(self.image, self.colour, (50,150), 75, 25)

    def checkIfTopCard(self):
        card_list = cards.get_sprites_at(pygame.mouse.get_pos())
        if self == card_list[len(card_list)-1]:
            return True

    def update(self):
        pass



#Class Inherit from Card, Store Number or String Values 
class PlayCard(Card):
    def __init__(self, number,position=0, icontype=""):
        #Send values back to Parent(Card)
        super().__init__(position, number, icontype="")
        self.number = number
        self.position = position
        self.acceleration = 1
        self.moved = False
        #Icon Type
        self.type = icontype


    def updateSurface(self, coord):
        #Update surface to be scaled
        self.surfaceScaled = coord
        
    def createCardDetails(self):
        #Default size before going into field
        normal_size = 150
        #Load Image
        self.border = pygame.image.load("graphics/border.png")
        #Remove black from image
        self.border.set_colorkey("black")
        #Icon
        if self.type == "Sword":
            self.icon = pygame.image.load('graphics/sword_icon.png')
        elif self.type == "Magic":
            self.icon = pygame.image.load('graphics/magic_icon.png')
        else:
            self.icon = pygame.image.load("graphics/border.png")
        self.icon.set_colorkey('white')

        #Number gen + Scaling
        if normal_size == self.image.get_width():
            font = pygame.font.SysFont(None, 120)
            img = font.render((f"{self.number}"), True, self.colour)
            #Old border
            #self.border = pygame.draw.rect(self.image, 'blue', self.image.get_rect(), 10)
            self.image.blit(img, self.image.get_rect().center)
            self.image.blit(self.border, self.image.get_rect())
            self.image.blit(self.icon, self.image.get_rect().topleft)
        else:
            #Font smaller to scale it down, doesn't look janky
            font = pygame.font.SysFont(None, 80)
            img = font.render((f"{self.number}"), True, self.colour)
            #Scale it depending on surfaceScaled (not in field or not)
            self.border = pygame.transform.scale(self.border, (self.surfaceScaled[0], self.surfaceScaled[1]) )
            self.image.blit(self.border, self.image.get_rect())
            self.image.blit(img, self.image.get_rect().center)
            
    def move_card_animated(self):
        #Update per tick, + 1 to y
        self.acceleration += 1
        self.rect.y += self.acceleration
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            #After stopping...
            self.moved = True
            #Record location

    def cardKillTimer(self):
        self.card_death_animation = pygame.USEREVENT + 1
        self.start_time = pygame.time.get_ticks()
        pygame.time.set_timer(self.card_death_animation,35,60)
        

        

    def playKillAnimation(self,event_list):
        #DEATH ANIMATION - Spins and scales smaller, cool weird effect
        for event in event_list:
            if event.type == self.card_death_animation:
                seconds=(pygame.time.get_ticks()-self.start_time)/1000
                #Loops 60 seconds - Deleted after 2 seconds or more (ClusterFUCK)
                if seconds < 0.5:
                    pass
                if seconds < 0.6 and seconds > 0.5:
                    self.poof = pygame.image.load('graphics/poof.png').convert()
                    self.poof.set_colorkey("black")
                    self.image = pygame.transform.scale(self.poof, (self.surfaceScaled[0] , self.surfaceScaled[1]))
                if seconds > 0.5 and seconds < 0.8:
                    self.poof = pygame.image.load('graphics/poof_2.png').convert()
                    self.poof.set_colorkey("black")
                    self.image = pygame.transform.scale(self.poof, (self.surfaceScaled[0] , self.surfaceScaled[1]))
                if seconds > 0.9 and seconds < 1.1:
                    self.poof = pygame.image.load('graphics/poof_3.png').convert()
                    self.poof.set_colorkey("black")
                    self.poof = pygame.transform.scale(self.poof, (self.surfaceScaled[0], self.surfaceScaled[1]) )
                if seconds > 1.1 and seconds < 1.3:
                    self.poof = pygame.image.load('graphics/poof_end.png').convert()
                    self.poof.set_colorkey("black")
                    self.image = pygame.transform.scale(self.poof, (self.surfaceScaled[0], self.surfaceScaled[1]) )                
                elif seconds >= 1.3:
                    cards.remove(self)    
   
    def expandUponHover(self):
        #When user hovers over card - enlarge and highlight
        multiplier = 1.05
        if not pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            #Only highlight the top card when hovering over multiple cards
            if self.checkIfTopCard():
                #If not in field, scale image for increased visibility
                if not self.fieldCollision:
                    self.image = pygame.transform.smoothscale(self.image, (self.surfaceScaled[0]*multiplier , self.surfaceScaled[1]*multiplier))
                    self.highlight_border = pygame.draw.rect(self.image, 'gold', self.image.get_rect(), 5, 5)
        #If not in Field
        elif not self.fieldCollision:
            self.image = pygame.Surface((self.surfaceScaled[0], self.surfaceScaled[1]))
            self.image.fill('grey')
            self.createCardDetails()

    def followMouse(self, event_list):
        #Set rectangle position to mouse cursor - if not already holding a card
        #If the card is not in a field, allow it to be clicked
        if not self.fieldCollision:
            if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()): 
                card_list = cards.get_sprites_at(pygame.mouse.get_pos())
                #The last card object (highest layer) is selected
                card_list[len(card_list)-1].rect.center = pygame.mouse.get_pos()
                #Move selected card to front of layeredupdate group
                cards.move_to_front(card_list[len(card_list)-1])

            for event in event_list:
                #If holding the card and mouse is released, put card back in it spawn position
                if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
                    card_list = cards.get_sprites_at(pygame.mouse.get_pos())
                    #If not colliding with field (to play card)
                    if not self.fieldCollision:
                        card_list[len(card_list)-1].rect.midbottom = self.position
                        #To allow animation of falling
                        self.moved = False

    def update(self, event_list):
        #If card has supplied coordinates and hasn't moved before, allow acceleration
        if self.position != 0 and self.moved == False:
            self.move_card_animated()
        self.followMouse(event_list)
        self.expandUponHover()
        if self.fieldCollision:
            self.playKillAnimation(event_list)
    


#Card Position Group
cardPositionsGroup = pygame.sprite.Group()

class CardPositions():
    def __init__(self):
        #0 indicates spot open, 1 means closed
        self.spots = [0,0,0,0,0]
        self.positions = [(50,500),(175,500),(300,500), 
        (425,500),(550,500)]
        self.maxPositionNumber = len(self.positions)
        index = 0
        for x in self.positions:
            cardPositionsGroup.add(CardPositions.CardHolder(x, index))
            #Supply object with index position that relates to self.positions
            index += 1


    def avaliableSpot(self):
        for x in range(self.maxPositionNumber):
            #If position 1 is avaliable
            
            if self.positions[self.maxPositionNumber-1] == 1:
                raise Exception('Exceeded maximum amount of card positions')
            elif not self.spots[x]:
                #Set it unavaiable
                #self.spots[x] = 1
                #Return position
                return self.positions[x]
    #Invididual Card Spots Created by CardPositions Class
    class CardHolder(pygame.sprite.Sprite):
        def __init__(self, pos, index):
            pygame.sprite.Sprite.__init__(self)
            #Position given by CardPositions
            self.image = pygame.Surface((50, 50))
            self.image.fill((100,100,100))
            self.rect = self.image.get_rect(midbottom = (pos))
            self.border = pygame.draw.rect(self.image, 'silver', self.image.get_rect(), 10)
            self.index = index
            self.holding_card = False

        
        #Check if card has left, if so - update CardPositioons self.spot with 0
        def checkIfCardLeft(self):
            card_list = cards.get_sprites_at(self.rect.center)
            if len(card_list) > 0:
                if self.rect.colliderect(card_list[0].rect):
                    #Set spots to 1 to indicated that card is in position
                    spot_list = cardPositionObject.__getattribute__("spots")    
                    spot_list[self.index] = 1
                    cardPositionObject.__setattr__("spots",spot_list)
                    self.holding_card = True
            elif self.holding_card and not len(card_list) > 0:
                self.holding_card = False
                #Get array so we can edit an individual index
                spot_list = cardPositionObject.__getattribute__("spots")
                #Set back to 0 so new cards can be spawned in
                spot_list[self.index] = 0
                cardPositionObject.__setattr__("spots",spot_list)


        def update(self):
            self.checkIfCardLeft()


#Card Group Holder
cards = pygame.sprite.LayeredUpdates()
#Card position object
cardPositionObject = CardPositions()




