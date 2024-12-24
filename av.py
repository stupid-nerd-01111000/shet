from pygame import display, event, draw, time 
import numpy as np

RED = (255, 0, 0)
BLACK = (0, 0, 0)


dis = display.set_mode((500, 500))

grid = np.zeros((5, 5))

clock = time.Clock()
count = 0

running = True
while running:
    for e in event.get():
        pass

    dis.fill(BLACK)

    col_idx = np.random.randint(0, 6)
    grid[col_idx]

    grid[:, (count) % 5] = a

    for n1, i in enumerate(grid):
        for n2, j in enumerate(grid):
            if grid[n1, n2] != 0:
                draw.rect(dis, RED, [n1*100, n2*100, 90, 90])

    display.update()
    grid[:, (count + 1) % 5] = a * b
    clock.tick(2)

    count += 1