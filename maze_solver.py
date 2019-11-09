import pygame
import random

class Solver(object):
    def __init__(self, lab_game, wallcoords, player):
        self.lab_game = lab_game
        self.wallcoords = wallcoords
        self.wayfound = False
        self.celldict = {(1, 1): None}
        self.cells = [(1, 1)]
        self.waylist = []
        self.player = player
        self.solve()

    def draw_cell(self, c):
        self.lab_game.fill((255, 255, 255))
        pygame.draw.rect(self.lab_game, (0, 0, 0), (0, 0, 50 * 20, 50))
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

    def solve(self):
        global clock
        clock = pygame.time.Clock()
        while not self.wayfound:
            pygame.time.delay(2)
            clock.tick(100)
            self.cells = self.add_neighbours(self.cells)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
        while True:
            print ("Im heree")
            for i in range(len(self.waylist)):
                self.lab_game.fill((255, 255, 255))
                pygame.draw.rect(self.lab_game, (0, 0, 0), (0, 0, 50 * 20, 50))
                for c in reversed(self.waylist[-i:]):
                    clock.tick(100)
                    pygame.time.delay(1)
                    self.drawGrid()
                    self.drawMaze()
                    if c == self.waylist[-i]:
                        self.lab_game.blit(self.player.pic, ((c[0]-1) * 20 + 1, (c[1]-1) * 20 + 51))
                    else:
                        pygame.draw.rect(self.lab_game, (0, 255, 0), ((c[0]-1) * 20 + 8, (c[1]-1) * 20 + 58, 4, 4))
                pygame.display.update()
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
