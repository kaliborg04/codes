import pygame
import random

N = 10

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

boids = []
for i in range(N):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    vx = random.randint(-2, 2)
    vy = random.randint(-2, 2)
    boid = {'x': x, 'y': y, 'vx': vx, 'vy': vy}
    boids.append(boid)

while True:
    screen.fill((0, 0, 0))
    for boid in boids:
        pygame.draw.circle(screen, (255, 0, 0), (boid['x'], boid['y']), 5)
    pygame.display.flip()
    clock.tick(60)
