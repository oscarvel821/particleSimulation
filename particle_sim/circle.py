import pygame

class Circle:

    def __init__(self, x, y, radius, thickness, color) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.thickness = thickness
        self.color = color

    def draw(self, win) -> None:
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius, self.thickness)