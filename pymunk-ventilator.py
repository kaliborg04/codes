import pygame
import pymunk
import pymunk.pygame_util
import random

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 1000)
draw_opts = pymunk.pygame_util.DrawOptions(screen)


line1 = pymunk.Segment(space.static_body, (0, 500), (0, 100), 5)
line1.elasticity = 0.5
line1.friction = 0.1
space.add(line1)

line2 = pymunk.Segment(space.static_body, (0, 100), (200, 0), 5)
line2.elasticity = 0.5
line2.friction = 0.1
space.add(line2)

line3 = pymunk.Segment(space.static_body, (200, 0), (500, 0), 5)
line3.elasticity = 0.5
line3.friction = 0.1
space.add(line3)

line4 = pymunk.Segment(space.static_body, (500, 0), (500, 300), 5)
line4.elasticity = 0.5
line4.friction = 0.1
space.add(line4)

line5 = pymunk.Segment(space.static_body, (500,  300), (100, 350), 5)
line5.elasticity = 0.5
line5.friction = 0.1                       
space.add(line5)

i = 0
bodies = []
while i < 20:
    body = pymunk.Body()
    body.position = (400, 50)
    r = random.randint(10, 20)
    shape = pymunk.Circle(body, r)
    shape.mass = r/10
    shape.elasticity = 0.5
    shape.friction = 0.1
    bodies.append(body)
    space.add(body, shape)
    i += 1

while True:
    space.step(1/60)
    screen.fill((0, 0, 0))
    space.debug_draw(draw_opts)
    pygame.display.flip()
    clock.tick(60)
