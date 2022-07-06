from random import randint
import pygame
from classes.player import PlayerObj, playerHealthText, PlayerHealth

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/enemy.png').convert()
        self.rect = self.image.get_rect(midbottom = (600,200))
        self.image.set_colorkey("white")
        self.health = 20
        self.hpbar = HealthBar(self.health)
        self.turn = False
        healthGroup.add(self.hpbar)

    def updateHealth(self, damage):
        if self.health != (self.health - damage):
            #Update enemy health
            self.health = self.health - damage
            #Update HP bar
            self.hpbar.updateBar(damage)
            if self.health <= 0:
                #Delete enemy as it is dead
                enemyGroup.remove(self)
                #Remove health bar as well
                healthGroup.empty()
                print("Enemy Slain")

    def setTimer(self):
        self.attack_animation = pygame.USEREVENT + 2
        #500 millisecond animation
        pygame.time.set_timer(self.attack_animation,1000,1)

    def enemyTurn(self, event_list):
        for event in event_list:
            if event.type == self.attack_animation:
                #Do animation
                #Damage player
                PlayerObj.health -= randint(5,10)
                #Increase turn count
                PlayerObj.turn_count += 1
                #Update player text (groupsingle automatically
                # deletes last text)
                playerHealthText.add(PlayerHealth())
                #Make it players turn
                PlayerObj.turn = True
                self.turn = False

    def update(self, event_list):
        if self.turn:
            self.enemyTurn(event_list)


    
enemyGroup = pygame.sprite.GroupSingle()
healthGroup = pygame.sprite.GroupSingle()

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, hp):
        super().__init__()
        self.image = pygame.Surface((200,25))
        self.rect = self.image.get_rect(midbottom = (600,25))
        self.image.fill("green")
        #Hp from Enemy
        self.health = hp
        self.total_damage = 0
    def updateBar(self, damage):
        self.total_damage += damage
        #Scales visual damage to surface size of bar with health provided
        hp_bar_scalar = 200/self.health
        #Update new surface, increase size by damage
        self.dmgBar = pygame.Surface((self.total_damage*hp_bar_scalar,25))
        self.dmgBar.fill('red')
        #Move red bar to the left, as more damage is taken
        self.image.blit(self.dmgBar, (self.image.get_rect()))

