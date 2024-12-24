import pygame

pygame. init()

pencere=pygame.display.set_mode((640,480))
canavar=pygame.image.load("asıl_foto1.png")
canavar_koordinat=canavar.get_rect()
canavar_koordinat.topleft=(10,10)





durum=True
while durum:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            durum=False
    pencere.blit(canavar,canavar_koordinat)
    pygame.display.update()

pygame.quit()