import pygame
skeleton = pygame.image.load('lab_game/skl1_fr1_menu.gif')
king = pygame.image.load('lab_game/kin1_fr1_menu.gif')
predator = pygame.image.load('lab_game/chr1_fr1_menu.gif')
grandpa = pygame.image.load('lab_game/wmg2_fr1_menu.gif')


class PlayerMenu(object):
    def __init__(self):
        self.main()
        self.player

    def drawPlayerNames(self, menu):
        pos = pygame.mouse.get_pos()
        if (pos[0] >= 135 and pos[0] <= 265) and (pos[1] >= 15 and pos[1] <= 50):
            back_col = (0, 255, 0)
        else:
            back_col = (255, 255, 255)

        pygame.draw.rect(menu, king_col, (60, 185, 130, 30))
        pygame.draw.rect(menu, skel_col, (210, 185, 130, 30))
        pygame.draw.rect(menu, pred_col, (60, 335, 130, 30))
        pygame.draw.rect(menu, gra_col, (210, 335, 130, 30))
        pygame.draw.rect(menu, back_col, (135, 15, 130, 35))
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        king_txt = myfont.render('King', False, (0, 0, 0))
        skel_txt = myfont.render('Skeleton', False, (0, 0, 0))
        pred_txt = myfont.render('Predator', False, (0, 0, 0))
        gra_txt = myfont.render('Grandpa', False, (0, 0, 0))
        menu.blit(king_txt, (100, 180))
        menu.blit(skel_txt, (220, 180))
        menu.blit(pred_txt, (75, 330))
        menu.blit(gra_txt, (225, 330))
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        back_button = myfont.render('DONE', False, (0, 0, 0))
        menu.blit(back_button, (155, 10))

    def redrawMenu(self, menu):
        menu.fill((0, 0, 0))
        menu.blit(king, (75, 75))
        menu.blit(skeleton, (225, 75))
        menu.blit(predator, (75, 225))
        menu.blit(grandpa, (225, 225))
        self.drawPlayerNames(menu)
        pygame.display.update()

    def main(self):
        global width, height, skel_col, king_col, gra_col, pred_col, back_col
        skel_col = (255, 0, 0)
        king_col = (0, 255, 0)
        gra_col = (255, 0, 0)
        pred_col = (255, 0, 0)
        self.player = 'king'
        width = 400
        height = 400
        run = True

        while run:
            menu = pygame.display.set_mode((width, height))
            pygame.display.set_caption("Choose player")

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    if (pos[0] >= 60 and pos[0] <= 190) and (pos[1] >= 185 and pos[1] <= 215):
                        king_col = (0, 255, 0)
                        skel_col = (255, 0, 0)
                        gra_col = (255, 0, 0)
                        pred_col = (255, 0, 0)
                        self.player = 'king'
                    if (pos[0] >= 210 and pos[0] <= 340) and (pos[1] >= 185 and pos[1] <= 225):
                        skel_col = (0, 255, 0)
                        king_col = (255, 0, 0)
                        gra_col = (255, 0, 0)
                        pred_col = (255, 0, 0)
                        self.player = 'skeleton'
                    if (pos[0] >= 60 and pos[0] <= 190) and (pos[1] >= 335 and pos[1] <= 365):
                        pred_col = (0, 255, 0)
                        skel_col = (255, 0, 0)
                        gra_col = (255, 0, 0)
                        king_col = (255, 0, 0)
                        self.player = 'predator'
                    if (pos[0] >= 210 and pos[0] <= 340) and (pos[1] >= 335 and pos[1] <= 365):
                        gra_col = (0, 255, 0)
                        skel_col = (255, 0, 0)
                        king_col = (255, 0, 0)
                        pred_col = (255, 0, 0)
                        self.player = 'grandpa'
                    if (pos[0] >= 135 and pos[0] <= 265) and (pos[1] >= 15 and pos[1] <= 50):
                        run = False

            self.redrawMenu(menu)
