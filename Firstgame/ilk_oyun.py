import pygame,random

from ilkpencere import pencere
from resim import canavar_koordinat, canavar

#Paketlerimizi başlattık
pygame.init()
#Penceremizi Oluşturma
GENISLIK,YUKSEKLIK=643,360
pencere=pygame.display.set_mode((GENISLIK,YUKSEKLIK))

#Arka plan şarkılarının ve ses efeklerinin eklenmesi
pygame.mixer.music.load("oyun_arka_plan.wav")
pygame.mixer.music.play(-1,0.0)
seviye_yukselme_sesi=pygame.mixer.Sound("level_up.wav")
yem_yem_sesi=pygame.mixer.Sound("jump.wav")


#FPS ayarlama
HIZ=10
saat=pygame.time.Clock()
FPS=27

#Karakter ve yem tanımlama
canacar=pygame.image.load("asıl_foto1.png")
canavar_koordinat=canavar.get_rect()
canavar_koordinat.topleft=(GENISLIK/2,YUKSEKLIK/2)


yem=pygame.image.load("cent1.png")
yem_koordinat=yem.get_rect()
yem_koordinat.topleft=(150,150)

arka_plan=pygame.image.load("asıl_background.jpg")

#Font ayarlaması
FONT=pygame.font.SysFont("consolas",64)

#Skor
SKOR=0
#Oyun döngüsü
durum=True
while durum:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            durum=False
    pencere.blit(arka_plan,(0,0))
    pencere.blit(canavar,canavar_koordinat)
    pencere.blit(yem,yem_koordinat)
    YAZI=FONT.render("Skor:"+str(SKOR),True,(255,0,0),(0,0,255))
    YAZI_KOORDİNAT=YAZI.get_rect()
    YAZI_KOORDİNAT.topleft=(20,20)
    pygame.draw.line(pencere,(255,0,255),(0,90),(643,90),3)
    pencere.blit(YAZI,YAZI_KOORDİNAT)
    tus=pygame.key.get_pressed()
    if tus[pygame.K_LEFT] and canavar_koordinat.left>0:
        canavar_koordinat.x-=HIZ
    elif tus[pygame.K_RIGHT] and canavar_koordinat.right<GENISLIK:
        canavar_koordinat.x+=HIZ
    elif tus[pygame.K_UP] and canavar_koordinat.top>0:
        canavar_koordinat.y-=HIZ
    elif tus[pygame.K_DOWN] and canavar_koordinat.bottom<YUKSEKLIK:
        canavar_koordinat.y+=HIZ
    if canavar_koordinat.colliderect(yem_koordinat):
        yem_yem_sesi.play()
        yem_koordinat.x=random.randint(0,GENISLIK-32)
        yem_koordinat.y=random.randint(91,YUKSEKLIK-32)
        SKOR=SKOR+1
    if SKOR>6:
        canavar=pygame.image.load("asıl_foto2.png")
        if tus[pygame.K_LEFT] and canavar_koordinat.left > 0:
            canavar_koordinat.x -= HIZ
        elif tus[pygame.K_RIGHT] and canavar_koordinat.right < GENISLIK:
            canavar_koordinat.x += HIZ
        elif tus[pygame.K_UP] and canavar_koordinat.top > 0:
            canavar_koordinat.y -= HIZ
        elif tus[pygame.K_DOWN] and canavar_koordinat.bottom < YUKSEKLIK:
            canavar_koordinat.y += HIZ
        if canavar_koordinat.colliderect(yem_koordinat):
            yem_yem_sesi.play()
            yem_koordinat.x = random.randint(0, GENISLIK - 32)
            yem_koordinat.y = random.randint(91, YUKSEKLIK - 32)
            SKOR = SKOR + 1


    pygame.display.update()
    saat.tick(FPS)


