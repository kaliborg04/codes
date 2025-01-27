import pygame
import random

N = 10

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
]
boids = []
for i in range(N):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    vx = random.randint(-2, 2)
    vy = random.randint(-2, 2)
    color_idx = random.randint(0, len(colors) - 1)
    color = colors[color_idx]
    boid = {'x': x, 'y': y, 'vx': vx, 'vy': vy, 'color': color}
    boids.append(boid)

while True:
    screen.fill((0, 0, 0))
    for boid in boids:
        boid['x'] += boid['vx']
        boid['y'] += boid['vy']
        pygame.draw.circle(screen, boid['color'], (boid['x'], boid['y']), 5)
    pygame.display.flip()
    clock.tick(60)
