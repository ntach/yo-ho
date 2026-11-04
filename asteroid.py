import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20, 50)
            first_rotated_velocity = self.velocity.rotate(split_angle)
            second_rotated_velocity = -first_rotated_velocity
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            second_new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            first_new_asteroid.velocity = first_rotated_velocity * 1.2
            second_new_asteroid.velocity = second_rotated_velocity * 1.2
