import pygame
from sudoku_solver import *
pygame.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sudoku Solver')



COLORS = {'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0)}

class Cell:
    CELL_SIZE = SCREEN_WIDTH // 9
    board = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 3, 6, 0, 0, 0, 0, 0],
             [0, 7, 0, 0, 9, 0, 2, 0, 0],
             [0, 5, 0, 0, 0, 7, 0, 0, 0],
             [0, 0, 0, 0, 4, 5, 7, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 3, 0],
             [0, 0, 1, 0, 0, 0, 0, 6, 8],
             [0, 0, 8, 5, 0, 0, 0, 1, 0],
             [0, 9, 0, 0, 0, 0, 4, 0, 0]]
    @classmethod
    def create_cells(cls):
        return [[cls(val, (i, j), 30, COLORS['white']) for j, val in enumerate(row)] for i, row in enumerate(Cell.board)]

    def __init__(self, value, pos, size, color):
        self.value = value
        self.x, self.y = pos
        self.size = size
        self.color = color

    def highlight(self, color):
        self.color = color

    def update(self, value):
        self.value = value




def update_screen(cells):
    WIN.fill(COLORS['white'])

    for row in cells:
        for cell in row:
            if cell.value != 0:
                pygame.draw.rect(WIN, cell.color, (cell.x*cell.CELL_SIZE, cell.y*cell.CELL_SIZE, cell.CELL_SIZE, cell.CELL_SIZE))
                number_font = pygame.font.SysFont('cambria', 35).render(f'{cell.value}', True, COLORS['black'])
                WIN.blit(number_font, (cell.x*cell.CELL_SIZE+14, cell.y*cell.CELL_SIZE+2))
    # draw grid lines and border
    pygame.draw.rect(WIN, COLORS['black'], (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 5)
    for hor_line in range(1, 9):
        pygame.draw.rect(WIN, COLORS['black'], (0, hor_line*Cell.CELL_SIZE, SCREEN_WIDTH, (5 if hor_line % 3 == 0 else 1)))
        for ver_line in range(1, 9):
            pygame.draw.rect(WIN, COLORS['black'], (ver_line*Cell.CELL_SIZE, 0, (5 if ver_line % 3 == 0 else 1), SCREEN_HEIGHT))

    pygame.display.update()


def main():
    run = True
    cells = Cell.create_cells()
    print(cells)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve(Cell.board, cells)



        update_screen(cells)


if __name__ == '__main__':
    main()