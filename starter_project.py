import pygame, sys, time

#===================
# classes definition
#===================


#Pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

# group setup
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group

last_time = time.time()
while True:
    #delta time
    dt = time.time() - last_time
    last_time=time.time()

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    pygame.display.update()
