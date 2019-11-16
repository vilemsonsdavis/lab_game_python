import pygame
import menu as m
import database as db


def redrawMenu(menu):
    menu.fill((0, 0, 0))

    exit_col = (255, 255, 255)
    user_col = (255, 255, 255)
    rec_col = (255, 255, 255)
    menu_col = (255, 255, 255)

    mouse_pos = pygame.mouse.get_pos()
    if (mouse_pos[0] >= 95 and mouse_pos[0] <= 305) and (mouse_pos[1] >= 50 and mouse_pos[1] <= 100):
        play_col = (0, 255, 0)
    if (mouse_pos[0] >= 95 and mouse_pos[0] <= 305) and (mouse_pos[1] >= 133 and mouse_pos[1] <= 183):
        user_col = (0, 255, 0)
    if (mouse_pos[0] >= 95 and mouse_pos[0] <= 305) and (mouse_pos[1] >= 216 and mouse_pos[1] <= 266):
        rec_col = (0, 255, 0)
    if (mouse_pos[0] >= 95 and mouse_pos[0] <= 305) and (mouse_pos[1] >= 299 and mouse_pos[1] <= 349):
        exit_col = (255, 0, 0)

    pygame.draw.rect(menu, menu_col, (90, 50, 210, 50))
    pygame.draw.rect(menu, user_col, (90, 133, 210, 50))
    pygame.draw.rect(menu, rec_col, (90, 216, 210, 50))
    pygame.draw.rect(menu, exit_col, (90, 299, 210, 50))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    menubutton = myfont.render('Menu', False, (0, 0, 0))
    userbutton = myfont.render('Fill user info', False, (0, 0, 0))
    recbutton = myfont.render('Records', False, (0, 0, 0))
    exitbutton = myfont.render('Exit', False, (0, 0, 0))
    menu.blit(menubutton, (170, 50))
    menu.blit(userbutton, (100, 133))
    menu.blit(recbutton, (123, 216))
    menu.blit(exitbutton, (170, 299))
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

                if (pos[0] >= 95 and pos[0] <= 305) and (pos[1] >= 50 and pos[1] <= 100):
                    m.Menu()
                if (pos[0] >= 95 and pos[0] <= 305) and (pos[1] >= 133 and pos[1] <= 183):
                    pass
                    # TO DO - implement user info filling log
                if (pos[0] >= 95 and pos[0] <= 305) and (pos[1] >= 216 and pos[1] <= 266):
                    db.read_users()
                if (pos[0] >= 95 and pos[0] <= 305) and (pos[1] >= 299 and pos[1] <= 349):
                    pygame.quit()

        redrawMenu(menu)

main()
