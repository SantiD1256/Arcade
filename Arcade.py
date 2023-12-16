from pygame import *
#Primero, necesitamos declarar dos variables: el shift de fondo y la velocidad de fondo actual.
#shift de fondo
shift = 0
#velocidad de fondo actual
speed = 0
class Jugador():
    def __init__(self, player_image, player_x, player_y, speed, height, width):
        sprite.Sprite.__init__(self)
    def update (self):
        #primer movimiento horizontal
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            # iterar sobre todos los objetos con los que el personaje ha colisionado
            for p in platforms_touched:
                # establecer el borde derecho del personaje en el borde izquierdo de la plataforma más a la izquierda
                self.rect.right = min(self.rect.right, p.rect.left)
    def gravitate(self):
        self.y_speed += 0.25
    
background_picture = "imagen.jpg"
win_width = 800
win_height = 500
# límites que el personaje no puede superar (el fondo empieza a irse)
left_bound = win_width / 40
right_bound = win_width - 8 * left_bound

window = (win_width,win_height)
finished = False
run = True

while run:
    #Procesamiento de evento
    for e in event.get():
        if e.type == QUIT:
            run = False
        #flecha presionada
        if e.type == KEYDOWN:
            shift += speed
            local_shift = shift % win_width
            # Dibujar el fondo a la derecha del shift
            window.blit(background_picture, (local_shift, 0))
            # Dibujar el fondo a la izquierda del shift
            if local_shift != 0:
                window.blit(background_picture, (local_shift - win_width, 0))
            if e.key == K_LEFT:
                speed = -5
            elif e.key == K_RIGHT:
                speed = 5
        #flecha liberada
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                speed = 0
            elif e.key == K_RIGHT:
                speed = 0

    if not finished:
        # comprobación de los límites de la pantalla:
        if robin.rect.x > right_bound and robin.x_speed > 0 or robin.rect.x < left_bound and robin.x_speed < 0:
            # al salir a la izquierda o derecha, el cambio es transferido al shift de la pantalla
            shift -= robin.x_speed
            # shift general para todos los objetos
            for s in all_sprites:
                s.rect.x -= robin.x_speed # el jugador también está en esta lista, así que su movimiento será cancelado visualmente
    display.update
    
