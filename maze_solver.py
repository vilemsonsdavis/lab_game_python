import pygame
import button

arr_left = pygame.image.load('lab_game/green_arrow_left.png')
arr_right = pygame.image.load('lab_game/green_arrow_right.png')
arr_up = pygame.image.load('lab_game/green_arrow_up.png')
arr_down = pygame.image.load('lab_game/green_arrow_down.png')

class Solver(object):
    def __init__(self, lab_game, wall_coords, player):
        self.lab_game = lab_game
        self.wall_coords = wall_coords
        self.correct_way_found = False
        self.cell_mapping = {(1, 1): None}
        self.cells = [(1, 1)]
        self.correct_way_cells = []
        self.do_exit = False
        self.exit_button = None
        self.player = player
        self.finish_position = (50, 30)
        self.solve()

    def exit(self):
        self.player.x = 1
        self.player.y = 51
        self.player.pic = self.player.playerd[0]

    def create_buttons(self):
        self.exit_button = button.Button(self.lab_game, 800, 5, 180, 40, "Exit Solution", True)

    def draw_buttons(self):
        self.exit_button.draw()

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                self.check_for_action()

    def check_for_action(self):
        if self.exit_button.isMouseOn():
            self.do_exit = True

    def draw_game(self):
        self.lab_game.fill((255, 255, 255))
        pygame.draw.rect(self.lab_game, (0, 0, 0), (0, 0, 50 * 20, 50))
        self.draw_buttons()
        self.draw_grid()
        self.draw_maze()

    def draw_cell(self, c):
        self.draw_game()
        for cl in self.cell_mapping.keys():
            pygame.draw.rect(self.lab_game, (0, 0, 255), ((cl[0]-1) * 20, (cl[1] - 1) * 20 + 50, 20, 20))
        pygame.draw.rect(self.lab_game, (0, 255, 0), ((c[0]-1) * 20, (c[1] - 1) * 20 + 50, 20, 20))
        pygame.display.update()

    def backtrack_way(self):
        cell = (50, 30)
        while cell != None:
            self.correct_way_cells.append(cell)
            cell = self.cell_mapping[cell]
        self.correct_way_found = True

    def draw_maze(self):
        for wall in self.wall_coords:
            pygame.draw.line(self.lab_game, (255, 255, 255), wall[0], wall[1])

    def draw_grid(self):
        for i in range(50):
            pygame.draw.line(self.lab_game, (0, 0, 0), (i * 20, 50), (i * 20, 650), 1)
        for i in range(30):
            pygame.draw.line(self.lab_game, (0, 0, 0), (0, i * 20 + 50), (1000, i * 20 + 50), 1)

    def mark_cell(self, cell, prev_neighbour, neighbours):
        self.cell_mapping[cell] = prev_neighbour
        neighbours.append(cell)
        self.draw_cell(cell)
        if self.finish_position in self.cell_mapping.keys():
            self.backtrack_way()

    def add_neighbours(self, prev_neighbours):
        neighbours = []
        for prev_neighbour in prev_neighbours:
            x = prev_neighbour[0]
            y = prev_neighbour[1]
            rightwall = ((x * 20, (y - 1) * 20 + 51), (x * 20, y * 20 + 49))
            leftwall = (((x-1) * 20, (y - 1) * 20 + 51), ((x-1) * 20, y * 20 + 49))
            downwall = (((x-1) * 20 + 1, y * 20 + 50), (x * 20 - 1, y * 20 + 50))
            upwall = (((x - 1) * 20 + 1, (y-1) * 20 + 50), (x * 20 - 1, (y-1) * 20 + 50))
            left_cell = (x - 1, y)
            right_cell = (x + 1, y)
            up_cell = (x, y - 1)
            down_cell = (x, y + 1)

            if right_cell not in self.cell_mapping.keys() and right_cell[0] <= 50 and rightwall in self.wall_coords:
                self.mark_cell(right_cell, prev_neighbour, neighbours)
            if left_cell not in self.cell_mapping.keys() and left_cell[0] >= 1 and leftwall in self.wall_coords:
                self.mark_cell(left_cell, prev_neighbour, neighbours)
            if down_cell not in self.cell_mapping.keys() and down_cell[1] <= 30 and downwall in self.wall_coords:
                self.mark_cell(down_cell, prev_neighbour, neighbours)
            if up_cell not in self.cell_mapping.keys() and up_cell[1] >= 1 and upwall in self.wall_coords:
                self.mark_cell(up_cell, prev_neighbour, neighbours)

        return neighbours

    def walk(self, prev):
        for i in range(20):
            clock.tick(100)
            pygame.time.delay(2)
            pygame.display.update()
            pygame.draw.rect(self.lab_game, (255, 255, 255), (self.player.x, self.player.y, 18, 18))
            if prev == 'right':
                self.player.x += 1
                self.player.pic = self.player.playerr[int(self.player.walk_count / 5) % 2]
            elif prev == 'left':
                self.player.x -= 1
                self.player.pic = self.player.playerl[int(self.player.walk_count / 5) % 2]
            elif prev == 'up':
                self.player.y -= 1
                self.player.pic = self.player.playeru[int(self.player.walk_count / 5) % 2]
            elif prev == 'down':
                self.player.y += 1
                self.player.pic = self.player.playerd[int(self.player.walk_count / 5) % 2]
            self.player.walk_count += 1
            self.player.draw_player()
            self.check_events()
            self.draw_buttons()

    def draw_solution(self):
        prev = None
        while True:
            self.draw_game()
            self.player.x = 1
            self.player.y = 51
            for e, c in enumerate(reversed(self.correct_way_cells), 2):
                if e - 1 > len(self.correct_way_cells):
                    break

                moving_ver_x = (c[0] - 1) * 20 + 1
                prev_up_y = c[1] * 20 + 51
                prev_down_y = (c[1] - 2) * 20 + 51
                moving_hor_y = (c[1] - 1) * 20 + 51
                prev_left_x = c[0] * 20 + 1
                prev_right_x = (c[0] - 2) * 20 + 1
                if prev == 'right':
                    self.lab_game.blit(arr_right, (prev_right_x, moving_hor_y))
                if prev == 'left':
                    self.lab_game.blit(arr_left, (prev_left_x, moving_hor_y))
                if prev == 'up':
                    self.lab_game.blit(arr_up, (moving_ver_x, prev_up_y))
                if prev == 'down':
                    self.lab_game.blit(arr_down, (moving_ver_x, prev_down_y))

                if e - len(self.correct_way_cells) != 1:
                    if c[0] < self.correct_way_cells[-e][0]:
                        prev = 'right'
                    if c[0] > self.correct_way_cells[-e][0]:
                        prev = 'left'
                    if c[1] < self.correct_way_cells[-e][1]:
                        prev = 'down'
                    if c[1] > self.correct_way_cells[-e][1]:
                        prev = 'up'

                self.walk(prev)
                if self.do_exit:
                    self.exit()
                    return
            clock.tick(10)
            pygame.time.delay(10)

    def solve(self):
        self.create_buttons()
        global clock
        clock = pygame.time.Clock()
        while not self.correct_way_found:
            pygame.time.delay(2)
            clock.tick(100)
            self.cells = self.add_neighbours(self.cells)
            self.check_events()
            if self.do_exit:
                self.exit()
                return
        self.draw_solution()
