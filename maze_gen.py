import pygame
import random

class Generator(object):
    def __init__(self, rows, columns, lab_game, drawMaze):
        self.rows = rows
        self.columns = columns
        self.currentCell = (1, 1)
        self.visitedCells = [(1, 1)]
        self.wayTrack = [(1, 1)]
        self.lab_game = lab_game
        self.wallCoords = []
        self.drawMaze = drawMaze

        self.generate()

    def chooseNeighbour(self):
        possibleNeighbours = []
        if (self.currentCell[0] + 1, self.currentCell[1]) not in self.visitedCells and self.currentCell[0]+1 <= 50:
            possibleNeighbours.append('right')
        if (self.currentCell[0] - 1, self.currentCell[1]) not in self.visitedCells and self.currentCell[0]-1 >= 1:
            possibleNeighbours.append('left')
        if (self.currentCell[0], self.currentCell[1] + 1) not in self.visitedCells and self.currentCell[1]+1 <= 30:
            possibleNeighbours.append('down')
        if (self.currentCell[0], self.currentCell[1] - 1) not in self.visitedCells and self.currentCell[1]-1 >= 1:
            possibleNeighbours.append('up')

        if possibleNeighbours:
            chosen = random.choice(possibleNeighbours)
        else:
            chosen = ""
        return chosen

    def move(self):
        nextCell = self.chooseNeighbour()
        if nextCell is not "":
            if nextCell == 'right':
                self.visitedCells.append((self.currentCell[0] + 1, self.currentCell[1]))
                self.wayTrack.append((self.currentCell[0] + 1, self.currentCell[1]))
                self.wallCoords.append(((self.currentCell[0]*20, (self.currentCell[1]-1)*20+51),
                                        (self.currentCell[0]*20, (self.currentCell[1])*20+49)))
                self.currentCell = (self.currentCell[0] + 1, self.currentCell[1])
            if nextCell == 'left':
                self.visitedCells.append((self.currentCell[0] - 1, self.currentCell[1]))
                self.wayTrack.append((self.currentCell[0] - 1, self.currentCell[1]))
                self.wallCoords.append((((self.currentCell[0]-1) * 20, (self.currentCell[1] - 1) * 20 + 51),
                                        ((self.currentCell[0]-1) * 20, (self.currentCell[1]) * 20 + 49)))
                self.currentCell = (self.currentCell[0] - 1, self.currentCell[1])
            if nextCell == 'down':
                self.visitedCells.append((self.currentCell[0], self.currentCell[1] + 1))
                self.wayTrack.append((self.currentCell[0], self.currentCell[1] + 1))
                self.wallCoords.append((((self.currentCell[0]-1) * 20 + 1, self.currentCell[1] * 20 + 50),
                                        (self.currentCell[0] * 20 - 1, self.currentCell[1] * 20 + 50)))
                self.currentCell = (self.currentCell[0], self.currentCell[1] + 1)
            if nextCell == 'up':
                self.visitedCells.append((self.currentCell[0], self.currentCell[1] - 1))
                self.wayTrack.append((self.currentCell[0], self.currentCell[1] - 1))
                self.wallCoords.append((((self.currentCell[0] - 1) * 20 + 1, (self.currentCell[1]-1) * 20 + 50),
                                        (self.currentCell[0] * 20 - 1, (self.currentCell[1]-1) * 20 + 50)))
                self.currentCell = (self.currentCell[0], self.currentCell[1] - 1)
        else:
            self.wayTrack.pop()
            if len(self.wayTrack) >= 1:
                self.currentCell = self.wayTrack[-1]

    def fillCell(self):
        self.lab_game.fill((255, 255, 255))
        pygame.draw.rect(self.lab_game, (0, 0, 0), (0, 0, self.columns*20, 50))
        self.drawGrid()
        for cell in self.visitedCells:
            if cell is not self.currentCell and cell in self.wayTrack:
                pygame.draw.rect(self.lab_game, (0, 0, 255), ((cell[0] - 1) * 20, (cell[1] - 1) * 20 + 50, 20, 20))
            elif cell is not self.currentCell and cell not in self.wayTrack:
                pygame.draw.rect(self.lab_game, (0, 255, 0), ((cell[0] - 1) * 20, (cell[1] - 1) * 20 + 50, 20, 20))
        pygame.draw.rect(self.lab_game, (255, 0, 0), ((self.currentCell[0]-1) *20, (self.currentCell[1]-1) * 20 + 50, 20, 20))
        pygame.display.update()

    def drawGrid(self):
        for i in range(int(self.columns)):
            pygame.draw.line(self.lab_game, (0, 0, 0), (i * 20, 50), (i * 20, 650), 1)
        for i in range(int(self.rows)):
            pygame.draw.line(self.lab_game, (0, 0, 0), (0, i * 20 + 50), (1000, i * 20 + 50), 1)

    def generate(self):
        clock = pygame.time.Clock()
        while self.wayTrack:
#            pygame.time.delay(0)
#            clock.tick(1500000000)
            if self.drawMaze:
                self.fillCell()
            self.move()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
