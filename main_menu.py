import pygame
import menu as m
import button


def check_for_action():
    if menu_button.isMouseOn():
        m.Menu()
    elif user_info_button.isMouseOn():
        pass
        # TO DO - implement user info filling log
    elif records_button.isMouseOn():
        pass
        # db.read_users()
    elif exit_button.isMouseOn():
        pygame.quit()


def create_buttons():
    global menu_button, user_info_button, records_button, exit_button
    menu_button = button.Button(menu_display, 90, 50, 210, 50, "Menu", False)
    user_info_button = button.Button(menu_display, 90, 133, 210, 50, "Fill your info", False)
    records_button = button.Button(menu_display, 90, 216, 210, 50, "Records", False)
    exit_button = button.Button(menu_display, 90, 299, 210, 50, "Exit", True)


def draw_buttons():
    menu_button.draw()
    user_info_button.draw()
    records_button.draw()
    exit_button.draw()


def draw_menu(display_menu):
    display_menu.fill((0, 0, 0))
    draw_buttons()
    pygame.display.update()


def check_events():
    global ok
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            ok = True
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP and ok:
            ok = False
            check_for_action()


def main():
    global width, height, menu_display, menu_button, user_info_button, records_button, exit_button, ok
    width = height =  400
    run = ok = True
    menu_display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Davis maze game Main Menu")
    create_buttons()

    while run:
        check_events()
        draw_menu(menu_display)


main()
