import pygame
import random

class Generator(object):
    def __init__(self, rows, columns, lab_game, draw_maze):
        self.rows = rows
        self.columns = columns
        self.current_cell = (1, 1)
        self.visited_cells = [(1, 1)]
        self.backup_way = [(1, 1)]
        self.lab_game = lab_game
        self.wall_coordinations = []
        self.draw_maze = draw_maze
        self.generate()

    def choose_neighbour(self):
        possible_neighbours = []
        curr_cell_x = self.current_cell[0]
        curr_cell_y = self.current_cell[1]

        right_cell = (curr_cell_x + 1, curr_cell_y)
        left_cell = (curr_cell_x - 1, curr_cell_y)
        down_cell = (curr_cell_x, curr_cell_y + 1)
        up_cell = (curr_cell_x, curr_cell_y - 1)

        if right_cell not in self.visited_cells and curr_cell_x + 1 <= 50:
            possible_neighbours.append('right')
        if left_cell not in self.visited_cells and curr_cell_x - 1 >= 1:
            possible_neighbours.append('left')
        if down_cell not in self.visited_cells and curr_cell_y + 1 <= 30:
            possible_neighbours.append('down')
        if up_cell not in self.visited_cells and curr_cell_y - 1 >= 1:
            possible_neighbours.append('up')

        if possible_neighbours:
            chosen = random.choice(possible_neighbours)
        else:
            chosen = ""
        return chosen

    def move(self):
        next_cell = self.choose_neighbour()
        if next_cell is not "":
            if next_cell == 'right':
                self.visited_cells.append((self.current_cell[0] + 1, self.current_cell[1]))
                self.backup_way.append((self.current_cell[0] + 1, self.current_cell[1]))
                self.wall_coordinations.append(((self.current_cell[0]*20, (self.current_cell[1]-1)*20+51),
                                        (self.current_cell[0]*20, (self.current_cell[1])*20+49)))
                self.current_cell = (self.current_cell[0] + 1, self.current_cell[1])
            if next_cell == 'left':
                self.visited_cells.append((self.current_cell[0] - 1, self.current_cell[1]))
                self.backup_way.append((self.current_cell[0] - 1, self.current_cell[1]))
                self.wall_coordinations.append((((self.current_cell[0]-1) * 20, (self.current_cell[1] - 1) * 20 + 51),
                                        ((self.current_cell[0]-1) * 20, (self.current_cell[1]) * 20 + 49)))
                self.current_cell = (self.current_cell[0] - 1, self.current_cell[1])
            if next_cell == 'down':
                self.visited_cells.append((self.current_cell[0], self.current_cell[1] + 1))
                self.backup_way.append((self.current_cell[0], self.current_cell[1] + 1))
                self.wall_coordinations.append((((self.current_cell[0]-1) * 20 + 1, self.current_cell[1] * 20 + 50),
                                        (self.current_cell[0] * 20 - 1, self.current_cell[1] * 20 + 50)))
                self.current_cell = (self.current_cell[0], self.current_cell[1] + 1)
            if next_cell == 'up':
                self.visited_cells.append((self.current_cell[0], self.current_cell[1] - 1))
                self.backup_way.append((self.current_cell[0], self.current_cell[1] - 1))
                self.wall_coordinations.append((((self.current_cell[0] - 1) * 20 + 1, (self.current_cell[1]-1) * 20 + 50),
                                        (self.current_cell[0] * 20 - 1, (self.current_cell[1]-1) * 20 + 50)))
                self.current_cell = (self.current_cell[0], self.current_cell[1] - 1)
        else:
            self.backup_way.pop()
            if len(self.backup_way) >= 1:
                self.current_cell = self.backup_way[-1]

    def fill_cell(self):
        self.lab_game.fill((255, 255, 255))
        pygame.draw.rect(self.lab_game, (0, 0, 0), (0, 0, self.columns*20, 50))
        self.drawGrid()
        for cell in self.visited_cells:
            if cell is not self.current_cell and cell in self.backup_way:
                pygame.draw.rect(self.lab_game, (0, 0, 255), ((cell[0] - 1) * 20, (cell[1] - 1) * 20 + 50, 20, 20))
            elif cell is not self.current_cell and cell not in self.backup_way:
                pygame.draw.rect(self.lab_game, (0, 255, 0), ((cell[0] - 1) * 20, (cell[1] - 1) * 20 + 50, 20, 20))
        pygame.draw.rect(self.lab_game, (255, 0, 0), ((self.current_cell[0]-1) *20, (self.current_cell[1]-1) * 20 + 50, 20, 20))
        pygame.display.update()

    def drawGrid(self):
        for i in range(int(self.columns)):
            pygame.draw.line(self.lab_game, (0, 0, 0), (i * 20, 50), (i * 20, 650), 1)
        for i in range(int(self.rows)):
            pygame.draw.line(self.lab_game, (0, 0, 0), (0, i * 20 + 50), (1000, i * 20 + 50), 1)

    def generate(self):
        clock = pygame.time.Clock()
        while self.backup_way:
            if self.draw_maze:
                self.fill_cell()
            self.move()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
