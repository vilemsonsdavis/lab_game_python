import pygame
import labyrinth
import player_menu as pm


class Menu(object):
    def __init__(self):
        self.main()

    def redrawMenu(self, menu):
        menu.fill((0, 0, 0))

        game_col = (255, 255, 255)
        exit_col = (255, 255, 255)
        mus_col = (255, 255, 255)
        play_col = (255, 255, 255)

        mouse_pos = pygame.mouse.get_pos()
        if (mouse_pos[0] >= 95 and mouse_pos[0] <= 305) and (mouse_pos[1] >= 50 and mouse_pos[1] <= 100):
            game_col = (0, 255, 0)
        if (mouse_pos[0] >= 95 and mouse_pos[0] <= 305) and (mouse_pos[1] >= 133 and mouse_pos[1] <= 183):
            play_col = (0, 255, 0)
        if (mouse_pos[0] >= 95 and mouse_pos[0] <= 305) and (mouse_pos[1] >= 216 and mouse_pos[1] <= 266):
            if not musicb:
                mus_col = (0, 255, 0)
            else:
                mus_col = (255, 0, 0)
        if (mouse_pos[0] >= 95 and mouse_pos[0] <= 305) and (mouse_pos[1] >= 299 and mouse_pos[1] <= 349):
            exit_col = (255, 0, 0)

        pygame.draw.rect(menu, game_col, (90, 50, 210, 50))
        pygame.draw.rect(menu, play_col, (90, 133, 210, 50))
        pygame.draw.rect(menu, mus_col, (90, 216, 210, 50))
        pygame.draw.rect(menu, exit_col, (90, 299, 210, 50))
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        gamebutton = myfont.render('Play', False, (0, 0, 0))
        playbutton = myfont.render('Choose Player', False, (0, 0, 0))
        musicbutton = myfont.render(music, False, (0, 0, 0))
        exitbutton = myfont.render('Exit', False, (0, 0, 0))
        menu.blit(gamebutton, (170, 50))
        menu.blit(playbutton, (100, 133))
        menu.blit(musicbutton, (123, 216))
        menu.blit(exitbutton, (170, 299))
        pygame.display.update()

    def main(self):
        global width, height, music, musicb
        music = 'Music: ON'
        width = 400
        height = 400
        run = True
        ok = False
        musicb = True
        playermenu = False

        while run:
            menu = pygame.display.set_mode((width, height))
            pygame.display.set_caption("Davis maze game Main Menu")

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ok = True
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP and ok:
                    pos = pygame.mouse.get_pos()
                    ok = False

                    if (pos[0] >= 95 and pos[0] <= 305) and (pos[1] >= 50 and pos[1] <= 100):
                        if not playermenu:
                            labyrinth.Labyrinth('king')
                        else:
                            labyrinth.Labyrinth(pmo.player)
                    if (pos[0] >= 95 and pos[0] <= 305) and (pos[1] >= 133 and pos[1] <= 183):
                        pmo = pm.PlayerMenu()
                        playermenu = True
                    if (pos[0] >= 95 and pos[0] <= 305) and (pos[1] >= 216 and pos[1] <= 266):
                        if musicb:
                            music = 'Music: OFF'
                            musicb = False
                        else:
                            music = 'Music: ON'
                            musicb = True
                    if (pos[0] >= 95 and pos[0] <= 305) and (pos[1] >= 299 and pos[1] <= 349):
                        run = False

            self.redrawMenu(menu)
