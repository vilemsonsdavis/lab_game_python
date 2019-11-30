import pygame
import maze_gen
import maze_solver as ms
import player as p

def drawButtons(lab_game):
    width = 1000
    exit_col = (255,255,255)
    draw_col = (255, 255, 255)
    gen_col = (255, 255, 255)
    solve_col = (255, 255, 255)
    mouse_pos = pygame.mouse.get_pos()

    if (mouse_pos[0] >= width-100 and mouse_pos[0] <= width - 20) and (mouse_pos[1] >= 5 and mouse_pos[1] <= 45):
        exit_col = (255, 0, 0)
    if (mouse_pos[0] >= 20 and mouse_pos[0] <= 270) and (mouse_pos[1] >= 5 and mouse_pos[1] <= 45):
        draw_col = (0, 255, 0)
    if (mouse_pos[0] >= 290 and mouse_pos[0] <= 590) and (mouse_pos[1] >= 5 and mouse_pos[1] <= 45):
        gen_col = (0, 255, 0)
    if (mouse_pos[0] >= 610 and mouse_pos[0] <= 810) and (mouse_pos[1] >= 5 and mouse_pos[1] <= 45):
        solve_col = (0, 255, 0)

    pygame.draw.rect(lab_game, (0, 0, 0), (0, 0, width, 50))
    pygame.draw.rect(lab_game, gen_col, (290, 5, 300, 40))
    pygame.draw.rect(lab_game, draw_col, (20, 5, 250, 40))
    pygame.draw.rect(lab_game, solve_col, (610, 5, 200, 40))
    pygame.draw.rect(lab_game, exit_col, (width-100, 5, 80, 40))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    gennewmazebutton = myfont.render('Generate new maze', False, (0, 0, 0))
    drawmazebutton = myfont.render('Draw new maze', False, (0, 0, 0))
    solvemazebutton = myfont.render('Solve', False, (0, 0, 0))
    exit = myfont.render('Exit', False, (0, 0, 0))
    lab_game.blit(gennewmazebutton, (300, 5))
    lab_game.blit(drawmazebutton, (40, 5))
    lab_game.blit(solvemazebutton, (630, 5))
    lab_game.blit(exit, (width-90, 5))


def drawGrid(lab_game):
    for i in range(columns):
        pygame.draw.line(lab_game, (0,0,0), (i*20, 50), (i*20, 650), 1)
    for i in range(rows):
        pygame.draw.line(lab_game, (0,0,0), (0, i*20+50), (1000, i*20+50), 1)

def redrawWindow(lab_game, width, height):
    lab_game.fill((255, 255, 255))
    drawGrid(lab_game)
    drawMaze(lab_game, maze.wall_coordinations)
    player.movePlayer()
    drawButtons(lab_game)
    player.drawPlayer()
    pygame.display.update()

def drawMaze(lab_game, wallCoords):
    for wall in wallCoords:
        pygame.draw.line(lab_game, (255, 255, 255), wall[0], wall[1])

class Labyrinth(object):
    def __init__(self, player_name):
        self.width = 1000
        self.height = 650
        self.player_name = player_name
        self.lab_game = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Villy's labyrinth game")
        clock = pygame.time.Clock()
        pygame.time.delay(2)
        clock.tick(100)
        global rows, columns
        rows = 30
        columns = 50
        self.main()

    def main(self):
        run = True
        global mazeDrawn, maze, player, solved
        maze = maze_gen.Generator((self.height - 50) / 20, self.width / 20, self.lab_game, False)
        player = p.Player(self.player_name, self.lab_game, maze.wall_coordinations)

        while run:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    if (pos[0] >= 20 and pos[0] <= 270) and (pos[1] >= 5 and pos[1] <= 45):
                        maze = maze_gen.Generator((self.height - 50) / 20, self.width / 20, self.lab_game, True)
                        player = p.Player(self.player_name, self.lab_game, maze.wall_coordinations)
                    if (pos[0] >= 290 and pos[0] <= 590) and (pos[1] >= 5 and pos[1] <= 45):
                        maze = maze_gen.Generator((self.height - 50) / 20, self.width / 20, self.lab_game, False)
                        player = p.Player(self.player_name, self.lab_game, maze.wall_coordinations)
                    if (pos[0] >= 610 and pos[0] <= 810) and (pos[1] >= 5 and pos[1] <= 45):
                        solved = ms.Solver(self.lab_game, maze.wall_coordinations, player)
                    if (pos[0] >= self.width-100 and pos[0] <= self.width - 20) and (pos[1] >= 5 and pos[1] <= 45):
                        run = False

            redrawWindow(self.lab_game, self.width, self.height)
