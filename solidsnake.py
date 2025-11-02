import pygame
import sys
import random

pygame.init()
szelesseg = 800
magassag = 600
screen = pygame.display.set_mode((szelesseg, magassag))
pygame.display.set_caption("Solid Snake")

icon = pygame.image.load("solidsnake.png")
pygame.display.set_icon(icon)

def inditas_kiiratas(szokoz):
    inditas = betutipus.render("Nyomd meg a SPACE-t a kezdéshez.", True, (255, 255, 255))

    if szokoz == True:
        screen.blit(inditas, (1000,1000)) 
    else:
        screen.blit(inditas, (180,100))


betutipus = pygame.font.SysFont(None, 35)

def pontszam_kiir(pont):
    szoveg = betutipus.render("Pontszám: " + str(pont), True, (255, 255, 255))
    screen.blit(szoveg, (10, 10))

pontszam = 0

kigyo_meret = 10
kigyo_sebesseg = 15

x_kigyo, y_kigyo = szelesseg // 2, magassag // 2
x_valt, y_valt = 0, 0

kigyo_lista = []
kigyo_hossza = 1

etel_x = round(random.randrange(0, szelesseg - kigyo_meret) / 10.0) * 10.0
etel_y = round(random.randrange(0, magassag - kigyo_meret) / 10.0) * 10.0

szokoz_lenyomva = False

ora = pygame.time.Clock()
running = True
while running:
    for esemeny in pygame.event.get():
        if esemeny.type == pygame.QUIT:
            running = False

        if esemeny.type == pygame.KEYDOWN:
            if esemeny.key == pygame.K_SPACE:
                szokoz_lenyomva = True

            if esemeny.type == pygame.KEYDOWN and szokoz_lenyomva == True:
                if esemeny.key == pygame.K_LEFT:
                    x_valt = -kigyo_meret
                    y_valt = 0
                elif esemeny.key == pygame.K_RIGHT:
                    x_valt = kigyo_meret
                    y_valt = 0
                elif esemeny.key == pygame.K_UP:
                    y_valt = -kigyo_meret
                    x_valt = 0
                elif esemeny.key == pygame.K_DOWN:
                    y_valt = kigyo_meret
                    x_valt = 0


    x_kigyo += x_valt
    y_kigyo += y_valt

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), [etel_x, etel_y, kigyo_meret, kigyo_meret])
   
    kigyo_fej = [x_kigyo, y_kigyo]
    kigyo_lista.append(kigyo_fej)

    if len(kigyo_lista) > kigyo_hossza:
        del kigyo_lista[0]

    
    for elem in kigyo_lista:
        pygame.draw.rect(screen, (0, 255, 0), [elem[0], elem[1], kigyo_meret, kigyo_meret])

    
    if x_kigyo == etel_x and y_kigyo == etel_y:
        etel_x = round(random.randrange(0, szelesseg - kigyo_meret) / 10.0) * 10.0
        etel_y = round(random.randrange(0, magassag - kigyo_meret) / 10.0) * 10.0
        kigyo_hossza += 1
        pontszam += 1
    
    if x_kigyo < 0 or x_kigyo >= szelesseg or y_kigyo < 0 or y_kigyo >= magassag:
        running = False
    
    for elem in kigyo_lista[:-1]:
        if elem == kigyo_fej:
            running = False


    inditas_kiiratas(szokoz_lenyomva)
    pontszam_kiir(pontszam)
    pygame.display.update()
    ora.tick(kigyo_sebesseg)

pygame.quit()
