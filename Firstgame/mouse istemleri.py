import pygame

from resim import canavar_koordinat

pygame.init()
GENISLIK,YUKSEKLIK=500,500
pencere=pygame.display.set_mode((GENISLIK,YUKSEKLIK))

canavar=pygame.image.load("canavar2.png")
canavar_koordinat=canavar.get_rect()
canavar_koordinat.topleft=(150,150)



durum=True
while durum:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            durum=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x_degeri=event.pos[0]

            mouse_y_degeri = event.pos[1]
            print("X ekseni:",mouse_x_degeri, " " "Y ekseni:",mouse_y_degeri)
pencere.fill((0,0,0))
pencere.blit(canavar,canavar_koordinat)
pygame.display.update()


pygame.quit()