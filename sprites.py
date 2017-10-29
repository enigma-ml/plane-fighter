import pygame


class TextBtn:
    def __init__(self, pos=(0, 0), size=(0, 0), text="", font='arial',
                 font_size=20, text_color=(0, 0, 0), bg=(255, 255, 255)):
        self.text = text
        self.font = pygame.font.SysFont(font, font_size)
        self.x = pos[0]
        self.y = pos[1]
        self.w = size[0]
        self.h = size[1]
        self.bg = bg
        self.color = text_color
        self.surf = self._set_text()
        self.rect = self._get_rect()

    def _get_rect(self):
        rect = self.surf.get_rect()
        rect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        return rect

    def _set_text(self):
        return self.font.render(self.text, True, self.color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w, self.h))
        screen.blit(self.surf, self.rect)
