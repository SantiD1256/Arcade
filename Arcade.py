import pygame
#Primero, necesitamos declarar dos variables: el shift de fondo y la velocidad de fondo actual.
#shift de fondo
shift = 0
#velocidad de fondo actual
speed = 0
background_picture = "imagen.jpg"
win_width = 800
win_height = 500
window = (win_width,win_height)
# límites que el personaje no puede superar (el fondo empieza a irse)
left_bound = win_width / 40
right_bound = win_width - 8 * left_bound
#Procesamiento de evento
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    #flecha presionada
    if event.type == pygame.KEYDOWN:
        shift += speed
        local_shift = shift % win_width
        # Dibujar el fondo a la derecha del shift
        window.blit(background_picture, (local_shift, 0))
        # Dibujar el fondo a la izquierda del shift
        if local_shift != 0:
            window.blit(background_picture, (local_shift - win_width, 0))
        if event.key == pygame.K_LEFT:
            speed = -5
        elif event.key == pygame.K_RIGHT:
            speed = 5
    #flecha liberada
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            speed = 0
        elif event.key == pygame.K_RIGHT:
            speed = 0
        
