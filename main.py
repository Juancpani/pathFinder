import pygame, sys
from pygame.locals import *

# CONSTANTS
N = 50
M = 50
SCREEN_SIZE = (500, 600)
SQUARE_LEN = 500 / 50
MARGIN = 0
BLACK = (0, 0, 0)
RED = (250, 0, 0)
GREEN = (0, 250, 0)
WHITE = (250, 250, 250)

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
clock = pygame.time.Clock()
grid = [[None for j in range(M)] for _ in range(N)]
selected = [[False for j in range(M)] for _ in range(N)]

for i in range(50):
    for j in range(50):
        x = SQUARE_LEN * j
        y = SQUARE_LEN * i
        rect = pygame.Rect(x, y, SQUARE_LEN, SQUARE_LEN)
        grid[i][j] = rect

def draw():
    for i in range(N + 1):
        width = 1
        horizontalStart = (MARGIN, MARGIN + (i * SQUARE_LEN))
        horizontalEnd = (SCREEN_SIZE[0] - MARGIN, MARGIN + (i * SQUARE_LEN))
        verticalStart = (MARGIN + (i * SQUARE_LEN), MARGIN)
        verticalEnd = (MARGIN + (i * SQUARE_LEN), SCREEN_SIZE[0] - MARGIN)

        pygame.draw.line(screen, BLACK, horizontalStart, horizontalEnd, width)
        pygame.draw.line(screen, BLACK, verticalStart, verticalEnd, width)
    
    for i in range(N):
        for j in range(M):
            rect = grid[i][j]
            taken = selected[i][j]
            if taken:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect, 1)


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for row in grid:
                    for rect in row:
                        if rect.collidepoint(pos):
                            i = int(rect.y // SQUARE_LEN)
                            j = int(rect.x // SQUARE_LEN)
                            selected[i][j] = True

        screen.fill(WHITE)
        draw()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    sys.exit()

main()


