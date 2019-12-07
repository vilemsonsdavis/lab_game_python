import pygame

class Button():
    def __init__(self, display, x, y, width, height, text, isExit):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.text = self.add_text(text)
        self.isExit = isExit

    def color_button(self):
        mouse_on_button = self.isMouseOn()
        if mouse_on_button:
            if self.isExit:
                self.color = (255, 0, 0)
            else:
                self.color = (0, 255, 0)
        else:
            self.color = (255, 255, 255)

    def isMouseOn(self):   #90, 50, 210, 50
        mouse_pos = pygame.mouse.get_pos()
        if (mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + self.width) and \
                (mouse_pos[1] >= self.y and mouse_pos[1] <= self.y + self.height):
            return True
        else:
            return False

    def draw(self):
        self.color_button()
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))
        self.display.blit(self.text, (self.x, self.y))

    def add_text(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 30)
        return font.render(text, False, (0, 0, 0))


