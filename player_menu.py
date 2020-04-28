import pygame
import button


skeleton = pygame.image.load('lab_game/skl1_fr1_menu.gif')
king = pygame.image.load('lab_game/kin1_fr1_menu.gif')
predator = pygame.image.load('lab_game/chr1_fr1_menu.gif')
grandpa = pygame.image.load('lab_game/wmg2_fr1_menu.gif')


class PlayerMenu(object):
    def __init__(self):
        self.king_button = self.skel_button = self.pred_button \
                = self.grandpa_button = self.done_button = self.player = self.menu_display = None
        self.run = True
        self.main()


    def create_buttons(self):
        self.king_button = button.Button(self.menu_display, 60, 185, 130, 30, "King", False)
        self.skel_button = button.Button(self.menu_display, 210, 185, 130, 30, "Skeleton", False)
        self.pred_button = button.Button(self.menu_display, 60, 335, 130, 30, "Predator", False)
        self.grandpa_button = button.Button(self.menu_display, 210, 335, 130, 30, "Grandpa", False)
        self.done_button = button.Button(self.menu_display, 135, 15, 130, 35, "DONE", True)

    def draw_buttons(self):
        self.king_button.draw()
        self.skel_button.draw()
        self.pred_button.draw()
        self.grandpa_button.draw()
        self.done_button.draw()

    def check_for_action(self):
        pos = pygame.mouse.get_pos()

        if (60 <= pos[0] <= 190) and (185 <= pos[1] <= 215):
            self.king_button.color = (255, 0, 0)
            self.skel_button.color = (255, 255, 255)
            self.pred_button.color = (255, 255, 255)
            self.grandpa_button.color = (255, 255, 255)
            self.player = 'king'
        if (210 <= pos[0] <= 340) and (185 <= pos[1] <= 225):
            self.skel_button.color = (255, 0, 0)
            self.king_button.color = (255, 255, 255)
            self.pred_button.color = (255, 255, 255)
            self.grandpa_button.color = (255, 255, 255)
            self.player = 'skeleton'
        if (60 <= pos[0] <= 190) and (335 <= pos[1] <= 365):
            self.pred_button.color = (255, 0, 0)
            self.king_button.color = (255, 255, 255)
            self.skel_button.color = (255, 255, 255)
            self.grandpa_button.color = (255, 255, 255)
            self.player = 'predator'
        if (210 <= pos[0] <= 340) and (335 <= pos[1] <= 365):
            self.grandpa_button.color = (255, 0, 0)
            self.king_button.color = (255, 255, 255)
            self.skel_button.color = (255, 255, 255)
            self.pred_button.color = (255, 255, 255)
            self.player = 'grandpa'
        if (135 <= pos[0] <= 265) and (15 <= pos[1] <= 50):
            self.run = False

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONUP:
                self.check_for_action()

    def draw_player_icons(self):
        self.menu_display.blit(king, (75, 75))
        self.menu_display.blit(skeleton, (225, 75))
        self.menu_display.blit(predator, (75, 225))
        self.menu_display.blit(grandpa, (225, 225))

    def draw_menu(self):
        self.menu_display.fill((0, 0, 0))
        self.draw_player_icons()
        self.draw_buttons()
        pygame.display.update()

    def main(self):
        width = height = 400
        self.menu_display = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Choose player")
        self.create_buttons()
        self.player = 'king'
        self.king_button.color = (255, 0, 0)

        while self.run:
            self.check_events()
            self.draw_menu()
