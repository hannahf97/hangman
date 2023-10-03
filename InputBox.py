import pygame as pg
from tkinter import *
from tkinter import messagebox

pg.init()
screen = pg.display.set_mode((800, 600))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font('source/Jalnan.ttf', 40)
BLACK =(0,0,0)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        Tk().wm_withdraw()
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.result = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.result = self.text
                    print(self.result)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    self.text += event.unicode
                    if len(self.text) > 2:
                        messagebox.showinfo("주의 !", "한글자만 입력하세요! ")
                        self.text = self.text[:-1]
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, BLACK)

    def update(self):
        # Resize the box if the text is too long.
        width = max(150, 100)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.txt_surface, (self.rect.x+50, self.rect.y+10))

    def getResult(self):
        return self.result
        # Blit the rect.
