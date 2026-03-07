#abrir e reproduzir um áudo de arquivo MP3 (com módulos)
#só vai funcionar se o mp3 estiver na pasta do código
#dá para colar crtl C + ctrl V direto no Pycharm
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('Pressione ENTER para sair...')
