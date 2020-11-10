import pygame
from pygame.draw import *

pygame.init()

FPS = 60
screen = pygame.display.set_mode((600, 800))

rect(screen, (102, 102, 102), (0, 0, 800, 350))
rect(screen, (0, 0, 0), (0, 350, 800, 250))
#луна
circle(screen, (230, 230, 230), (560, 40), 40)
#облака
ellipse(screen, (26, 26, 26), (300, 150, 300, 50))
ellipse(screen, (77, 77, 77), (260, 30, 300, 50))
ellipse(screen, (57, 57, 57), (50, 80, 450, 50))
#дом
polygon(screen, (40, 34, 10), [(25,100), (330,100), (330,550), (25,550)])
polygon(screen, (0, 0, 0), [(30,90), (325,90), (350,130), (0,130)])
polygon(screen, (26, 26, 26), [(60,60), (70,60), (70,110), (60,110)])
polygon(screen, (26, 26, 26), [(310,50), (320,50), (320,110), (310,110)])
#окна
polygon(screen, (72, 61, 55), [(50,130), (90,130), (90,352), (50,352)])
polygon(screen, (72, 61, 55), [(130,130), (170,130), (170,352), (130,352)])
polygon(screen, (72, 61, 55), [(210,130), (250,130), (250,352), (210,352)])
polygon(screen, (72, 61, 55), [(290,130), (320,130), (320,352), (290,352)])
#балкон
polygon(screen, (26, 26, 26), [(0,350), (350,350), (350,380), (0,380)])
polygon(screen, (26, 26, 26), [(15,300), (340,300), (340,315), (15,315)])
polygon(screen, (26, 26, 26), [(5,315), (15,315), (15,350), (5,350)])
polygon(screen, (26, 26, 26), [(130,315), (140,315), (140,350), (130,350)])
polygon(screen, (26, 26, 26), [(190,315), (200,315), (200,350), (190,350)])
polygon(screen, (26, 26, 26), [(340,315), (350,315), (350,350), (340,350)])
#окна
polygon(screen, (43, 17, 0), [(55,400), (115,400), (115,460), (55,460)])
polygon(screen, (43, 17, 0), [(130,400), (190,400), (190,460), (130,460)])
polygon(screen, (212, 170, 0), [(205,400), (265,400), (265,460), (205,460)])
#призрак
circle(screen, (179, 179, 179), (500, 600), 20)
circle(screen, (133, 204, 223), (490, 600), 5)
circle(screen, (133, 204, 223), (505, 600), 5)
circle(screen, (0, 0, 0), (488, 600), 2)
circle(screen, (0, 0, 0), (503, 600), 2)
polygon(screen, (179, 179, 179), [(520,595), (580,680), (420,700), (485,608)])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
