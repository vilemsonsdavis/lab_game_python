import pygame
import maze_gen
import maze_solver as ms
import player as p
import button
import game_finished


class Labyrinth(object):
    def __init__(self, player_name):
        self.width = 1000
        self.height = 650
        self.player_name = player_name
        self.rows = 30
        self.columns = 50
        self.maze = self.player = self.generate_maze_button = self.draw_maze_button \
            = self.solve_maze_button = self.exit_button = self.solved = self.game_display = None
        self.run = True
        self.create_display()
        self.main()

    def check_for_action(self):
        if self.generate_maze_button.isMouseOn():
            self.maze = maze_gen.Generator((self.height - 50) / 20, self.width / 20, self.game_display, True)
            self.player = p.Player(self.player_name, self.game_display, self.maze.wall_coordinations)
        elif self.draw_maze_button.isMouseOn():
            self.maze = maze_gen.Generator((self.height - 50) / 20, self.width / 20, self.game_display, False)
            self.player = p.Player(self.player_name, self.game_display, self.maze.wall_coordinations)
        elif self.solve_maze_button.isMouseOn():
            self.solved = ms.Solver(self.game_display, self.maze.wall_coordinations, self.player)
        elif self.exit_button.isMouseOn():
            self.run = False

    def create_buttons(self):
        self.generate_maze_button = button.Button(self.game_display, 300, 5, 210, 40, "Generate new maze", False)
        self.draw_maze_button = button.Button(self.game_display, 20, 5, 250, 40, "Draw new maze", False)
        self.solve_maze_button = button.Button(self.game_display, 610, 5, 200, 40, "Solve", False)
        self.exit_button = button.Button(self.game_display, 900, 5, 100, 40, "Exit", True)

    def draw_buttons(self):
        self.generate_maze_button.draw()
        self.draw_maze_button.draw()
        self.solve_maze_button.draw()
        self.exit_button.draw()

    def draw_display(self):
        self.game_display.fill((255, 255, 255))
        pygame.draw.rect(self.game_display, (0, 0, 0), (0, 0, self.width, 50))
        self.draw_grid()
        self.draw_buttons()
        self.draw_maze()
        self.player.move_player()
        self.player.draw_player()
        pygame.display.update()

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONUP:
                self.check_for_action()

        if self.player.x >= 980 and self.player.y >= 630:
            gf = game_finished.Game_Finished()
            if gf.play_again:
                self.maze = maze_gen.Generator((self.height - 50) / 20, self.width / 20, self.game_display, False)
                self.player = p.Player(self.player_name, self.game_display, self.maze.wall_coordinations)
            else:
                self.run = False

    def create_display(self):
        self.game_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Villy's labyrinth game")
        clock = pygame.time.Clock()
        pygame.time.delay(2)
        clock.tick(100)

    def draw_maze(self):
        for wall in self.maze.wall_coordinations:
            pygame.draw.line(self.game_display, (255, 255, 255), wall[0], wall[1])

    def draw_grid(self):
        for i in range(self.columns):
            pygame.draw.line(self.game_display, (0, 0, 0), (i * 20, 50), (i * 20, 650), 1)
        for i in range(self.rows):
            pygame.draw.line(self.game_display, (0, 0, 0), (0, i * 20 + 50), (1000, i * 20 + 50), 1)

    def main(self):
        self.create_buttons()
        self.maze = maze_gen.Generator((self.height - 50) / 20, self.width / 20, self.game_display, False)
        self.player = p.Player(self.player_name, self.game_display, self.maze.wall_coordinations)

        while self.run:
            self.check_events()
            self.draw_display()
