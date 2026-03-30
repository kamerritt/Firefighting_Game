import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Kyle Saves The Day!')

BG = pygame.image.load('/Users/kamerritt/Desktop/game/game_background.jpg')
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5

FONT = pygame.font.SysFont('comicsans', 30)

def draw(player, time_elapsed):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f'Time: {round(time_elapsed)}s', 1, 'white')
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, 'green', player)

    pygame.display.update() 

def main():
    run = True

    player = pygame.Rect(200, (HEIGHT - PLAYER_HEIGHT), PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    starttime = time.time()
    time_elapsed = 0

    while run:
        clock.tick(60)
        time_elapsed = time.time() - starttime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL

        elif keys[pygame.K_RIGHT] and player.x + PLAYER_VEL  +player.width <= WIDTH:
            player.x += PLAYER_VEL      

        draw(player, time_elapsed)

    pygame.quit


if __name__ == "__main__":
    main()