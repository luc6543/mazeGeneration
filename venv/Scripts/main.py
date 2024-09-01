import pygame
import random
from pygame.locals import *
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

tile_size = 50
class World():
    def __init__(self):
        self.tile_list = []
        data = self.generate()
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    block = pygame.sprite.Sprite()
                    block.image = pygame.Surface((tile_size, tile_size))
                    block.image.fill((238,170,91))

                    block_rect = block.image.get_rect()

                    block_rect.x = col_count * tile_size
                    block_rect.y = row_count * tile_size

                    tile = (block, block_rect)
                    self.tile_list.append(tile)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0].image, tile[1])

    def generate(self):
        world_data = []
        columns = SCREEN_WIDTH / tile_size
        rows = SCREEN_HEIGHT / tile_size

        col_counter = 0
        while col_counter < columns:
            row_counter = 0
            row = []
            while row_counter < rows:
                row.append(random.randint(0,1))
                row_counter += 1
            world_data.append(row)

            col_counter += 1
        return world_data

    


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


world = World()


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

running = True
while running:

    screen.fill((251,215,150))
    world.draw()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)


    screen.blit(player.surf, player.rect)

    pygame.display.flip()
    clock.tick(60)