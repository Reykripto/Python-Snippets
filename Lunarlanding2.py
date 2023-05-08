# Lunar Landing game By E.Rey

import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Crear la ventana del juego
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Establecer el título de la ventana
pygame.display.set_caption("Aterrizaje lunar")

# Definir los colores que se van a utilizar en el juego
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
YELLOW = (255, 255, 0)

# Definir la fuente que se va a utilizar para el texto
font = pygame.font.Font(None, 36)

# Definir la posición y velocidad del módulo lunar
module_x = random.randint(0, WINDOW_WIDTH - 45)
module_y = 0
module_speed_x = 0
module_speed_y = 0

# Definir la posición y velocidad del paisaje lunar
landscape_x = random.randint(-WINDOW_WIDTH, 0)
landscape_y = WINDOW_HEIGHT - 40
landscape_speed_x = -1

# Generar las plataformas de aterrizaje aleatoriamente
platforms = []
for i in range(5):
    platform_x = random.randint(0, WINDOW_WIDTH - 100)
    platform_y = WINDOW_HEIGHT - 100
    platform = pygame.Rect(platform_x, platform_y, 100, 20)
    platforms.append(platform)

# Definir una variable para controlar el bucle principal del juego
game_over = False

# Crear un reloj para controlar la velocidad de fotogramas del juego
clock = pygame.time.Clock()

# Bucle principal del juego
while not game_over:
    # Manejar los eventos de teclado y ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Dibujar el fondo del juego
    screen.fill(BLACK)
# Dibujar el paisaje lunar
pygame.draw.rect(screen, GRAY, (landscape_x, landscape_y, WINDOW_WIDTH * 2, 40))
# Actualizar la posición del paisaje lunar
landscape_x += landscape_speed_x
if landscape_x <= -WINDOW_WIDTH:
    landscape_x = 0
# Dibujar las plataformas de aterrizaje
for platform in platforms:
    pygame.draw.rect(screen, WHITE, platform)
# Dibujar el módulo lunar
pygame.draw.rect(screen, YELLOW, (module_x, module_y, 45, 45))
# Actualizar la posición del módulo lunar
module_x += module_speed_x
module_y += module_speed_y
# Aplicar gravedad al módulo lunar
module_speed_y += 0.1
# Comprobar si el módulo lunar ha colisionado con el paisaje lunar
if module_y + 45 > landscape_y:
        game_over = True
    # Mostrar mensaje de "Has perdido" y esperar a que el usuario cierre la ventana
        text = font.render("Has perdido", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)  # Esperar 2 segundos
        game_over = True
# Comprobar si el módulo lunar ha aterrizado en una plataforma 
for platform in platforms:
    if module_y + 45 > platform.top and module_y + 45 < platform.top + 10 and module_x + 45 > platform.left and module_x < platform.left + 100:
        # Mostrar mensaje de "Has ganado" y esperar a que el usuario cierre la ventana
        text = font.render("¡Has ganado!", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)
        game_over = True

pygame.display.update()
clock.tick(60)