import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.image = pygame.Surface((150,150))
        self.rect = self.image.get_rect(midbottom = (600,200))
        self.image.fill("green")
        self.health = 20
        healthGroup.add(HealthBar())


enemyGroup = pygame.sprite.GroupSingle()
healthGroup = pygame.sprite.GroupSingle()

class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.image = pygame.Surface((200,25))
        self.rect = self.image.get_rect(midbottom = (600,25))
        self.image.fill("green")
        self.health = 20
