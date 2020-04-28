import pygame

class Button():
    def __init__(self, display, x, y, width, height, text, isExit):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_width = self.text_height = 0
        self.color = (255, 255, 255)
        self.isExit = isExit
        self.text = self.add_text(text)

    def color_button(self):
        mouse_on_button = self.isMouseOn()

        if mouse_on_button:
            if self.isExit:
                self.color = (255, 0, 0)
            elif not self.isExit and self.color != (255, 0, 0):
                self.color = (0, 255, 0)
        elif not self.isExit and self.color != (255, 0, 0):
            self.color = (255, 255, 255)
        elif self.isExit:
            self.color = (255, 255, 255)

    def isMouseOn(self):
        mouse_pos = pygame.mouse.get_pos()
        if (mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + self.width) and \
                (mouse_pos[1] >= self.y and mouse_pos[1] <= self.y + self.height):
            return True
        else:
            return False

    def draw(self):
        self.color_button()
        text_x_pos = self.x + (self.width - self.text_width) / 2
        text_y_pos = self.y + (self.height - self.text_height) / 2
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))
        self.display.blit(self.text, (text_x_pos, text_y_pos))

    def add_text(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('arial', 25)
        self.text_width, self.text_height = font.size(text)
        return font.render(text, False, (0, 0, 0))


