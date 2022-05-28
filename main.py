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
BLACK = (0, 0, 0)  # 0
MINT = (0, 255, 255)  # 1
PURPLE = (127, 0, 255)  # 2
ORANGE = (255, 128, 0)  # 3
BLUE = (0, 0, 255)  # 4
YELLOW = (255, 255, 0)  # 5
GREEN = (0, 255, 0)  # 6
RED = (255, 0, 0)  # 7
WHITE = (255, 255, 255)  # 8


block_start_move = False

# 기본 틀 그리기
game_grid_list = [[0 for col in range(columns)] for row in range(rows)]
for idx, grid in enumerate(game_grid_list):
    game_grid_list[idx][0] = 8
    game_grid_list[idx][columns - 1] = 8
for idx, grid in enumerate(game_grid_list[rows - 1]):
    game_grid_list[rows - 1][idx] = 8

def DrawBlock(col_idx, row_idx, color):
    center_x = (col_idx * cell_size) + (cell_size / 2)
    center_y = (row_idx * cell_size) + (cell_size / 2)

    block = pygame.Rect(0, 0, block_size, block_size)
    block.center = (center_x, center_y)

    pygame.draw.rect(screen, color, block)

# 게임 스크린 그리기
def BlockPrint():
    for row_idx, row in enumerate(game_grid_list):
        for col_idx, col in enumerate(row):
            if col == 8:
                DrawBlock(col_idx, row_idx, WHITE)
            elif col == 1:
                DrawBlock(col_idx, row_idx, MINT)
            elif col == 2:
                DrawBlock(col_idx, row_idx, PURPLE)
            elif col == 3:
                DrawBlock(col_idx, row_idx, ORANGE)
            elif col == 4:
                DrawBlock(col_idx, row_idx, BLUE)
            elif col == 5:
                DrawBlock(col_idx, row_idx, YELLOW)
            elif col == 6:
                DrawBlock(col_idx, row_idx, GREEN)
            elif col == 7:
                DrawBlock(col_idx, row_idx, RED)
                
def SpawnBlock(id):
    # 인덱스 0은 x, 1은 y좌표를 의미
    if id == 0:
        pass
    elif id == 1:
        block_pos_0 = [5, 0]
        block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
        block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
        block_pos_3 = [block_pos_0[0] + 2, block_pos_0[1]]
    elif id == 2:
        block_pos_0 = [5, 1]
        block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
        block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
        block_pos_3 = [block_pos_0[0], block_pos_0[1] - 1]
    elif id == 3:
        block_pos_0 = [5, 1]
        block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
        block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
        block_pos_3 = [block_pos_0[0] - 1, block_pos_0[1] - 1]

    game_grid_list[block_pos_0[1]][block_pos_0[0]] = id
    game_grid_list[block_pos_1[1]][block_pos_1[0]] = id
    game_grid_list[block_pos_2[1]][block_pos_2[0]] = id
    game_grid_list[block_pos_3[1]][block_pos_3[0]] = id    

# main
Running = True
while Running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    if block_start_move == False:
        id = randrange(1, 8)
        SpawnBlock(3)
        block_start_move = True
    screen.fill(BLACK)
    BlockPrint()

    pygame.display.update()  # !!! 제발 마지막에 작성 꼭! 해주기 !!!

pygame.quit()