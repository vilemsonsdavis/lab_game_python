import pygame
import labyrinth
import player_menu as pm
import button


class Menu(object):
    def __init__(self):
        self.music = 'Music: ON'
        self.width = self.height = 400
        self.run = self.musicOn = True
        self.ok = self.playermenu = False
        self.play_button = self.character_button = self.music_button = self.exit_button = self.pmo = self.menu_display = None
        self.create_display()
        self.main()

    def check_for_action(self):
        if self.play_button.isMouseOn():
            if not self.playermenu:
                labyrinth.Labyrinth('king')
            else:
                labyrinth.Labyrinth(self.pmo.player)
            self.create_display()
        elif self.character_button.isMouseOn():
            self.pmo = pm.PlayerMenu()
            self.playermenu = True
        elif self.music_button.isMouseOn():
            if self.musicOn:
                self.music = 'Music: OFF'
                self.musicOn = False
            else:
                self.music = 'Music: ON'
                self.musicOn = True
            self.create_buttons()
        elif self.exit_button.isMouseOn():
            self.run = False

    def create_buttons(self):
        self.play_button = button.Button(self.menu_display, 90, 50, 210, 50, "Play", False)
        self.character_button = button.Button(self.menu_display, 90, 133, 210, 50, "Choose Character", False)
        self.music_button = button.Button(self.menu_display, 90, 216, 210, 50, self.music, False)
        self.exit_button = button.Button(self.menu_display, 90, 299, 210, 50, "Exit", True)

    def draw_buttons(self):
        self.play_button.draw()
        self.character_button.draw()
        self.music_button.draw()
        self.exit_button.draw()

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.ok = True
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONUP and self.ok:
                self.ok = False
                self.check_for_action()

    def draw_menu(self):
        self.menu_display.fill((0, 0, 0))
        self.draw_buttons()
        pygame.display.update()

    def create_display(self):
        self.menu_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Davis maze game Main Menu")

    def main(self):
        self.create_buttons()

        while self.run:
            self.check_events()
            self.draw_menu()
