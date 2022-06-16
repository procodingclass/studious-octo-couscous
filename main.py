import pygame, sys, random
from game import create_screen, screen_height, gameplay


screen = create_screen()
# Load image frames
player_surf = pygame.image.load("assets/joe/0.png").convert_alpha()

# scale image frames
player_surf = pygame.transform.scale(player_surf, (30, 43))

# Player Rectangle
player_rect = pygame.Rect(610, screen_height - 130 ,30,43) # x, y, width, height


while True:


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()



    gameplay()



    screen.blit(player_surf,player_rect)

    pygame.display.update()
