import pygame
import menu as m


def redrawMenu(menu):
    menu.fill((0, 0, 0))

    game_col = (255, 255, 255)
    exit_col = (255, 255, 255)

    mouse_pos = pygame.mouse.get_pos()
    if (mouse_pos[0] >= 120 and mouse_pos[0] <= 280) and (mouse_pos[1] >= 225 and mouse_pos[1] <= 275):
        exit_col = (255, 0, 0)
    if (mouse_pos[0] >= 120 and mouse_pos[0] <= 280) and (mouse_pos[1] >= 125 and mouse_pos[1] <= 175):
        game_col = (0, 255, 0)

    pygame.draw.rect(menu, game_col, (120, 125, 160, 50))
    pygame.draw.rect(menu, exit_col, (120, 225, 160, 50))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    playbutton = myfont.render('Menu', False, (0, 0, 0))
    exitbutton = myfont.render('Exit', False, (0, 0, 0))
    menu.blit(playbutton, (170, 125))
    menu.blit(exitbutton, (175, 225))
    pygame.display.update()

def main():
    global width, height
    width = 400
    height = 400
    run = True
    ok = False

    while run:
        menu = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Davis maze game Main Menu")

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                ok = True
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and ok:
                ok = False
                pos = pygame.mouse.get_pos()

                if (pos[0] >= 120 and pos[0] <= 280) and (pos[1] >= 225 and pos[1] <= 275):
                    pygame.quit()
                if (pos[0] >= 120 and pos[0] <= 280) and (pos[1] >= 125 and pos[1] <= 175):
                    m.Menu()

        redrawMenu(menu)

main()
