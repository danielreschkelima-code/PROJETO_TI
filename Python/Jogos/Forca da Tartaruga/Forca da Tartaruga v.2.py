# Forca da Tartaruga v.2 (pygame ao invés de turtle)
#import gemini
import pygame
pygame.init()

x = 1920
y = 1080
fps = 60
tela = pygame.display.set_mode((x,y))
pygame.time.Clock()
rodando = True

while rodando:
    pygame.time.Clock().tick(fps)
    tela.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                rodando = False
            if event.key == pygame.K_SPACE:
                print ('sucesso')
                a = 10
                pygame.draw.rect(tela,(a,a,a), pygame.Rect(a,a,a,a), a) 

                a +=10

    pygame.display.flip()
    
pygame.quit()