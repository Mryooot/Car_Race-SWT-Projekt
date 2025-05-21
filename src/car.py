import pygame
import math

class Car:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/car.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0
        self.speed = 0
        self.max_speed = 8
        self.acceleration = 0.3
        self.rotation_speed = 3

    def update(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            print("UP gedrückt")
            self.speed = min(self.speed + self.acceleration, self.max_speed)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            print("DOWN gedrückt")
            self.speed = max(self.speed - self.acceleration, -self.max_speed / 2)
        else:
            self.speed *= 0.98  # natürliche Verzögerung

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            print("LEFT gedrückt")
            self.angle += self.rotation_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            print("RIGHT gedrückt")
            self.angle -= self.rotation_speed

        # Bewegung berechnen
        rad = math.radians(self.angle)
        dx = -self.speed * math.sin(rad)
        dy = -self.speed * math.cos(rad)
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated.get_rect(center=self.rect.center)
        screen.blit(rotated, new_rect)
