import pygame 
from settings import *

class Friend(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.copy()

        self.direction = pygame.math.Vector2()
        self.speed = 3

        self.obstacle_sprites = obstacle_sprites
		
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
		

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: 
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: 
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: 
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: 
                        self.rect.top = sprite.rect.bottom

    def import_graphics(self,name):
        main_path = f'graphics/characters/{name}/'

    def update(self):
        self.move(self.speed)