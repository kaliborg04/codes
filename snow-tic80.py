# script:  python

from random import randint, choice
from math import floor

FLAKES_COUNT = 1000

flakes = []
for i in range(FLAKES_COUNT):
    x = randint(0, 239)
    swing = randint(2, 4)
    vxdir = choice([1, -1])
    flake = {
        'x': x,
        'xmax': x + swing,
        'xmin': x - swing,
        'y': randint(0, 135),
        'vy': randint(7, 12), # pix/sec
        'vx': vxdir * randint(5, 10),
    }
    flakes.append(flake)

frame = 1

def TIC():
    global frame

    frame += 1
    dt = 1/60

    cls(10)
    for flake in flakes:
        dist_y = dt * flake['vy']
        flake['y'] += dist_y
        if flake['y'] >= 136:
            flake['y'] -= 136

        dist_x = dt * flake['vx']
        flake['x'] += dist_x
        if flake['x'] >= flake['xmax']:
            flake['vx'] = -flake['vx']
        if flake['x'] <= flake['xmin']:
            flake['vx'] = -flake['vx']
        
        pix(floor(flake['x']), floor(flake['y']), 12)

    if frame != 5:
        return
    frame = 1
        
    vbank(1)
    x = randint(0, 239)
    y = 135
    while pix(x, y) == 12:
        y -= 1
    tri(x, y, x - 16, y + 8, x + 16, y + 8, 12)
    vbank(0)

# <TILES>
# 001:eccccccccc888888caaaaaaaca888888cacccccccacc0ccccacc0ccccacc0ccc
# 002:ccccceee8888cceeaaaa0cee888a0ceeccca0ccc0cca0c0c0cca0c0c0cca0c0c
# 003:eccccccccc888888caaaaaaaca888888cacccccccacccccccacc0ccccacc0ccc
# 004:ccccceee8888cceeaaaa0cee888a0ceeccca0cccccca0c0c0cca0c0c0cca0c0c
# 017:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 018:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# 019:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 020:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# </TILES>

# <WAVES>
# 000:00000000ffffffff00000000ffffffff
# 001:0123456789abcdeffedcba9876543210
# 002:0123456789abcdef0123456789abcdef
# </WAVES>

# <SFX>
# 000:000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000304000000000
# </SFX>

# <TRACKS>
# 000:100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </TRACKS>

# <PALETTE>
# 000:1a1c2c5d275db13e53ef7d57ffcd75a7f07038b76425717929366f3b5dc941a6f673eff7f4f4f494b0c2566c86333c57
# </PALETTE>

