import pygame
import sudoku_solver
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

    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update_screen(board)


if __name__ == '__main__':
    main()