import pygame

pygame.init()

surface = pygame.display.set_mode((1334, 750))
pygame.display.set_caption('game')

clock = pygame.time.Clock()


def main_loop():
    shut_down = False

    while not shut_down:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shut_down = True

        pygame.display.update()

        clock.tick(60)

main_loop()
pygame.quit()
quit()