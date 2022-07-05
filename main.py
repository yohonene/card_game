import pygame
import classes.cardsObject
import classes.button
import classes.field
from sys import exit



#Essential Variable Setup
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()


#Game States 
debug = False #Allows testing of Card Objects
level = True #Actual Game

#Intialise Card Class, Button Class, and Field Class
c = classes.cardsObject
b = classes.button
f = classes.field

#Initial Game State Object Paramaters
def debugLevel():
    #Create Button Object
        #Button Positions on Area
    buttonPositionList = [(100,100),(100,300),(100,500)]
    b.buttonGroup.add(classes.button.Buttons('orange', 100, 75, buttonPositionList[0], 'Normal' ))
    b.buttonGroup.add(classes.button.Buttons('green', 100, 75, buttonPositionList[1], 'Number' ))
    b.buttonGroup.add(classes.button.Buttons('blue', 100, 75, buttonPositionList[2], 'Letter' ))
    #Field Object
    f.fieldGroup.add(classes.field.Playfield((500,425)))
def levelCreate():
    buttonPositionList = [(100,100)]
    b.buttonGroup.add(classes.button.DealButton('orange', 100, 75, buttonPositionList[0], 'Number' ))
    f.fieldGroup.add(classes.field.Playfield((400,225)))

#Populate Background
bg = pygame.Surface(screen.get_size()).convert()
bg.fill((100,100,100))

#Create objects for each level
if debug:
    debugLevel()
elif level:
    levelCreate()

#Event Loop
while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    #Debug Mode
    if debug:
        #Update and draw objects
        screen.blit(bg, (0,0))
        f.textFieldGroup.draw(screen)
        f.fieldGroup.draw(screen)
        f.fieldGroup.update(event_list)
        c.cards.draw(screen)
        c.cards.update()
        b.buttonGroup.draw(screen)
        b.buttonGroup.update(event_list)
    #Actual Gameplay
    elif level:
        screen.blit(bg, (0,0)) 
        f.textFieldGroup.draw(screen)
        f.fieldGroup.draw(screen)
        f.fieldGroup.update(event_list)
        c.cardPositionsGroup.draw(screen)
        c.cardPositionsGroup.update()
        b.buttonGroup.draw(screen)
        b.buttonGroup.update(event_list)
        c.cards.draw(screen)
        c.cards.update(event_list)

    
    pygame.display.update()
    clock.tick(60)