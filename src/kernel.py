import pygame
from utils.contents import colors
from utils.contents import etc
from utils.etc import gui
pygame.init()
window = pygame.display.set_mode((600,600))
window.fill(colors.WHITE)
mouse = []
#this comment below are texture imports that in future versions I will add and OOP
#image = pygame.image.load("./terra.png").convert()
#image = pygame.transform.scale(image,(20,20))
Done = False
gui.init_gui()
def main():
    global mouse,window,image
    while etc.running:
        
        from utils.etc import texture
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            etc.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            etc.drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            etc.drawing = False
        mouse = pygame.mouse.get_pos()
        if etc.drawing:
            #window.blit(image,mouse)
            print(texture.RGB)
            window.set_at(mouse,texture.RGB)
        pygame.display.update()
main()
pygame.quit()
