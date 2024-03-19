import pygame

pygame.init()
screen = pygame.display.set_mode((670, 373))
clock = pygame.time.Clock()
FPS = 60
fon = pygame.image.load('image/fons/fon1.jpg').convert()
player = pygame.image.load('image/player/walk/1.png').convert_alpha()
walk_r = [
    pygame.image.load('image/player/walk/1.png').convert_alpha(),
    pygame.image.load('image/player/walk/2.png').convert_alpha(),
    pygame.image.load('image/player/walk/3.png').convert_alpha(),
    pygame.image.load('image/player/walk/4.png').convert_alpha(),
    pygame.image.load('image/player/walk/5.png').convert_alpha(),
    pygame.image.load('image/player/walk/6.png').convert_alpha(),
    pygame.image.load('image/player/walk/7.png').convert_alpha(),
]
player_aim_count = 0
fon_x = 0
player_speed = 5
player_x = 10
player_y = 200
dog = [
    pygame.image.load('image/dog/1.png').convert_alpha(),
    pygame.image.load('image/dog/2.png').convert_alpha(),
    pygame.image.load('image/dog/3.png').convert_alpha(),
    pygame.image.load('image/dog/4.png').convert_alpha(),
    pygame.image.load('image/dog/5.png').convert_alpha(),
]
dog_aim_count = 0
dog_list = []
is_jump = False
jump_count = 8
dog_timer = pygame.USEREVENT + 1
pygame.time.set_timer(dog_timer, 2500)

label = pygame.font.Font('font/Klyakson.otf', 40)
lose_label = label.render('Вы проиграли!', True, (193, 196, 199))

gameplay = True

flag = True
while flag:
    screen.blit(fon, (fon_x, 0))
    screen.blit(fon, (fon_x + 1380, 0))
    screen.blit(walk_r[player_aim_count], (player_x, player_y))

    if gameplay:

        player_rect = walk_r[0].get_rect(topleft=(player_x, player_y))
        if dog_list:
            for (i, el) in enumerate(dog_list):
                screen.blit(dog[dog_aim_count], el)
                el.x -= 10

                if el.x < -10:
                    dog_list.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False
        keys = pygame.key.get_pressed()
        if player_aim_count == 6:
            player_aim_count = 0
        else:
            player_aim_count += 1
        if dog_aim_count == 4:
            dog_aim_count = 0
        else:
            dog_aim_count += 1
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 8
        fon_x -= 20
        if fon_x == -1380:
            fon_x = 0
    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (180, 100))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flag = False
        if event.type == dog_timer:
            dog_list.append(dog[0].get_rect(topleft=(680, 280)))
    clock.tick(20)
