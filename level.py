import pygame
from settings import *
from player import Player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.player = Player((0, 0), [self.visible_sprites], self.obstacles_sprites)

        self.display_map()

    def display_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == 'p':
                    self.player.rect.topleft = (x, y)

    def run(self):
        self.visible_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        pygame.display.flip()
                          