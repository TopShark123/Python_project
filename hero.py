import pygame
import os

from pygame.sprite import _Group

class PLayer(pygame.sprite.Sprite)

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('images','player movement down','down_0.png'))
        self.rect_up = self.image.get_rect(topleft = pos)
        self.PLAYER_MOVEMENT_SPEED = 5

        self.direction = pygame.math.Vector2()


        def input(self):
            keys_pressed = pygame.key.get_pressed()
            
            if keys_pressed[pygame.K_UP]:
                self.direction.y = -1
            elif keys_pressed[pygame.K_DOWN]:
                self.direction.y = 1
            else:
                self.direction = 0
                
            
            if keys_pressed[pygame.K_LEFT]:
                self.direction.x = 1
            elif keys_pressed[pygame.K_RIGHT]:
                self.direction.x = -1
            else:
                self.direction.x = 0
                
        def player_movement():
            pass
        def update(self):
            self.input()