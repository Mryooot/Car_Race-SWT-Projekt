import pygame
import sys
from car import Car  # Importiere die Car-Klasse

# Initialisierung
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 1290, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Race - SWT Projekt")

# Clock für FPS
clock = pygame.time.Clock()

# Auto erstellen
car = Car(WIDTH // 2, HEIGHT // 2)

# Hauptloop
running = True
while running:
    # Event-Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    car.update(keys)

    # Hintergrundfarbe
    screen.fill((30, 30, 30))  # dunkelgrau

    # Auto zeichnen
    car.draw(screen)

    # Anzeige aktualisieren
    pygame.display.flip()

    # Max. 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()
