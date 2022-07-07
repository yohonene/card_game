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
win = True #If player wins
level = False #Actual Game

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
    # buttonPositionList = [(100,100),(100,200),(100,300)]
    # b.buttonGroup.add(classes.button.DealButton('orange', 100, 75, buttonPositionList[0], 'Sword' ))
    # b.buttonGroup.add(classes.button.DealButton('green', 100, 75, buttonPositionList[1], 'Magic' ))
    f.fieldGroup.add(classes.field.Playfield((600,500)))
    e.enemyGroup.add(classes.enemyObj.Enemy())
    p.playerHealthText.add(classes.player.PlayerHealth())

#bg music
bg_music = pygame.mixer.Sound('sound/roguelegacy2_suntower2.mp3')
bg_music.play(-1)
bg_music.set_volume(0.25)
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
        if win:
            if event.type == pygame.MOUSEBUTTONDOWN:
                levelCreate()
                bg.fill((100,100,100))
                level = True
                win = False

    #Actual Gameplay
    if win:
        f.fieldGroup.empty()
        e.enemyGroup.empty()
        p.playerHealthText.empty()
        f.textFieldGroup.empty()
        c.cards.empty()
        bg.fill((25,25,100))
        screen.blit(bg, (0,0)) 
        font = pygame.font.SysFont(None, 150)
        Text = font.render("Click to Play", True, 'white')
        Text2 = font.render("+ = Draw", True, 'Grey')
        Text3 = font.render("Swords / Eye = Attack", True, 'green')
        font = pygame.font.SysFont(None, 70)
        Text4 = font.render("If you play a card less than 4, you may play it again", True, 'red')
        screen.blit(Text, (55,50))
        screen.blit(Text2, (300,300))
        screen.blit(Text3, (55,500))
        screen.blit(Text4, (0,700))

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