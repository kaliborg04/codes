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
    (0, 255, 255), # cyan
    (255, 0, 255), # magenta
    (255, 255, 0), # yellow
    (255, 255, 255), # white
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
    for i in range(len(boids)):
        boid = boids[i]
        for j in range(len(boids)):
            if j == i:
                continue
            other = boids[j]
            dist_x = boid['x'] - other['x']
            dist_y = boid['y'] - other['y']
            if abs(dist_x) < 20 and abs(dist_y) < 20:
                boid['vx'] += dist_x * 0.1
                boid['vy'] += dist_y * 0.1

        if boid['x'] < 50:
            boid['vx'] += 5
        if boid['x'] > 450:
            boid['vx'] += -5
        if boid['y'] < 50:
            boid['vy'] += 5
        if boid['y'] > 450:
            boid['vy'] += -5

        boid['x'] += boid['vx']
        boid['y'] += boid['vy']
        pygame.draw.circle(screen, boid['color'], (boid['x'], boid['y']), 5)
    pygame.display.flip()
    clock.tick(60)
