import pygame
import numpy as np
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
pygame.display.set_caption("old broken tv - 你個電視壞咗啊")
clock = pygame.time.Clock()

def generation(width, height):
    noise = np.random.randint(0, 256, (height, width), dtype = np.uint8)
    rgb_noise = np.stack([noise] * 3, axis = -1)
    rgb_noise = np.transpose(rgb_noise, (1, 0, 2))
    surface = pygame.surfarray.make_surface(rgb_noise)
    return surface

def main():
    global screen
    running = True

    while running:
        width, height = screen.get_size()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        screen.blit(generation(width, height), (0, 0))
        pygame.display.flip()
        clock.tick(15)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()