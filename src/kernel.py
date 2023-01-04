import pygame
from utils.contents import colors
pygame.init()
window = pygame.display.set_mode((600,600))
window.fill(colors.WHITE)
mouse = []
image = pygame.image.load("./terra.png").convert()
image = pygame.transform.scale(image,(20,20))
def main():
    global mouse,window,image
    while colors.running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            colors.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            colors.drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            colors.drawing = False
        mouse = pygame.mouse.get_pos()
        if colors.drawing:
            window.blit(image,mouse)
            window.set_at(mouse,colors.BLACK)
        pygame.display.update()
main()
pygame.quit()
