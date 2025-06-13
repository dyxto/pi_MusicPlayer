'''
https://www.geeksforgeeks.org/how-to-play-random-mp3-from-a-folder-in-python/
https://www.pygame.org/docs/ref/music.html
'''
import os
import random
import pygame
import time

pygame.mixer.init()
folder_path = '/home/kali/Music'

mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]
print(mp3_files)

# pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.load(random.choice(mp3_files))
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick()
    time.sleep(1)
    pygame.mixer.music.queue(random.choice(mp3_files))