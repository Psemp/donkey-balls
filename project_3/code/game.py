import pygame
from pathlib import Path
from map_init import board
from characters import mac, macpos, guard, guardpos
from items import needle, ether, container


def main():

    syringe_created = False
    game_over = False

    pygame.init

    win = pygame.display.set_mode((480, 512))

    run = True

    def get_path(file_name):
        return str(Path(__file__).parent.parent.joinpath("images", file_name))

    def get_image(file_name):
        return pygame.image.load(get_path(file_name)).convert()

    def get_image_alpha(file_name):
        return pygame.image.load(get_path(file_name)).convert_alpha()

    known_images = ['floor.png', 'wall.png']
    known_alpha_images = ['plyr.png', 'ether.png', 'needle.png', 'container.png', 'guard.png', 'syringe.png', 'victory.png', 'defeat.png']

    images = {}

    for known_image in known_images:
        loaded_image = get_image(known_image)
        images[known_image] = loaded_image

    for known_image in known_alpha_images:
        loaded_image = get_image_alpha(known_image)
        images[known_image] = loaded_image

    while run:

        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        Tuple_macpos = tuple(macpos)

        if mac.alive and guard.alive and macpos == guardpos and not syringe_created:
            mac.alive = False
            game_over = True
        if mac.alive and guard.alive and macpos == guardpos and syringe_created:
            guard.alive = False
            game_over = True
        if mac.alive and needle.gathered and ether.gathered and container.gathered:
            syringe_created = True
        if mac.alive and not needle.gathered and Tuple_macpos == needle.coordinates:
            needle.gathered = True
        if mac.alive and not ether.gathered and Tuple_macpos == ether.coordinates:
            ether.gathered = True
        if mac.alive and not container.gathered and Tuple_macpos == container.coordinates:
            container.gathered = True

    # DRAW

        win.fill((255, 255, 255))

        for i in range(0, len(board.floors)):
            win.blit(images["floor.png"], (board.floors[i]))

        for i in range(0, len(board.walls)):
            win.blit(images["wall.png"], (board.walls[i]))

        if not ether.gathered:
            win.blit(images["ether.png"], (ether.coordinates))
        else:
            win.blit(images["ether.png"], (0, 480))

        if not needle.gathered:
            win.blit(images["needle.png"], (needle.coordinates))
        else:
            win.blit(images["needle.png"], (32, 480))

        if not container.gathered:
            win.blit(images["container.png"], (container.coordinates))
        else:
            win.blit(images["container.png"], (64, 480))

        if syringe_created:
            win.blit(images["syringe.png"], (416, 480))

        if mac.alive:
            win.blit(images["plyr.png"], (macpos))

        if guard.alive:
            win.blit(images["guard.png"], (guardpos))

        if game_over and mac.alive:
            win.blit(images["victory.png"], (0, 0))

        if game_over and not mac.alive:
            win.blit(images["defeat.png"], (0, 0))

    # /DRAW

    # MOVEMENT

        player_action = pygame.key.get_pressed()

        if player_action[pygame.K_LEFT] and not game_over:
            macpos[0] = macpos[0] - mac.vel
            if tuple(macpos) in board.walls:
                macpos[0] = macpos[0] + mac.vel

        if player_action[pygame.K_RIGHT] and not game_over:
            macpos[0] = macpos[0] + mac.vel
            if tuple(macpos) in board.walls:
                macpos[0] = macpos[0] - mac.vel

        if player_action[pygame.K_UP] and not game_over:
            macpos[1] = macpos[1] - mac.vel
            if tuple(macpos) in board.walls:
                macpos[1] = macpos[1] + mac.vel

        if player_action[pygame.K_DOWN] and not game_over:
            macpos[1] = macpos[1] + mac.vel
            if tuple(macpos) in board.walls:
                macpos[1] = macpos[1] - mac.vel

    # /MOVEMENT

        pygame.display.flip()
