import pygame


pygame.init()

pencere=pygame.display.set_mode((800,680))

font_listesi=pygame.font.get_fonts()
for font in font_listesi:
    print(font)
font_ismi=pygame.font.SysFont("consolas",64)

yazı=font_ismi.render("Hello world",True,(255,0,0))
yazı_koordinat=yazı.get_rect()
yazı_koordinat.topleft=(150,150)

durum=True
while durum:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            durum=False
    pencere.blit(yazı,yazı_koordinat)
    pygame.display.update()


pygame.quit()