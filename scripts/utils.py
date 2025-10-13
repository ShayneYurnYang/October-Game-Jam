import pygame

BASE_IMAGE_PATH = 'data/images/'

def load_img(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey('black')
    return img