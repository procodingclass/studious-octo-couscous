import pygame
import ctypes

screen_width = 700
screen_height = 400

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))

def create_screen():
    global screen
    return screen

def loadImages(images_path):
    image_list = []

    for path in images_path:
        loaded_image = pygame.image.load(path).convert_alpha()
        image_list.append(loaded_image)
    return image_list

def scaleImages(image_list, width, height):
    scaled_images = []
    if(len(image_list) == 1):
        return pygame.transform.scale(image_list[0], (width, height))

    for img in image_list:
        image = pygame.transform.scale(img, (width, height))
        scaled_images.append(image)

    return scaled_images

#Images
color_surf = loadImages(["assets/color_bg.jpg"])
background_surf = loadImages(["assets/environment.png"])

ground_surf = loadImages(["assets/ground.png"])
door_surf = loadImages(["assets/doorOpen.png"])
win_surf = loadImages(["assets/win.png"])


#player_surf = loadImages(["assets/joe1.png"])
cloud_surf = loadImages(["assets/cloud.png"])
cloud_surf[0].set_alpha(200)

doorHeight=100
doorWidth=100

#Image Scaling
background_surf = scaleImages(background_surf, screen_width, 700)

color_surf = scaleImages(color_surf, screen_width, 400)
door_surf= scaleImages(door_surf, 100,100)
cloud_surf = scaleImages(cloud_surf, 100, 50)
#player_surf = scaleImages(player_surf, 40, 63)
ground_surf = scaleImages(ground_surf, screen_width, 90)


# sprites
#player_rect = pygame.Rect(620,screen_height-145,40,63)
ground_rect = pygame.Rect(0,screen_height- 88,screen_width,40)
door_rect = pygame.Rect(screen_width-130, screen_height-190, 100,100)



cloud1X = 50
cloud2X = 300
cloud3X = 550



def draw_arena():
    global color_surf, background_surf
    global ground_surf, door_surf, win_surf
    global cloud_surf, ground_rect, door_rect
    global cloud1X, cloud2X, cloud3X
    global screen

    screen.blit(color_surf, (0, 0))
    screen.blit(background_surf, (0, 0))
    screen.blit(ground_surf, (0, screen_height-90))
    screen.blit(door_surf,door_rect)



    screen.blit(cloud_surf, (cloud1X, 30))
    if cloud1X < -100:
        cloud1X = screen_width
    else:
        cloud1X -= 2

    screen.blit(cloud_surf, (cloud2X, 55))
    if cloud2X < -50:
        cloud2X = screen_width
    else:
        cloud2X -= 1

    screen.blit(cloud_surf, (cloud3X, 20))
    if cloud3X < 0:
        cloud3X = screen_width
    else:
        cloud3X -= 2


    clock.tick(30)


def key_down(event):
    global player_vel_x, player_vel_y, player_animation_counter

    if(event.type == pygame.KEYDOWN):
        if(event.key == pygame.K_RIGHT):
            player_vel_x = 5
            player_animation_counter +=1

        elif(event.key == pygame.K_LEFT):
            player_vel_x = -5
            player_animation_counter +=1

        elif(event.key == pygame.K_SPACE):
            player_vel_y = -15


def key_up(event):
    global player_vel_x
    if(event.type == pygame.KEYUP):
        if(event.key == pygame.K_RIGHT):
            player_vel_x = 0
        elif(event.key == pygame.K_LEFT):
            player_vel_x = 0



def check_collision(static_rect, moving_rect, vel_x, vel_y):
    # x- direction
    moving_rect_props = (moving_rect.x + vel_x, moving_rect.y, moving_rect.width, moving_rect.height)
    if static_rect.colliderect(moving_rect_props):
            vel_x = 0

            #check for collision in y direction
            moving_rect_props = (moving_rect.x, moving_rect.y + vel_y, moving_rect.width, moving_rect.height)
            if static_rect.colliderect(moving_rect_props):
                #check if below the platform i.e. jumping
                if(vel_y < 0):
                    vel_y = static_rect.bottom - moving_rect.top
                elif(vel_y > 0): #check if above the platform i.e. falling
                    vel_y = static_rect.top - moving_rect.bottom

    # make player to stand on platform
    # y- direction
    static_rect_props = (static_rect.x, static_rect.y - vel_y, static_rect.width, static_rect.height)
    if(moving_rect.colliderect(static_rect_props)):
        vel_y = 0
    return vel_x, vel_y




def gameplay():
    global door_surf, win_surf
    global ground_rect, screen

    draw_arena()
    try:
        import main

        if(main.player_rect != None and main.player_surf != None):
            if(main.player_rect.colliderect(door_rect)):
                screen.blit(win_surf[0],(screen_width / 2 - 140,100))



    except:
        pass
