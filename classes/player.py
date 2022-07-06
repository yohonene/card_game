from cmath import rect
import pygame
class Player():
    def __init__(self):
        self.turn = True
        self.health = 100
        self.turn_count = 1
        self.card_count = 0


PlayerObj = Player()
playerHealthText = pygame.sprite.GroupSingle()

class PlayerHealth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((275,175))
        self.rect = self.image.get_rect(midbottom = (1050,750))
        self.image.fill((25,25,100))
        self.text = str(PlayerObj.health)
        self.Turns = str(PlayerObj.turn_count)
        self.card_count = str(PlayerObj.card_count)
        self.createText()
    
    def createText(self):
        font = pygame.font.SysFont(None, 40)
        cardText = font.render("Cards: "+ self.card_count, True, 'white')
        self.image.blit(cardText, (5,5))

        healthText = font.render("Health: "+ self.text, True, 'white')
        self.image.blit(healthText, (5,75))

        TurnText = font.render('Turns: ' + self.Turns, True, 'white')
        self.image.blit(TurnText, (5,145))


