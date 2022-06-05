import pygame
from random import *

# 게임 스크린 그리기
def BlockRender():
    for row_idx, row in enumerate(game_grid_list):
        for col_idx, col in enumerate(row):
            if col == 8:
                DrawBlock(col_idx, row_idx, WHITE)
            elif col == 1:
                DrawBlock(col_idx, row_idx, MINT)
            elif col == 2:
                DrawBlock(col_idx, row_idx, PURPLE)
            elif col == 3:
                DrawBlock(col_idx, row_idx, BLUE)
            elif col == 4:
                DrawBlock(col_idx, row_idx, ORANGE)
            elif col == 5:
                DrawBlock(col_idx, row_idx, YELLOW)
            elif col == 6:
                DrawBlock(col_idx, row_idx, RED)
            elif col == 7:
                DrawBlock(col_idx, row_idx, GREEN)
            elif col == 9:
                DrawBlock(col_idx, row_idx, GRAY)

# 블록 그리기
def DrawBlock(col_idx, row_idx, color):
    center_x = (col_idx * cell_size) + (cell_size / 2)
    center_y = (row_idx * cell_size) + (cell_size / 2) - 50

    block = pygame.Rect(0, 0, block_size, block_size)
    block.center = (center_x, center_y)

    pygame.draw.rect(screen, color, block)

# 블록 포지션 세팅
def BlockPositionSet(id):
    game_grid_list[block_pos_0[1]][block_pos_0[0]] = id
    game_grid_list[block_pos_1[1]][block_pos_1[0]] = id
    game_grid_list[block_pos_2[1]][block_pos_2[0]] = id
    game_grid_list[block_pos_3[1]][block_pos_3[0]] = id

# 블록 스폰하기
def SpawnBlock(id):
    global block_pos_0, block_pos_1, block_pos_2, block_pos_3
    # 인덱스 0은 x, 1은 y좌표를 의미
    if id == 0:
        pass
    elif id == 1:
        block_pos_0 = [5, 2]
        block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
        block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
        block_pos_3 = [block_pos_0[0] + 2, block_pos_0[1]]
    elif id == 2:
        block_pos_0 = [5, 3]
        block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
        block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
        block_pos_3 = [block_pos_0[0], block_pos_0[1] - 1]
    elif id == 3:
        block_pos_0 = [5, 3]
        block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
        block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
        block_pos_3 = [block_pos_0[0] - 1, block_pos_0[1] - 1]
    elif id == 4:
        block_pos_0 = [5, 3]
        block_pos_1 = [block_pos_0[0] + 1, block_pos_0[1]]
        block_pos_2 = [block_pos_0[0] - 1, block_pos_0[1]]
        block_pos_3 = [block_pos_0[0] + 1, block_pos_0[1] - 1]
    elif id == 5:
        block_pos_0 = [5, 3]
        block_pos_1 = [block_pos_0[0] + 1, block_pos_0[1]]
        block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1] - 1]
        block_pos_3 = [block_pos_0[0], block_pos_0[1] - 1]
    elif id == 6:
        block_pos_0 = [5, 3]
        block_pos_1 = [block_pos_0[0] + 1, block_pos_0[1]]
        block_pos_2 = [block_pos_0[0], block_pos_0[1] - 1]
        block_pos_3 = [block_pos_0[0] - 1, block_pos_0[1] - 1]
    elif id == 7:
        block_pos_0 = [5, 3]
        block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
        block_pos_2 = [block_pos_0[0], block_pos_0[1] - 1]
        block_pos_3 = [block_pos_0[0] + 1, block_pos_0[1] - 1]

    BlockPositionSet(id)

# 블록 떨어지기
def DroppingBlock():
    global block_pos_0, block_pos_1, block_pos_2, block_pos_3, start_ticks, block_start_move, Running, rotate, drop_time
    drop_time = 1.5 / level
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    if elapsed_time > drop_time:
        if game_grid_list[block_pos_0[1] + 1][block_pos_0[0]] == 8 or game_grid_list[block_pos_1[1] + 1][block_pos_1[0]] == 8 or\
           game_grid_list[block_pos_2[1] + 1][block_pos_2[0]] == 8 or game_grid_list[block_pos_3[1] + 1][block_pos_3[0]] == 8 or\
           game_grid_list[block_pos_0[1] + 1][block_pos_0[0]] == 9 or game_grid_list[block_pos_1[1] + 1][block_pos_1[0]] == 9 or\
           game_grid_list[block_pos_2[1] + 1][block_pos_2[0]] == 9 or game_grid_list[block_pos_3[1] + 1][block_pos_3[0]] == 9:
            
            block_start_move = False
            BlockPositionSet(9)
        else:
            start_ticks = pygame.time.get_ticks()
            BlockPositionSet(0)
            block_pos_0 = [block_pos_0[0], block_pos_0[1] + 1]
            block_pos_1 = [block_pos_1[0], block_pos_1[1] + 1]
            block_pos_2 = [block_pos_2[0], block_pos_2[1] + 1]
            block_pos_3 = [block_pos_3[0], block_pos_3[1] + 1]
            BlockPositionSet(id)
        
# 블록 왼쪽으로 움직이기
def BlockMoveLeft():
    global block_pos_0, block_pos_1, block_pos_2, block_pos_3
    if game_grid_list[block_pos_0[1]][block_pos_0[0] - 1] == 8 or game_grid_list[block_pos_1[1]][block_pos_1[0] - 1] == 8 or\
       game_grid_list[block_pos_2[1]][block_pos_2[0] - 1] == 8 or game_grid_list[block_pos_3[1]][block_pos_3[0] - 1] == 8 or\
       game_grid_list[block_pos_0[1]][block_pos_0[0] - 1] == 9 or game_grid_list[block_pos_1[1]][block_pos_1[0] - 1] == 9 or\
       game_grid_list[block_pos_2[1]][block_pos_2[0] - 1] == 9 or game_grid_list[block_pos_3[1]][block_pos_3[0] - 1] == 9:
        pass
    else:
        BlockPositionSet(0)
        block_pos_0 = [block_pos_0[0] - 1, block_pos_0[1]]
        block_pos_1 = [block_pos_1[0] - 1, block_pos_1[1]]
        block_pos_2 = [block_pos_2[0] - 1, block_pos_2[1]]
        block_pos_3 = [block_pos_3[0] - 1, block_pos_3[1]]
        BlockPositionSet(id)

# 블록 오른쪽으로 움직이기
def BlockMoveRight():
    global block_pos_0, block_pos_1, block_pos_2, block_pos_3
    if game_grid_list[block_pos_0[1]][block_pos_0[0] + 1] == 8 or game_grid_list[block_pos_1[1]][block_pos_1[0] + 1] == 8 or\
       game_grid_list[block_pos_2[1]][block_pos_2[0] + 1] == 8 or game_grid_list[block_pos_3[1]][block_pos_3[0] + 1] == 8 or\
       game_grid_list[block_pos_0[1]][block_pos_0[0] + 1] == 9 or game_grid_list[block_pos_1[1]][block_pos_1[0] + 1] == 9 or\
       game_grid_list[block_pos_2[1]][block_pos_2[0] + 1] == 9 or game_grid_list[block_pos_3[1]][block_pos_3[0] + 1] == 9:
        pass
    else:
        BlockPositionSet(0)
        block_pos_0 = [block_pos_0[0] + 1, block_pos_0[1]]
        block_pos_1 = [block_pos_1[0] + 1, block_pos_1[1]]
        block_pos_2 = [block_pos_2[0] + 1, block_pos_2[1]]
        block_pos_3 = [block_pos_3[0] + 1, block_pos_3[1]]
        BlockPositionSet(id)

# 블록 빠르게 내려가기
def Drop():
    global block_pos_0, block_pos_1, block_pos_2, block_pos_3, block_start_move, drop_time
    if game_grid_list[block_pos_0[1] + 1][block_pos_0[0]] == 8 or game_grid_list[block_pos_1[1] + 1][block_pos_1[0]] == 8 or\
       game_grid_list[block_pos_2[1] + 1][block_pos_2[0]] == 8 or game_grid_list[block_pos_3[1] + 1][block_pos_3[0]] == 8 or\
       game_grid_list[block_pos_0[1] + 1][block_pos_0[0]] == 9 or game_grid_list[block_pos_1[1] + 1][block_pos_1[0]] == 9 or\
       game_grid_list[block_pos_2[1] + 1][block_pos_2[0]] == 9 or game_grid_list[block_pos_3[1] + 1][block_pos_3[0]] == 9:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > drop_time:
            block_start_move = False

    else:
        BlockPositionSet(0)
        block_pos_0 = [block_pos_0[0], block_pos_0[1] + 1]
        block_pos_1 = [block_pos_1[0], block_pos_1[1] + 1]
        block_pos_2 = [block_pos_2[0], block_pos_2[1] + 1]
        block_pos_3 = [block_pos_3[0], block_pos_3[1] + 1]
        BlockPositionSet(id)

# 블록 바로 내려가기
def HardDrop():
    global block_pos_0, block_pos_1, block_pos_2, block_pos_3, block_start_move
    BlockPositionSet(0)
    while True:
        if (game_grid_list[block_pos_0[1] + 1][block_pos_0[0]] or game_grid_list[block_pos_1[1] + 1][block_pos_1[0]]
         or game_grid_list[block_pos_2[1] + 1][block_pos_2[0]] or game_grid_list[block_pos_3[1] + 1][block_pos_3[0]]) == 8 \
         or (game_grid_list[block_pos_0[1] + 1][block_pos_0[0]] or game_grid_list[block_pos_1[1] + 1][block_pos_1[0]]
         or game_grid_list[block_pos_2[1] + 1][block_pos_2[0]] or game_grid_list[block_pos_3[1] + 1][block_pos_3[0]]) == 9:

            BlockPositionSet(9)
            block_start_move = False
            break
        else:
            block_pos_0 = [block_pos_0[0], block_pos_0[1] + 1]
            block_pos_1 = [block_pos_1[0], block_pos_1[1] + 1]
            block_pos_2 = [block_pos_2[0], block_pos_2[1] + 1]
            block_pos_3 = [block_pos_3[0], block_pos_3[1] + 1]

# 블록 돌리기
def RotateBlock(id, rot):
    global block_pos_0, block_pos_1, block_pos_2, block_pos_3, rotate
    if game_grid_list[block_pos_0[1] - 1][block_pos_0[0] - 1] == 8 or game_grid_list[block_pos_0[1]][block_pos_0[0] - 1] == 8 or\
       game_grid_list[block_pos_0[1] + 1][block_pos_0[0] - 1] == 8 or game_grid_list[block_pos_0[1] - 1][block_pos_0[0]] == 8 or\
       game_grid_list[block_pos_0[1] + 1][block_pos_0[0]] == 8 or game_grid_list[block_pos_0[1] - 1][block_pos_0[0] + 1] == 8 or\
       game_grid_list[block_pos_0[1]][block_pos_0[0] + 1] == 8 or game_grid_list[block_pos_0[1] + 1][block_pos_0[0] + 1] == 8 or\
       game_grid_list[block_pos_0[1] - 1][block_pos_0[0] - 1] == 9 or game_grid_list[block_pos_0[1]][block_pos_0[0] - 1] == 9 or\
       game_grid_list[block_pos_0[1] + 1][block_pos_0[0] - 1] == 9 or game_grid_list[block_pos_0[1] - 1][block_pos_0[0]] == 9 or\
       game_grid_list[block_pos_0[1] + 1][block_pos_0[0]] == 9 or game_grid_list[block_pos_0[1] - 1][block_pos_0[0] + 1] == 9 or\
       game_grid_list[block_pos_0[1]][block_pos_0[0] + 1] == 9 or game_grid_list[block_pos_0[1] + 1][block_pos_0[0] + 1] == 9:
            print("dhfb")
            rotate -= 1
            return
    else:
        BlockPositionSet(0)
        if id == 1:
            if rot == 0 or rot == 2:
                rotate = 0
                block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
                block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
                block_pos_3 = [block_pos_0[0] + 2, block_pos_0[1]]
            elif rot == 1:
                block_pos_1 = [block_pos_0[0], block_pos_0[1] + 1]
                block_pos_2 = [block_pos_0[0], block_pos_0[1] - 1]
                block_pos_3 = [block_pos_0[0], block_pos_0[1] - 2]
        elif id == 2:
            if rot == 0 or rot == 4:
                rotate = 0
                block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
                block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
                block_pos_3 = [block_pos_0[0], block_pos_0[1] - 1]
            elif rot == 1:
                block_pos_1 = [block_pos_0[0], block_pos_0[1] - 1]
                block_pos_2 = [block_pos_0[0], block_pos_0[1] + 1]
                block_pos_3 = [block_pos_0[0] + 1, block_pos_0[1]]
            elif rot == 2:
                block_pos_1 = [block_pos_0[0] + 1, block_pos_0[1]]
                block_pos_2 = [block_pos_0[0] - 1, block_pos_0[1]]
                block_pos_3 = [block_pos_0[0], block_pos_0[1] + 1]
            elif rot == 3:
                block_pos_1 = [block_pos_0[0], block_pos_0[1] + 1]
                block_pos_2 = [block_pos_0[0] - 1, block_pos_0[1]]
                block_pos_3 = [block_pos_0[0], block_pos_0[1] - 1]
        elif id == 3:
            if rot == 0 or rot == 4:
                rotate = 0
                block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
                block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
                block_pos_3 = [block_pos_0[0] - 1, block_pos_0[1] - 1]
            elif rot == 1:
                block_pos_1 = [block_pos_0[0], block_pos_0[1] - 1]
                block_pos_2 = [block_pos_0[0], block_pos_0[1] + 1]
                block_pos_3 = [block_pos_0[0] + 1, block_pos_0[1] - 1]
            elif rot == 2:
                block_pos_1 = [block_pos_0[0] + 1, block_pos_0[1]]
                block_pos_2 = [block_pos_0[0] - 1, block_pos_0[1]]
                block_pos_3 = [block_pos_0[0] + 1, block_pos_0[1] + 1]
            elif rot == 3:
                block_pos_1 = [block_pos_0[0], block_pos_0[1] + 1]
                block_pos_2 = [block_pos_0[0], block_pos_0[1] - 1]
                block_pos_3 = [block_pos_0[0] - 1, block_pos_0[1] + 1]
        elif id == 4:
            if rot == 0 or rot == 4:
                rotate = 0
                block_pos_1 = [block_pos_0[0] + 1, block_pos_0[1]]
                block_pos_2 = [block_pos_0[0] - 1, block_pos_0[1]]
                block_pos_3 = [block_pos_0[0] + 1, block_pos_0[1] - 1]
            elif rot == 1:
                block_pos_1 = [block_pos_0[0], block_pos_0[1] + 1]
                block_pos_2 = [block_pos_0[0], block_pos_0[1] - 1]
                block_pos_3 = [block_pos_0[0] + 1, block_pos_0[1] + 1]
            elif rot == 2:
                block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
                block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
                block_pos_3 = [block_pos_0[0] - 1, block_pos_0[1] + 1]
            elif rot == 3:
                block_pos_1 = [block_pos_0[0], block_pos_0[1] - 1]
                block_pos_2 = [block_pos_0[0], block_pos_0[1] + 1]
                block_pos_3 = [block_pos_0[0] - 1, block_pos_0[1] - 1]
        elif id == 6:
            if rot == 0 or rot == 2:
                rotate = 0
                block_pos_1 = [block_pos_0[0] + 1, block_pos_0[1]]
                block_pos_2 = [block_pos_0[0], block_pos_0[1] - 1]
                block_pos_3 = [block_pos_0[0] - 1, block_pos_0[1] - 1]
            elif rot == 1:
                block_pos_1 = [block_pos_0[0], block_pos_0[1] + 1]
                block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
                block_pos_3 = [block_pos_0[0] + 1, block_pos_0[1] - 1]
        elif id == 7:
            if rot == 0 or rot == 2:
                rotate = 0
                block_pos_1 = [block_pos_0[0] - 1, block_pos_0[1]]
                block_pos_2 = [block_pos_0[0], block_pos_0[1] - 1]
                block_pos_3 = [block_pos_0[0] + 1, block_pos_0[1] - 1]
            elif rot == 1:
                block_pos_1 = [block_pos_0[0], block_pos_0[1] - 1]
                block_pos_2 = [block_pos_0[0] + 1, block_pos_0[1]]
                block_pos_3 = [block_pos_0[0] + 1, block_pos_0[1] + 1]

        BlockPositionSet(id)

# 블록 라인 점검 (완성되면 삭제)  
def LineCheck():
    clear_line = 0
    for idx, line in enumerate(game_grid_list):
        success = True
        for idx_bl, block in enumerate(line):
            if idx_bl == 9:
                continue
            if block == 0:
                success = False
                break
            if idx == rows - 1:
                success = False

        if success == True:
            del game_grid_list[idx]
            game_grid_list.insert(0, [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8])
            clear_line += 1
    ScoreAndLevel(clear_line)

# 점수와 레벨관리
def ScoreAndLevel(cl):
    global level, score
    score += randrange(50, 151) * cl
    level = score // 1000
    print(level, score)

#블록 홀드
def BlockHold():
    global block_start_move, hold_block_id, next_block_id, step, id, hold
    BlockPositionSet(0)
    if hold_block_id == None:  # hold 처음
        hold_block_id = id
        next_block_id = randrange(1, 8)
        id = next_block_id
    else:
        step = id
        id = hold_block_id
        hold_block_id = step


# 초기화
pygame.init()
screen_width = 300
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# 기본 세팅 값
rows = 22
columns = 12
cell_size = 25
block_size = 21
block_start_move = False
drop_time = None
start_ticks = None
level = 1
score = 1000
id = 0
rotate = 0
hold = False
hold_block_id = None
next_block_id = None
step = None

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
GRAY = (128, 128, 128)  # 9

# 현재 블록의 위치
block_pos_0 = []
block_pos_1 = []
block_pos_2 = []
block_pos_3 = []

# 블록 스피드
k_left_speed = 0
k_right_speed = 0
k_down_speed = 0

# 폰트
game_font = pygame.font.Font(None, 120)

# 기본 틀 그리기
game_grid_list = [[0 for col in range(columns)] for row in range(rows)]
for idx, grid in enumerate(game_grid_list):
    game_grid_list[idx][0] = 8
    game_grid_list[idx][columns - 1] = 8
for idx, grid in enumerate(game_grid_list[rows - 1]):
    game_grid_list[rows - 1][idx] = 8

# main
Running = True
while Running:

    for event in pygame.event.get():  # 키보드, 마우스 입력 받기
        if event.type == pygame.QUIT:  # 종료
            Running = False
        elif event.type == pygame.KEYDOWN:  # 아래방향키
            if event.key == pygame.K_SPACE:
                HardDrop()
            elif event.key == pygame.K_UP:  # 위방향키
                rotate += 1
                RotateBlock(id, rotate)
            elif event.key == pygame.K_LEFT:  # 왼쪽방향키
                BlockMoveLeft()
            elif event.key == pygame.K_RIGHT:  # 오른쪽방향키
                BlockMoveRight()
            elif event.key == pygame.K_c:
                hold = True
                block_start_move = False
                BlockHold()

    if event.type == pygame.KEYDOWN:  # 키가 눌렸을 때
        if event.key == pygame.K_LEFT:
            k_left_speed += 0.1
            if k_left_speed >= 15:
                k_left_speed = 0
                BlockMoveLeft()
        elif event.key == pygame.K_RIGHT:
            k_right_speed += 0.1
            if k_right_speed >= 15:
                k_right_speed = 0
                BlockMoveRight()
        elif event.key == pygame.K_DOWN:
            k_down_speed += 0.1
            if k_down_speed >= 5 // level:
                k_down_speed = 0
                Drop()

    elif event.type == pygame.KEYUP:  # 키를 땠을 때 스피드 초기화
        k_left_speed = 0
        k_right_speed = 0
        k_down_speed = 0
        
    if block_start_move == False:  # 처음 시작하거나 블록이 배치되거나 hold할 때, 새 블록 생성하기
        # 게임오버체크
        for idx, grid in enumerate(game_grid_list[0]):
            if game_grid_list[2][idx] == 9:
                Running = False
                break
        LineCheck()
        rotate = 0
        if hold == True:
            hold = False
        else:
            next_block_id = randrange(1, 8)
            id = next_block_id
        start_ticks = pygame.time.get_ticks()
        SpawnBlock(id)
        block_start_move = True

    DroppingBlock()  # 시간이 지나며 떨어짐
    screen.fill(BLACK)
    BlockRender()  # 리스트 화면 출력

    pygame.display.update()  # !!! 제발 마지막에 작성 꼭! 해주기 !!!


# msg = game_font.render(f"Your level is {level}", True, WHITE)
# msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))
# screen.fill(BLACK)
# screen.blit(msg,msg_rect)

# 3초 보여주고 종료
#pygame.time.delay(3000)
pygame.quit()