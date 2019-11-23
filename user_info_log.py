import pygame


class User_info_log ():
    def __init__(self):
        self.main()

    def redrawMenu(self, menu):
        menu.fill((0, 0, 0))

        back_col = (255, 255, 255)

        mouse_pos = pygame.mouse.get_pos()
        if (mouse_pos[0] >= 95 and mouse_pos[0] <= 305) and (mouse_pos[1] >= 299 and mouse_pos[1] <= 349):
            back_col = (255, 0, 0)

        pygame.draw.rect(menu, back_col, (90, 299, 210, 50))
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        exitbutton = myfont.render('Back', False, (0, 0, 0))
        menu.blit(exitbutton, (170, 299))
        pygame.display.update()

    def main(self):
        global width, height
        width = 400
        height = 400
        run = True
        ok = False

        while run:
            menu = pygame.display.set_mode((width, height))
            pygame.display.set_caption("User Information log")

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ok = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP and ok:
                    ok = False
                    pos = pygame.mouse.get_pos()

                    if (pos[0] >= 95 and pos[0] <= 305) and (pos[1] >= 299 and pos[1] <= 349):
                        run = False

            self.redrawMenu(menu)