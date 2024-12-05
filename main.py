import ducks
import pygame
import random

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

game_surface = pygame.display.set_mode((1440, 848))
pygame.display.set_caption("Duck Escape!")

font = pygame.font.SysFont('Arial', 40)

duck = ducks.GoldenDuck(
    position=(100, 100)
)

points = 0

direction = (random.choice([5, -5]), random.choice([5, -5]))

spawned_ducks = []

running = True
while running:
    game_surface.fill("white")
    game_surface.blit(font.render(f"Points: {points}", True, (20, 20, 20)), (20, 20))

    if random.randint(1, 50) == 16:
        if random.randint(10, 20) == 16:
            spawned_ducks.append(ducks.GoldenDuck(
                position=(random.randint(0, 1440), random.randint(0, 848))
            ))
        else:
            spawned_ducks.append(ducks.Duck(
                position=(random.randint(0, 1440), random.randint(0, 848))
            ))

    for duck in spawned_ducks:
        if not duck.is_caught():
            screen_width, screen_height = pygame.display.get_surface().get_size()
            x, y = duck.get_pos()
            duck_width, duck_height = duck.get_dimensions()

            direction_x, direction_y = direction

            if x + duck_width >= screen_width or x <= 0:
                direction_x *= -1

            if y + duck_height >= screen_height or y <= 0:
                direction_y *= -1

            direction = (direction_x, direction_y)

            duck.move(direction[0], direction[1])
            duck.draw(game_surface)

    pygame.display.flip()
    fpsClock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for duck in spawned_ducks:
                if not duck.is_caught() and duck.clicked(pygame.mouse.get_pos()):
                    if not duck.type:
                        points += 2
                    elif duck.type == "golden":
                        points += 10
                    duck.hide()
