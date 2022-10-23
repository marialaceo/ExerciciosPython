import pygame
resposta=str(input('Deseja escutar Roar - Katy Perry? '))
if (resposta=='sim'):
    pygame.init()
    pygame.mixer.music.load('roar.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else:
    print('Que pena :(')