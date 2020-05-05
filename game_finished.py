import pygame
import button

you_won = pygame.image.load('lab_game/youwon.gif')

class Game_Finished(object):
    def __init__(self):
        self.width = 1000
        self.height = 650
        self.run = True
        self.play_again = False
        self.finish_display = self.play_again_button = self.exit_button = None
        self.main()

    def create_buttons(self):
        self.play_again_button = button.Button(self.finish_display, 200, 475, 600, 40, "Play Again", False)
        self.exit_button = button.Button(self.finish_display, 200, 550, 600, 40, "Exit", True)

    def draw_buttons(self):
        self.play_again_button.draw()
        self.exit_button.draw()

    def draw_display(self):
        self.finish_display.fill((0, 0, 0))
        self.finish_display.blit(you_won, (290, 50))
        self.draw_buttons()
        pygame.display.update()

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONUP:
                self.check_for_action()

    def check_for_action(self):
        if self.play_again_button.isMouseOn():
            self.run = False
            self.play_again = True
        elif self.exit_button.isMouseOn():
            self.run = False

    def create_display(self):
        self.finish_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Villy's labyrinth game")
        clock = pygame.time.Clock()
        pygame.time.delay(2)
        clock.tick(100)

    def main(self):
        self.create_display()
        self.create_buttons()

        while self.run:
            self.check_events()
            self.draw_display()