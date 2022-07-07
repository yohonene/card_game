import pygame
import classes.cardsObject
import classes.button
import classes.field
import classes.enemyObj
import classes.player
from sys import exit



#Essential Variable Setup
pygame.init()
screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()


#Game States 
win = False #If player wins
level = True #Actual Game

#Intialise Card Class, Button Class, and Field Class
c = classes.cardsObject
b = classes.button
f = classes.field
e = classes.enemyObj
p = classes.player

#Check if enemy dead

def gameState():
    if classes.enemyObj.enemyGroup.sprite:
        return False
    else:
        return True


#Initial Game State Object Paramaters

def levelCreate():
    buttonPositionList = [(100,100),(100,200),(100,300)]
    b.buttonGroup.add(classes.button.DealButton('orange', 100, 75, buttonPositionList[0], 'Sword' ))
    b.buttonGroup.add(classes.button.DealButton('green', 100, 75, buttonPositionList[1], 'Magic' ))
    f.fieldGroup.add(classes.field.Playfield((600,500)))
    e.enemyGroup.add(classes.enemyObj.Enemy())
    p.playerHealthText.add(classes.player.PlayerHealth())

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
    if win:
        bg.fill((25,25,100))
        screen.blit(bg, (0,0)) 
        font = pygame.font.SysFont(None, 150)
        Text = font.render("You win!", True, 'white')
        screen.blit(Text, (55,50))

    elif level:
        screen.blit(bg, (0,0)) 
        f.textFieldGroup.draw(screen)
        f.fieldGroup.draw(screen)
        f.fieldGroup.update(event_list)
        c.cardPositionsGroup.draw(screen)
        c.cardPositionsGroup.update()
        c.cardPositionObject.update()
        b.buttonGroup.draw(screen)
        b.buttonGroup.update(event_list)
        c.cards.draw(screen)
        c.cards.update(event_list)
        e.enemyGroup.draw(screen)
        e.healthGroup.draw(screen)
        e.enemyGroup.update(event_list)
        p.playerHealthText.draw(screen)

        win = gameState()

    
    pygame.display.update()
    clock.tick(60)