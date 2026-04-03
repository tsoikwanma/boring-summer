import pygame
import random
import sys

# Window settings
WIDTH, HEIGHT = 640, 480

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("rainy night - 去夜蒲先嚟落雨（連個天都唔鍾意我")

class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.speed = random.randint(4, 10)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-20, -1)
            self.x = random.randint(0, WIDTH)

    def draw(self, screen):
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y + 5))


def draw_thunder(screen):
    # Random chance for thunder
    if random.randint(0, 100) < 2:  # 2% chance per frame
        start_x = random.randint(50, WIDTH - 50)
        start_y = 20
        z_points = [
            (start_x, start_y),
            (start_x + 10, start_y + 40),
            (start_x - 10, start_y + 80),
            (start_x + 10, start_y + 200),
        ]
        pygame.draw.lines(screen, YELLOW, False, z_points, 1)  # thinner line


def main():
    pygame.mixer.music.load("rain.mp3")
    pygame.mixer.music.play(-1)  # Loop forever

    clock = pygame.time.Clock()

    # Create raindrops
    raindrops = [Raindrop() for _ in range(200)]

    global screen
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                global WIDTH, HEIGHT
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        screen.fill(BLACK)

        # Update and draw raindrops
        for drop in raindrops:
            drop.fall()
            drop.draw(screen)

        # Maybe draw thunder
        draw_thunder(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()