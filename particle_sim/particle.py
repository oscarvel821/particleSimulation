import pygame
from math import pi, sqrt
from random import random
from vector import addVector, getComponents, compToVector, addVectorWithScaler, dotProduct
from circle import Circle

class Particle(Circle):
    def __init__(self, x, y, radius, mass, thickness, color) -> None:
        super().__init__(x, y, radius, thickness, color)
        self.mass = mass # mass cannot be zero
        self.velocity = [60,random() * (2 * pi)]
        self.acc = [30, pi/2]

    def update(self, fps) -> None:
        delta_t = 1/fps

        x_comp, y_comp = getComponents(self.velocity)

        self.x, self.y = self.x + x_comp * delta_t, self.y + y_comp * delta_t
        
        # self.velocity = addVectorWithScaler(self.velocity, self.acc, delta_t)

    def checkBorderCollision(self, box) -> None:
        if (self.x - self.radius) < box.left():
            x, y = getComponents(self.velocity)

            self.velocity = compToVector(x * -1, y)
        elif (self.y - self.radius) < box.top():
            x, y = getComponents(self.velocity)

            self.velocity = compToVector(x, y * -1)
        elif (self.x + self.radius) > box.right():
            x, y = getComponents(self.velocity)

            self.velocity = compToVector(x * -1, y)
        elif (self.y + self.radius) > box.bottom():
            x, y = getComponents(self.velocity)

            self.velocity = compToVector(x, y * -1)

    def particleCollision(self, other) -> None:
        if self.particleDetection(other):
            self.static_resolution(other)
            self.particleResponse(other)

    def particleDetection(self, other) -> bool:
        distance = (self.x - other.x) ** 2 + (self.y - other.y) ** 2

        if abs(distance) <= (self.radius + other.radius) ** 2:
            return True
        
        return False
    
    def static_resolution(self, other) -> None:
        distance = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

        overlap = (distance - self.radius - other.radius) * 0.5

        #unit normal vector
        unit_normal = [(other.x - self.x) / distance, (other.y - self.y) / distance]

        self.x -= overlap * unit_normal[0]
        self.y -= overlap * unit_normal[1]

        self.x += overlap * unit_normal[0]
        self.y += overlap * unit_normal[1]


    def particleResponse(self, other) -> None:
        #initial velocities
        v1 = getComponents(self.velocity)
        v2 = getComponents(other.velocity)

        #unit normal and unit tangent vectors
        normal = [other.x - self.x, other.y - self.y]
        unit_normal = [normal[0] / (sqrt(normal[0]** 2 + normal[1] ** 2)), normal[1] / (sqrt(normal[0]** 2 + normal[1] ** 2))]

        unit_tangent = [-unit_normal[1], unit_normal[0]]

        #scalers
        v1n = dotProduct(unit_normal, v1)
        v1t = dotProduct(unit_tangent, v1)
        v2n = dotProduct(unit_normal, v2)
        v2t = dotProduct(unit_tangent, v2)

        #use one-dimensional collision formuals
        new_v1n = (v1n * (self.mass - other.mass) + (2 * other.mass * v2n)) / (self.mass + other.mass)
        new_v2n = (v2n * (other.mass - self.mass) + (2 * self.mass * v1n)) / (self.mass + other.mass)

        #convert back to vectors
        new_v1n = [unit_normal[0] * new_v1n, unit_normal[1] * new_v1n]
        new_v1t = [unit_tangent[0] * v1t, unit_tangent[1] * v1t]

        new_v2n = [unit_normal[0] * new_v2n, unit_normal[1] * new_v2n]
        new_v2t = [unit_tangent[0] * v2t, unit_tangent[1] * v2t]

        #convert back to polar coordinates
        self.velocity = compToVector((new_v1n[0] + new_v1t[0]), (new_v1n[1] + new_v1t[1]))
        other.velocity = compToVector((new_v2n[0] + new_v2t[0]), (new_v2n[1] + new_v2t[1]))











    