import pygame
from random import *

# 초기화
pygame.init()
screen_width = 300
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# 기본 세팅 값
rows = 20
columns = 12
cell_size = 25
block_size = 21
cell_margin = 2

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 기본 틀 그리기
game_basic_grid = [[0 for col in range(columns)] for row in range(rows)]
for idx, grid in enumerate(game_basic_grid):
    game_basic_grid[idx][0] = 1
    game_basic_grid[idx][columns - 1] = 1
for idx, grid in enumerate(game_basic_grid[rows - 1]):
    game_basic_grid[rows - 1][idx] = 1

# 게임 스크린 그리기
def game_screen():
    for row_idx, row in enumerate(game_basic_grid):
        for col_idx, col in enumerate(row):
            if col != 0:
                center_x = (col_idx * cell_size) + (cell_size / 2)
                center_y = (row_idx * cell_size) + (cell_size / 2)

                block = pygame.Rect(0, 0, block_size, block_size)
                block.center = (center_x, center_y)

                pygame.draw.rect(screen, WHITE, block)
                
# main
Running = True
while Running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    screen.fill(BLACK)
    game_screen()

    pygame.display.update()  # !!! 제발 마지막에 작성 꼭! 해주기 !!!

pygame.quit()