import pygame
import sys
import random
import math

pygame.init()

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("6packs can only be admired from afar, not touchable - 美麗的腹肌只可遠觀，不可褻玩")
clock = pygame.time.Clock()

hand_image = pygame.image.load("hand.png")
sixpack_image = pygame.image.load("6packs.png")
hand_image = pygame.transform.scale(hand_image, (150, 130))
sixpack_image = pygame.transform.scale(sixpack_image, (200, 260))

hand_rect = hand_image.get_rect()
sixpack_rect = sixpack_image.get_rect(center = (800 // 2, 600 // 2))

def main():
    global window
    running = True

    while running:
        width, height = window.get_size()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        hand_rect.center = pygame.mouse.get_pos()

        safe_distance = 300
        dx = sixpack_rect.centerx - hand_rect.centerx
        dy = sixpack_rect.centery - hand_rect.centery
        distance = math.hypot(dx, dy)

        if distance < safe_distance:
            if distance < 1:  # hand completely overlapping sixpack
                sixpack_rect.center = (
                    random.randint(100, width - 100),
                    random.randint(100, height - 100)
                )
            else:
                push_strength = (safe_distance - distance) // 2 + 10
                sixpack_rect.x += int((dx / distance) * push_strength)
                sixpack_rect.y += int((dy / distance) * push_strength)

        sixpack_rect.x = max(0, min(width - sixpack_rect.width, sixpack_rect.x))
        sixpack_rect.y = max(0, min(height - sixpack_rect.height, sixpack_rect.y))

        if sixpack_rect.left <= 0:
            sixpack_rect.x = 0
            sixpack_rect.x += 20
        elif sixpack_rect.right >= width:
            sixpack_rect.x = width - sixpack_rect.width
            sixpack_rect.x -= 20

        if sixpack_rect.top <= 0:
            sixpack_rect.y = 0
            sixpack_rect.y += 20
        elif sixpack_rect.bottom >= height:
            sixpack_rect.y = height - sixpack_rect.height
            sixpack_rect.y -= 20

        window.fill((0, 0, 0))
        window.blit(sixpack_image, sixpack_rect)
        window.blit(hand_image, hand_rect)

        pygame.display.update() # flip() is the same
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()