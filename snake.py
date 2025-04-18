import pygame
import random

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

snake = [
    {'xc': 24, 'yc': 25},
    {'xc': 25, 'yc': 25},
    {'xc': 26, 'yc': 25},
]
new = {'xc': random.randint(5, 45), 'yc': random.randint(30, 45)}

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

speed = 4
direction = RIGHT
dist = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            newdir = None
            if event.key == pygame.K_LEFT:
                newdir = LEFT
            elif event.key == pygame.K_RIGHT:
                newdir = RIGHT
            elif event.key == pygame.K_UP:
                newdir = UP
            elif event.key == pygame.K_DOWN:
                newdir = DOWN

            if newdir is not None:            
                newhead = snake[-1].copy()
                if newdir == LEFT:
                    newhead['xc'] -= 1
                elif newdir == RIGHT:
                    newhead['xc'] += 1
                elif newdir == UP:
                    newhead['yc'] -= 1
                elif newdir == DOWN:
                    newhead['yc'] += 1

                cell2 = snake[-2]
                if (newhead['xc'] == cell2['xc'] and
                        newhead['yc'] == cell2['yc']):
                    pass
                else:
                    direction = newdir

    t = clock.tick(60) / 1000
    dist += speed * t
    print(t, dist)
    if dist >= 1: 
        dist -= 1

        for i in range(len(snake) - 1):
            cell = snake[i]
            nxt = snake[i + 1]
            cell['xc'] = nxt['xc']
            cell['yc'] = nxt['yc']

        head = snake[-1]
        if direction == RIGHT:
            head['xc'] += 1
        elif direction == LEFT:
            head['xc'] -= 1
        elif direction == UP:
            head['yc'] -= 1
        elif direction == DOWN:
            head['yc'] += 1

        if head['xc'] > 49:
            head['xc'] = 0
        elif head['xc'] < 0:
            head['xc'] = 49
        elif head['yc'] > 49:
            head['yc'] = 0
        elif head['yc'] < 0:
            head['yc'] = 49

        for i in range(len(snake) - 1):
            cell = snake[i]
            if head['xc'] == cell['xc'] and head['yc'] == cell['yc']:
                speed = 0

        if head['xc'] == new['xc'] and head['yc'] == new['yc']:
            speed *= 1.1
            snake.insert(0, new)
            while True:
                new = {
                    'xc': random.randint(0, 49),
                    'yc': random.randint(0, 49),
                }
                new_is_good = True
                for cell in snake:
                    dist_x = abs(cell['xc'] - new['xc'])
                    dist_y = abs(cell['yc'] - new['yc'])
                    if abs(dist_x) < 5 and abs(dist_y) < 5:
                        new_is_good = False
                        break
                if new_is_good:
                    break

    screen.fill((0, 0, 0))

    x = new['xc'] * 10
    y = new['yc'] * 10
    pygame.draw.rect(screen, (75, 255, 166), pygame.Rect(x, y, 10, 10))

    for (i, cell) in enumerate(reversed(snake)):
        if i % 2 == 0:
            color = (255, 0, 0)
        else:
            color = (0, 255, 0)
        x = cell['xc'] * 10
        y = cell['yc'] * 10
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))
    pygame.display.flip()
