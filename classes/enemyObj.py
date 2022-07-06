import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/enemy.png').convert()
        self.rect = self.image.get_rect(midbottom = (600,200))
        self.image.set_colorkey("white")
        self.health = 20
        healthGroup.add(HealthBar())

    def updateHealth(self, damage):
        if self.health != (self.health - damage):
            #Update enemy health
            self.health = self.health - damage
            if self.health < 0:
                #Delete enemy as it is dead
                enemyGroup.remove(self)
                #Remove health bar as well
                healthGroup.empty()
                print("Enemy Slain")
            print(self.health)
        

enemyGroup = pygame.sprite.GroupSingle()
healthGroup = pygame.sprite.GroupSingle()

class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.image = pygame.Surface((200,25))
        self.rect = self.image.get_rect(midbottom = (600,25))
        self.image.fill("green")
        self.health = 20
