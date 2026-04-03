import pygame
import sys
from collections import deque

pygame.init()

WINDOW_WIDTH = 282
WINDOW_HEIGHT = 578

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("endless force quit apps - del極都仲有")

bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

def main():
    # Load apps and resize
    app_images = []
    for fname in ["app1.png", "app2.png", "app3.png"]:
        img = pygame.image.load(fname).convert_alpha()
        img = pygame.transform.scale(img, (180, 360))  # resize apps smaller
        app_images.append(img)

    # Queue of apps (left-to-right order)
    app_queue = deque(app_images)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    # Remove the rightmost (middle) app and put it back to the end
                    removed = app_queue.pop()
                    app_queue.appendleft(removed)

        # Draw background
        screen.blit(bg, (0, 0))

        # Draw apps from left → right, overlapping
        x_offset = 0
        overlap = 30  # how much each app overlaps the previous one
        for i, app in enumerate(app_queue):
            if i >= 3:
                break
            rect = app.get_rect(midleft=(x_offset, WINDOW_HEIGHT // 2))
            screen.blit(app, rect)
            x_offset += overlap  # move next app slightly right

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()