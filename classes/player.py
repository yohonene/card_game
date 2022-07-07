from cmath import rect
import pygame
class Player():
    def __init__(self):
        self.turn = True
        self.health = 75
        self.turn_count = 1
        self.card_count = 0
    
    


PlayerObj = Player()
playerHealthText = pygame.sprite.GroupSingle()

class PlayerHealth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((300,200))
        self.rect = self.image.get_rect(midbottom = (950,750))
        self.image.fill((100,100,100))
        self.text = str(PlayerObj.health)
        self.Turns = str(PlayerObj.turn_count)
        self.card_count = str(PlayerObj.card_count)
        self.createText()
        self.createBorder()

    def createBorder(self):
        self.border = pygame.image.load("graphics/health_border.png")
        self.border.set_colorkey("black")
        self.image.blit(self.border, self.image.get_rect())

    
    def createText(self):
        font = pygame.font.SysFont(None, 40)
        cardText = font.render("Cards: "+ self.card_count, True, 'white')
        self.image.blit(cardText, (30,25))

        healthText = font.render("Health: "+ self.text, True, 'green')
        self.image.blit(healthText, (30,80))

        TurnText = font.render('Turns: ' + self.Turns, True, 'white')
        self.image.blit(TurnText, (30,135))


