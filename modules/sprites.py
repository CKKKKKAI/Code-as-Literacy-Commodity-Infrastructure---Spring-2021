import os
import pygame

class pusherSprite(pygame.sprite.Sprite):
    def __init__(self, col, row, cfg):
        pygame.sprite.Sprite.__init__(self)
        self.image_path = os.path.join(cfg.IMAGESDIR, 'player.png')
        self.image = pygame.image.load(self.image_path).convert()
        color = self.image.get_at((0, 0))
        self.image.set_colorkey(color, pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.col = col
        self.row = row
    def move(self, direction, is_test=False):
        if is_test:
            if direction == 'up':
                return self.col, self.row - 1
            elif direction == 'down':
                return self.col, self.row + 1
            elif direction == 'left':
                return self.col - 1, self.row
            elif direction == 'right':
                return self.col + 1, self.row
        else:
            if direction == 'up':
                self.row -= 1
            elif direction == 'down':
                self.row += 1
            elif direction == 'left':
                self.col -= 1
            elif direction == 'right':
                self.col += 1
    def draw(self, screen):
        self.rect.x = self.rect.width * self.col
        self.rect.y = self.rect.height * self.row
        screen.blit(self.image, self.rect)


class elementSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, col, row, cfg):
        pygame.sprite.Sprite.__init__(self)
        self.image_path = os.path.join(cfg.IMAGESDIR, sprite_name)
        self.image = pygame.image.load(self.image_path).convert()
        color = self.image.get_at((0, 0))
        self.image.set_colorkey(color, pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.sprite_type = sprite_name.split('.')[0]
        self.col = col
        self.row = row
    def draw(self, screen):
        self.rect.x = self.rect.width * self.col
        self.rect.y = self.rect.height * self.row
        screen.blit(self.image, self.rect)
    def move(self, direction, is_test=False):
        if self.sprite_type == 'box':
            if is_test:
                if direction == 'up':
                    return self.col, self.row - 1
                elif direction == 'down':
                    return self.col, self.row + 1
                elif direction == 'left':
                    return self.col - 1, self.row
                elif direction == 'right':
                    return self.col + 1, self.row
            else:
                if direction == 'up':
                    self.row -= 1
                elif direction == 'down':
                    self.row += 1
                elif direction == 'left':
                    self.col -= 1
                elif direction == 'right':
                    self.col += 1