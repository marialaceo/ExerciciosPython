import pygame
pygame.init()
pygame.mixer.music.load('roar.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()