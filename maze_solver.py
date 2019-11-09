import pygame
import random

arr_left = pygame.image.load('lab_game/green_arrow_left.png')
arr_right = pygame.image.load('lab_game/green_arrow_right.png')
arr_up = pygame.image.load('lab_game/green_arrow_up.png')
arr_down = pygame.image.load('lab_game/green_arrow_down.png')

class Solver(object):
    def __init__(self, lab_game, wallcoords, player):
        self.lab_game = lab_game
        self.wallcoords = wallcoords
        self.wayfound = False
        self.celldict = {(1, 1): None}
        self.cells = [(1, 1)]
        self.waylist = []
        self.exit = False
        self.player = player
        self.solve()

    def draw_buttons(self):
        width = 1000
        exit_col = (255, 255, 255)
        mouse_pos = pygame.mouse.get_pos()

        if (mouse_pos[0] >= width - 200 and mouse_pos[0] <= width - 20) and (mouse_pos[1] >= 5 and mouse_pos[1] <= 45):
            exit_col = (255, 0, 0)

        pygame.draw.rect(self.lab_game, (0, 0, 0), (0, 0, width, 50))
        pygame.draw.rect(self.lab_game, exit_col, (width - 200, 5, 180, 40))
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        exit = myfont.render('Exit Solution', False, (0, 0, 0))
        self.lab_game.blit(exit, (width - 190, 5))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if (pos[0] >= width - 200 and pos[0] <= width - 20) and (pos[1] >= 5 and pos[1] <= 45):
                    self.exit = True

    def draw_cell(self, c):
        self.lab_game.fill((255, 255, 255))
        pygame.draw.rect(self.lab_game, (0, 0, 0), (0, 0, 50 * 20, 50))
        self.draw_buttons()
        self.drawGrid()
        self.drawMaze()
        for cl in self.celldict.keys():
            pygame.draw.rect(self.lab_game, (0, 0, 255), ((cl[0]-1) * 20, (cl[1] - 1) * 20 + 50, 20, 20))
        pygame.draw.rect(self.lab_game, (0, 255, 0), ((c[0]-1) * 20, (c[1] - 1) * 20 + 50, 20, 20))
        pygame.display.update()

    def backtrack_way(self):
        cell = (50, 30)
        while cell != None:
            self.waylist.append(cell)
            cell = self.celldict[cell]
        self.wayfound = True

    def drawMaze(self):
        for wall in self.wallcoords:
            pygame.draw.line(self.lab_game, (255, 255, 255), wall[0], wall[1])

    def drawGrid(self):
        for i in range(50):
            pygame.draw.line(self.lab_game, (0, 0, 0), (i * 20, 50), (i * 20, 650), 1)
        for i in range(30):
            pygame.draw.line(self.lab_game, (0, 0, 0), (0, i * 20 + 50), (1000, i * 20 + 50), 1)

    def add_neighbours(self, prev_neighbours):
        neighbours = []
        for pv in prev_neighbours:
            x = pv[0]
            y = pv[1]
            rightwall = ((x * 20, (y - 1) * 20 + 51), (x * 20, y * 20 + 49))
            leftwall = (((x-1) * 20, (y - 1) * 20 + 51), ((x-1) * 20, y * 20 + 49))
            upwall = (((x-1) * 20 + 1, y * 20 + 50), (x * 20 - 1, y * 20 + 50))
            downwall = (((x - 1) * 20 + 1, (y-1) * 20 + 50), (x * 20 - 1, (y-1) * 20 + 50))

            if (x + 1, y) not in self.celldict.keys() and x + 1 <= 50 and rightwall in self.wallcoords:
                self.celldict[(x+1, y)] = (x, y)
                neighbours.append((x + 1, y))
                self.draw_cell((x+1, y))
            if (x - 1, y) not in self.celldict.keys() and x - 1 >= 1 and leftwall in self.wallcoords:
                self.celldict[(x-1, y)] = (x, y)
                neighbours.append((x - 1, y))
                self.draw_cell((x - 1, y))
            if (x, y + 1) not in self.celldict.keys() and y + 1 <= 30 and upwall in self.wallcoords:
                self.celldict[(x, y+1)] = (x, y)
                neighbours.append((x, y + 1))
                self.draw_cell((x, y + 1))
            if (x, y - 1) not in self.celldict.keys() and y - 1 >= 1 and downwall in self.wallcoords:
                self.celldict[(x, y-1)] = (x, y)
                neighbours.append((x, y - 1))
                self.draw_cell((x, y - 1))
        if (50, 30) in self.celldict.keys():
            self.backtrack_way()

        return neighbours

    def draw_solution(self):
        self.lab_game.fill((255, 255, 255))
        pygame.draw.rect(self.lab_game, (0, 0, 0), (0, 0, 50 * 20, 50))
        self.drawGrid()
        self.drawMaze()
        prev = None
        while True:
            for e, c in enumerate(reversed(self.waylist), 2):
                clock.tick(10)
                pygame.time.delay(10)
                if e > len(self.waylist):
                    break

                self.lab_game.blit(self.player.pic, ((c[0] - 1) * 20 + 1, (c[1] - 1) * 20 + 51))

                if prev == 'right':
                    self.lab_game.blit(arr_right, ((c[0] - 2) * 20 + 1, (c[1] - 1) * 20 + 51))
                if prev == 'left':
                    self.lab_game.blit(arr_left, (c[0] * 20 + 1, (c[1] - 1) * 20 + 51))
                if prev == 'up':
                    self.lab_game.blit(arr_up, ((c[0] - 1) * 20 + 1, c[1] * 20 + 51))
                if prev == 'down':
                    self.lab_game.blit(arr_down, ((c[0] - 1) * 20 + 1, (c[1] - 2) * 20 + 51))

                if c[0] < self.waylist[-e][0]:
                    prev = 'right'
                if c[0] > self.waylist[-e][0]:
                    prev = 'left'
                if c[1] < self.waylist[-e][1]:
                    prev = 'down'
                if c[1] > self.waylist[-e][1]:
                    prev = 'up'

                pygame.display.update()
                self.draw_buttons()
                if self.exit:
                    return

    def solve(self):
        global clock
        clock = pygame.time.Clock()
        while not self.wayfound:
            pygame.time.delay(2)
            clock.tick(100)
            self.cells = self.add_neighbours(self.cells)
            if self.exit:
                return

        self.draw_solution()
