# -*- coding: utf-8 -*-

import pygame
import time


path = "/Users/jayce/Desktop/1.mp3"
pygame.mixer.init()

track = pygame.mixer.music.load(path)

# 播放

pygame.mixer.music.play()

time.sleep(300)
pygame.mixer.music.stop()