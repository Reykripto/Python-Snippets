# Lunar landing
import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Crear la ventana del juego
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Definir los colores que se usarán
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Definir la gravedad de la luna
GRAVITY = 0.1

# Definir la posición inicial del módulo lunar
module_x = WINDOW_WIDTH / 2
module_y = 0

# Definir la velocidad inicial del módulo lunar
module_vx = 0
module_vy = 0

# Definir la aceleración del módulo lunar
module_ax = 0
module_ay = GRAVITY

# Definir la velocidad de desplazamiento del módulo lunar
MODULE_SPEED = 5

# Definir la altura máxima a la que puede elevarse el módulo lunar
MAX_HEIGHT = 300

# Definir la posición y el ancho de las plataformas de aterrizaje
PLATFORM_Y = WINDOW_HEIGHT - 50
PLATFORM_WIDTH = 50

# Definir una lista vacía para almacenar las plataformas de aterrizaje
platforms = []

# Generar las plataformas de aterrizaje de forma aleatoria
for i in range(10):
    platform_x = random.randint(0, WINDOW_WIDTH - PLATFORM_WIDTH)
    platforms.append(pygame.Rect(platform_x, PLATFORM_Y, PLATFORM_WIDTH, 5))

# Crear el bucle principal del juego
clock = pygame.time.Clock()
game_over = False
while not game_over:

    # Manejar eventos de teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                module_ay = -GRAVITY
            elif event.key == pygame.K_LEFT:
                module_ax = -MODULE_SPEED
            elif event.key == pygame.K_RIGHT:
                module_ax = MODULE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                module_ay = GRAVITY
            elif event.key == pygame.K_LEFT:
                module_ax = 0
            elif event.key == pygame.K_RIGHT:
                module_ax = 0

    # Actualizar la posición del módulo lunar
    module_x += module_vx
    module_y += module_vy
    module_vx += module_ax
    module_vy += module_ay

    # Limitar la velocidad vertical del módulo lunar
    module_vy = min(module_vy, GRAVITY * MAX_HEIGHT)

    # Dibujar el fondo negro
    screen.fill(BLACK)

    # Dibujar el paisaje lunar
    for i in range(50):
        x = random.randint(0, WINDOW_WIDTH)
        y = random.randint(0, WINDOW_HEIGHT - 50)
        pygame.draw.rect(screen, WHITE, (x, y, 2, 10))

    # Dibujar las plataformas de aterrizaje
    for platform in platforms:
        pygame.draw.rect(screen, YELLOW, platform)
    # Dibujar el módulo lunar
module_rect = pygame.Rect(module_x, module_y, 45, 45)
pygame.draw.rect(screen, WHITE, module_rect)

# Actualizar la pantalla
pygame.display.update()

# Verificar si el módulo lunar ha aterrizado en una plataforma
for platform in platforms:
    if module_rect.colliderect(platform):
        game_over = True
        print("¡Aterrizaje exitoso!")

# Verificar si el módulo lunar ha chocado contra el suelo
if module_y >= WINDOW_HEIGHT - 45:
    game_over = True
    print("¡Aterrizaje fallido!")

# Limitar la velocidad de fotogramas del juego
clock.tick(60)
pygame.quit()


# Este código utiliza la biblioteca Pygame 
# para crear la ventana del juego y 
# manejar los eventos de teclado. El paisaje lunar y 
# las plataformas de aterrizaje se generan de forma aleatoria 
# utilizando la función `random.randint()`, 
# y se dibujan en la ventana utilizando 
# la función `pygame.draw.rect()`. 
# El módulo lunar se dibuja como un rectángulo blanco de 45x45 píxeles, 
# y su posición y velocidad se actualizan en cada fotograma del juego. 
# Las teclas de flecha izquierda y derecha se utilizan para mover el módulo lunar horizontalmente, 
# y la tecla de flecha arriba se utiliza para elevar el módulo lunar. 
# Cuando el módulo lunar aterriza en una plataforma o choca contra el suelo, 
# el juego termina y se muestra un mensaje en la consola.