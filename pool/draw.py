import pygame
import numpy as np

from . import balls


def draw():
    pygame.init()

    x_bounds = [0, 700]
    y_bounds = [0, 500]
    size = [x_bounds[1], y_bounds[1]]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Drawing test")
    done = False

    clock = pygame.time.Clock()

    # Create n balls with random positions on the screen and random velocities
    n = 10
    TestBalls = balls.Balls(
        n,
        np.random.randint(*x_bounds, size=(n, 2)).astype(np.float64),
        np.random.randint(-5, 5, size=(n, 2)).astype(np.float64),
        np.random.randint(4, 10, size=(n,)),
    )

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Move balls
        TestBalls.move(x_bounds, y_bounds)

        # Draw background and balls
        screen.fill((0, 0, 0))
        TestBalls.draw(screen)

        # Limit FPS
        clock.tick(60)

        # Update screen
        pygame.display.flip()

    pygame.quit()
