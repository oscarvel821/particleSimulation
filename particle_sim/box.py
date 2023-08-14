import pygame

class Box:

    def __init__(self, x, y, x_offset, y_offset, width, height, thickness, color) -> None:
        self.x = x
        self.y = y
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.width = width
        self.height = height
        self.thickness = thickness
        self.color = color

    def draw(self, win) -> None:
        pygame.draw.rect(win, self.color, (self.x + self.x_offset, self.y + self.y_offset, self.width, self.height), self.thickness)

    def topLeft(self) -> tuple:
        return (self.x + self.x_offset, self.y + self.y_offset)
    
    def topRight(self) -> tuple:
        return (self.width, self.y + self.y_offset)
    
    def bottomLeft(self) -> tuple:
        return (self.x + self.x_offset, self.height)
    
    def bottomRight(self) -> tuple:
        return (self.width, self.height)
    
    def left(self) -> int:
        return self.x + self.x_offset
    
    def top(self) -> int:
        return self.y + self.y_offset
    
    def right(self) -> int:
        return self.width + self.x_offset
    
    def bottom(self) -> int:
        return self.height + self.y_offset