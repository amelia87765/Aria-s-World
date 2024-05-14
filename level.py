import pygame
from settings import *
from player import Player

class Level:
    def __init__(self):
        self.camera_x = 0
        self.camera_y = 0
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.player = Player((0, 0), [self.visible_sprites], self.obstacles_sprites)

        self.display_group = DisplayGroup()
        self.display_map()

    def update_camera(self, player_rect):
        self.camera_x = player_rect.centerx - (WIDTH // 2)
        self.camera_y = player_rect.centery - (HEIGHT // 2)

    def display_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == 'p':
                    self.player.rect.topleft = (x, y)

    def run(self):
       self.visible_sprites.update()
       self.display_group.draw(self.display_surface)
       self.visible_sprites.draw(self.display_surface)
       pygame.display.flip()

class DisplayGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('graphics/map/map.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
    def draw(self, surface):

        surface.blit(self.floor_surf, self.floor_rect)

        super().draw(surface)                              