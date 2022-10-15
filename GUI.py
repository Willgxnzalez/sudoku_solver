import pygame
from sudoku_solver import *
pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sudoku Solver')


CELL_SIZE = SCREEN_WIDTH // 9
COLORS = {'black': (0, 0, 0), 'white': (255, 255, 255)}

board = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 6, 0, 0, 0, 0, 0],
         [0, 7, 0, 0, 9, 0, 2, 0, 0],
         [0, 5, 0, 0, 0, 7, 0, 0, 0],
         [0, 0, 0, 0, 4, 5, 7, 0, 0],
         [0, 0 ,0 ,1 ,0 ,0 ,0 ,3 ,0],
         [0, 0, 1, 0, 0, 0, 0, 6, 8],
         [0, 0, 8, 5, 0, 0, 0, 1, 0],
         [0, 9, 0, 0, 0, 0, 4, 0, 0]]

def update_screen(brd):
    WIN.fill(COLORS['white'])

    # draw grid lines and border
    pygame.draw.rect(WIN, COLORS['black'], (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 5)
    for hor_line, row in enumerate(brd, 1):
        pygame.draw.rect(WIN, COLORS['black'], (0, hor_line*CELL_SIZE, SCREEN_WIDTH, (5 if hor_line % 3 == 0 else 1)))
        for ver_line in range(1, len(row)):
            pygame.draw.rect(WIN, COLORS['black'], (ver_line*CELL_SIZE, 0, (5 if ver_line % 3 == 0 else 1), SCREEN_HEIGHT))

        # draw numbers onto the screen
    for i, row in enumerate(brd):
        for j, value in enumerate(row):
            if value != 0:
                number_font = pygame.font.SysFont('calibri', 30).render(f'{value}', True, COLORS['black'])
                WIN.blit(number_font, (j * CELL_SIZE + number_font.get_width() + 1, i * CELL_SIZE + number_font.get_height() // 2 - 3, 1, 1))

    pygame.display.update()

def main():
    start_solve = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_solve = True
        if start_solve:
            solve(board)

        update_screen(board)


if __name__ == '__main__':
    main()