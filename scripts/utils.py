import pygame

BASE_IMAGE_PATH = 'data/images/'

# Load an image
def load_img(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey('black')
    return img