import pygame
import classes.cardsObject
import classes.button
import classes.field
import classes.enemyObj
from sys import exit



#Essential Variable Setup
pygame.init()
screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()


#Game States 
debug = False #Allows testing of Card Objects
level = True #Actual Game

#Intialise Card Class, Button Class, and Field Class
c = classes.cardsObject
b = classes.button
f = classes.field
e = classes.enemyObj

#Initial Game State Object Paramaters

def levelCreate():
    buttonPositionList = [(100,100),(100,200),(100,300)]
    b.buttonGroup.add(classes.button.DealButton('orange', 100, 75, buttonPositionList[0], 'Sword' ))
    b.buttonGroup.add(classes.button.DealButton('green', 100, 75, buttonPositionList[1], 'Magic' ))
    f.fieldGroup.add(classes.field.Playfield((600,500)))
    e.enemyGroup.add(classes.enemyObj.Enemy())

#Populate Background
bg = pygame.Surface(screen.get_size()).convert()
bg.fill((100,100,100))

#Create objects for each level
if level:
    levelCreate()

#Event Loop
while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    #Actual Gameplay
    if level:
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
        e.enemyGroup.draw(screen)
        e.healthGroup.draw(screen)
        e.enemyGroup.update(event_list)

    
    pygame.display.update()
    clock.tick(60)