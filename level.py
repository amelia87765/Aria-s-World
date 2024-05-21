import pygame
from settings import *
from player import Player
from friend import Friend

class Level:
    def __init__(self):
        self.camera_x = 0
        self.camera_y = 0
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = DisplayGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.player = Player((0, 0), [self.visible_sprites], self.obstacles_sprites)
        self.friends = pygame.sprite.Group()

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
                elif column == 'f1':
                    friend = Friend((x, y), [self.visible_sprites, self.friends], self.obstacles_sprites, 'graphics/characters/Fox.png')
                    self.friends.add(friend)
                elif column == 'f2':
                    friend = Friend((x, y), [self.visible_sprites, self.friends], self.obstacles_sprites, 'graphics/characters/Julek.png')
                    self.friends.add(friend)

    def run(self):
        self.visible_sprites.update()
        self.visible_sprites.custom_draw(self.player)
        pygame.display.flip()
    def handle_interaction(self, player):
        for friend in self.friends:
            if friend.check_proximity(player):
                friend.interact(self.display_surface)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            friend.handle_option_1()
                        elif event.key == pygame.K_2:
                            friend.handle_option_2()
                        elif event.key == pygame.K_3:
                            friend.handle_option_1() 
                        elif event.key == pygame.K_4:
                            friend.handle_option_1()  
    def handle_option_1(self, friend):
        friend.friendship_level += 1

    def handle_option_2(self, friend):
        friend.friendship_level -= 1
class DisplayGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('graphics/map/map.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
    def custom_draw(self,player):

        self.offset.x = min(max(player.rect.centerx - self.half_width, 0), self.floor_rect.width - WIDTH)
        self.offset.y = min(max(player.rect.centery - self.half_height, 0), self.floor_rect.height - HEIGHT)

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)                             