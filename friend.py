import pygame
import random
import math
from settings import *

class Friend(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites,image_path):
        super().__init__(groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.copy()

        self.direction = pygame.math.Vector2()
        self.speed = 2
        self.timer = 0
        self.move_interval = random.randint(100, 200)
        self.direction = pygame.math.Vector2(random.choice([-1, 1]), random.choice([-1, 1]))

        self.obstacle_sprites = obstacle_sprites

        self.interaction_options = {
            1: "Pobaw się piłką",
            2: "Obszczekaj",
            3: "Zaproponuj wspólny spacer",
            4: "Daj przysmak"
        }

        self.friendship_level = 0

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

    def check_proximity(self,player):
        distance = math.dist(self.rect.center, player.rect.center)
        if distance < 50:
            return True
        return False

    def interact(self,screen):
        font = pygame.font.Font(None, 24)
        options_surface = pygame.Surface((200, len(self.interaction_options) * 30))
        options_surface.fill((255, 255, 255))
        options_surface.set_alpha(200)
        options_rect = options_surface.get_rect()
        options_rect.topleft = self.rect.x, self.rect.y - options_rect.height

        for index, (option_num, option_text) in enumerate(self.interaction_options.items()):
            option_render = font.render(option_text, True, (0, 0, 0))
            option_rect = option_render.get_rect(topleft=(10, index * 30))
            options_surface.blit(option_render, option_rect)

        screen.blit(options_surface, options_rect)

    def update(self):
        self.timer += 1
        if self.timer >= self.move_interval:
            self.timer = 0
            self.move_interval = random.randint(50, 200)
            self.direction = pygame.math.Vector2(random.choice([-1, 1]), random.choice([-1, 1]))

        self.move(self.speed)
