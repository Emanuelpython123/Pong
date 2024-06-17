import pygame

pygame.init()

#Coordenadas p1
p1x = 45
p1y = 205
p1s = 0
p1w = 15
p1h = 90
#Coordenadas p2
p2x = 735
p2y = 205
p2s = 0
p2w = 15
p2h = 90
#Pelota
px = 400
py = 245
pr = 10
ps = 3
psy = 3
#Tabla de colores

BLACK					=			(  0,   0,   0)
BLUE					=			(  0,   0, 255)
GREEN					=			(  0, 255,   0)
RED						=			(255,   0,   0)
WHITE					=			(255, 255, 255)

size = (800, 500)
screen = pygame.display.set_mode(size)
lose = False

# Controlar FPS
clock = pygame.time.Clock()

while not lose:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lose = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                p2s = -5
            if event.key == pygame.K_l:
                p2s = 5
            if event.key == pygame.K_w:
                p1s = -5
            if event.key == pygame.K_s:
                p1s = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_o:
                p2s = 0
            if event.key == pygame.K_l:
                p2s = 0
            if event.key == pygame.K_w:
                p1s = 0
            if event.key == pygame.K_s:
                p1s = 0    
    if py > 500 or py < 0:
        psy *= -1
    if px > 800 or px < 0:
        px = 400
        py = 245
        ps *= -1
    px += ps
    py += psy
    p1y += p1s
    p2y += p2s
    screen.fill(BLACK)
    
    p1 = pygame.draw.rect(screen, BLUE, [p1x, p1y, p1w, p1h])
    p2 = pygame.draw.rect(screen, RED, [p2x, p2y, p2w, p2h])
    p = pygame.draw.circle(screen, WHITE, [px, py], pr)
    pygame.display.flip()
    clock.tick(80)
    if p.colliderect(p1) or p.colliderect(p2):
        ps *= -1
    if p1y > 500-90 or p1y < 0:
        p1s = 0
    if p2y > 500-90 or p2y < 0:
        p2s = 0
pygame.quit()