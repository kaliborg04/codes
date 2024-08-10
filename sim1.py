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

i = 0
while i < 10:
    body = pymunk.Body()
    x = random.randint(100, 400)
    body.position = (x, 0)
    r = random.randint(10, 20)
    shape = pymunk.Circle(body, r)
    shape.mass = 1
    shape.elasticity = 0.7
    shape.friction = 1
    space.add(body, shape)
    i += 1

line1 = pymunk.Segment(space.static_body, (250, 150), (480, 70), 2)
line1.elasticity = 0.7
line1.friction = 1
space.add(line1)

line2 = pymunk.Segment(space.static_body, (50, 150), (280, 240), 2)
line2.elasticity = 0.7
line2.friction = 1
space.add(line2)

line3 = pymunk.Segment(space.static_body, (250, 350), (480, 270), 2)
line3.elasticity = 0.7
line3.friction = 1
space.add(line3)

line4 = pymunk.Segment(space.static_body, (50, 400), (500, 500), 2)
line4.elasticity = 0.7
line4.friction = 1
space.add(line4)
stop_line = pymunk.Segment(space.static_body, (500,  500), (500, 460), 3)
stop_line.elasticity = 0.7
stop_line.friction = 1                       
space.add(stop_line)

while True:
   space.step(1/60)
   screen.fill((0, 0, 0))
   space.debug_draw(draw_opts)
   pygame.display.flip()
   clock.tick(60)
