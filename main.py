import pygame

print("Starting...")
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print("Setup End")

#loop para manter a janela aberta e fecha-la.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
