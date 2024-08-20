import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 1000)
draw_opts = pymunk.pygame_util.DrawOptions(screen)

body = pymunk.Body()
body.position = (250, 0)
shape = pymunk.Circle(body, 10)
shape.mass = 1
shape.elasticity = 0.7
shape.friction = 1
space.add(body, shape)

line1 = pymunk.Segment(space.static_body, (160, 320), (400, 266), 0)
line1.elasticity = 0.7
line1.friction = 1
space.add(line1)
line2 = pymunk.Segment(space.static_body, (40, 200), (280, 220), 2)
line2.elasticity = 0.7
line2.friction = 1
space.add(line2)

line3 = pymunk.Segment(space.static_body, (0, 450), (500, 500), 2)
line3.elasticity = 0.7
line3.friction = 1
space.add(line3)

stop_line1 = pymunk.Segment(space.static_body, (0, 450), (0, 400), 2)
stop_line1.elasticity = 0.7
stop_line1.friction = 1
space.add(stop_line1)

stop_line2 = pymunk.Segment(space.static_body, (500, 500), (500, 450), 2)
stop_line2.elasticity = 0.7
stop_line2.friction = 1
space.add(stop_line2)

while True:
   space.step(1/60)
   screen.fill((0, 0, 0))
   space.debug_draw(draw_opts)
   pygame.display.flip()
   clock.tick(60)
