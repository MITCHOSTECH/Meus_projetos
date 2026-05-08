import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.mixer.music.get_volume()
while pygame.mixer.music.get_busy():
    continue
