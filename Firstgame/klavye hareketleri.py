import pygame

from resim import canavar_koordinat

pygame.init()

GENISLIK=750
YUKSEKLIK=680
pencere=pygame.display.set_mode((GENISLIK,YUKSEKLIK))

HIZ=60
canavar=pygame.image.load('canavar2.png')
canavar_koordinat=canavar.get_rect()
canavar_koordinat.topleft=(GENISLIK/2,YUKSEKLIK/2)




durum=True
while durum:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            durum=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                canavar_koordinat.x-=HIZ
            elif event.key==pygame.K_UP:
                canavar_koordinat.y-=HIZ
            elif event.key==pygame.K_RIGHT:
                canavar_koordinat.x+=HIZ
            elif event.key==pygame.K_DOWN:
                canavar_koordinat.y+=HIZ
    pencere.fill((0,0,0))





    pencere.blit(canavar,canavar_koordinat)
    pygame.display.update()

pygame.quit()