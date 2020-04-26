import pygame
import random

class Generator(object):
    def __init__(self, rows, columns, game_display, draw_maze):
        self.rows = rows
        self.columns = columns
        self.current_cell = (1, 1)
        self.visited_cells = [(1, 1)]
        self.backup_way = [(1, 1)]
        self.game_display = game_display
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

    def add_maze_drawing_params(self, cell, wall):
        self.visited_cells.append(cell)
        self.backup_way.append(cell)
        self.wall_coordinations.append(wall)
        self.current_cell = cell

    def move(self):
        next_cell = self.choose_neighbour()
        if next_cell is not "" and next_cell in ('right', 'left', 'up', 'down'):
            if next_cell == 'right':
                cell = (self.current_cell[0] + 1, self.current_cell[1])
                point_one = (self.current_cell[0]*20, (self.current_cell[1]-1)*20+51)
                point_two = (self.current_cell[0]*20, (self.current_cell[1])*20+49)
                wall = (point_one, point_two)
            elif next_cell == 'left':
                cell = (self.current_cell[0] - 1, self.current_cell[1])
                point_one = ((self.current_cell[0]-1) * 20, (self.current_cell[1] - 1) * 20 + 51)
                point_two = ((self.current_cell[0]-1) * 20, (self.current_cell[1]) * 20 + 49)
                wall = (point_one, point_two)
            elif next_cell == 'down':
                cell = (self.current_cell[0], self.current_cell[1] + 1)
                point_one = ((self.current_cell[0] - 1) * 20 + 1, self.current_cell[1] * 20 + 50)
                point_two = (self.current_cell[0] * 20 - 1, self.current_cell[1] * 20 + 50)
                wall = (point_one, point_two)
            elif next_cell == 'up':
                cell = (self.current_cell[0], self.current_cell[1] - 1)
                point_one = ((self.current_cell[0] - 1) * 20 + 1, (self.current_cell[1]-1) * 20 + 50)
                point_two = (self.current_cell[0] * 20 - 1, (self.current_cell[1]-1) * 20 + 50)
                wall = (point_one, point_two)
            self.add_maze_drawing_params(cell, wall)
        else:
            self.backup_way.pop()
            if len(self.backup_way) >= 1:
                self.current_cell = self.backup_way[-1]

    def draw_game(self):
        self.game_display.fill((255, 255, 255))
        pygame.draw.rect(self.game_display, (0, 0, 0), (0, 0, self.columns*20, 50))
        self.draw_grid()
        self.color_cells()
        pygame.display.update()

    def color_cells(self):

        def params(cell):
            cell_x = (cell[0] - 1) * 20
            cell_y = (cell[1] - 1) * 20 + 50
            return cell_x, cell_y, 20, 20

        current_cell_params = params(self.current_cell)
        for visited_cell in self.visited_cells:
            cell_params = params(visited_cell)
            if visited_cell is not self.current_cell and visited_cell in self.backup_way:
                pygame.draw.rect(self.game_display, (0, 0, 255), cell_params)
            elif visited_cell is not self.current_cell and visited_cell not in self.backup_way:
                pygame.draw.rect(self.game_display, (0, 255, 0), cell_params)
        pygame.draw.rect(self.game_display, (255, 0, 0), current_cell_params)

    def draw_grid(self):
        for i in range(int(self.columns)):
            pygame.draw.line(self.game_display, (0, 0, 0), (i * 20, 50), (i * 20, 650), 1)
        for i in range(int(self.rows)):
            pygame.draw.line(self.game_display, (0, 0, 0), (0, i * 20 + 50), (1000, i * 20 + 50), 1)

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

    def generate(self):
        while self.backup_way:
            if self.draw_maze:
                self.draw_game()
            self.move()
            self.check_events()
