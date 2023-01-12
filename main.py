# Library
import pygame
from random import randrange
import time
from math import sqrt


# Constants
HEIGHT = 800
WIDTH = 800
COLOR_BCKGRD = (30, 30, 30)
COLOR_MAT = (52, 92, 35)
COLOR_LINE = (100, 155, 80)
COLOR_ALERT = (100, 40, 40)
mission = 10

# Functions


def nearest_dice(mouse_pos):
    """ Returns the index of the nearest dice from de mouse.
        0 for dice 1.
    """
    dice_choice = None
    pos = (WIDTH//2, HEIGHT//2)
    dice_dim = dices_images[0].get_rect()
    dist_limit = sqrt((dice_dim[2]/2)**2 + (dice_dim[3]/2)**2)
    min_distance = dist_limit
    for dice_index in range(3):
        offset = (dice_index-1)*120
        dice_position = (pos[0]+offset, pos[1])
        dice_distance = sqrt(
            (mouse_pos[0]-dice_position[0])**2 + (mouse_pos[1]-dice_position[1])**2)
        if dice_distance < dist_limit and dice_distance < min_distance:
            min_distance = dice_distance
            dice_choice = dice_index
    return dice_choice


def dice_roll(dice_number: int):
    """ Takes the number of the dice as parameter.
        Randomly draw a number between 1 and 6. Draw the Dice and retrun the number.
    """
    for _ in range(10):
        dice_value = randrange(1, 7)
        dice_values[dice_number-1] = dice_value
        screen_update()
        time.sleep(0.05)
    return dice_value


def screen_update(victory=None):
    """ Refreshes the display of graphic elements.
        scores list format : [total_score_player1, total_score_player2, rolls_player1, rolls_player2]
        if victory is not None, print the name of the winner. (victory = 1 for player 1)
    """
    text = base_font.render("Manches gagnées", 0, (10, 10, 10))
    textpos = text.get_rect(center=(WIDTH//4, 10))
    surface_up_header.blit(text, textpos)
    screen.blit(surface_up_header, (WIDTH//4, 20))
    surface_up.fill(COLOR_MAT)
    text = base_font.render("Joueur 1", 0, (10, 10, 10))
    textpos = text.get_rect(centerx=WIDTH//8, centery=10)
    surface_up.blit(text, textpos)
    text = base_font.render("Joueur 2", 0, (10, 10, 10))
    textpos = text.get_rect(centerx=3*WIDTH//8, centery=10)
    surface_up.blit(text, textpos)
    # Total score of player1
    text = base_font.render(str(scores[0]), 0, (10, 10, 10))
    textpos = text.get_rect(centerx=WIDTH//8, centery=30)
    surface_up.blit(text, textpos)
    # Total score of player2
    text = base_font.render(str(scores[1]), 0, (10, 10, 10))
    textpos = text.get_rect(centerx=3*WIDTH//8, centery=30)
    surface_up.blit(text, textpos)
    screen.blit(surface_up, (WIDTH//4, 40))

    pygame.draw.rect(screen, COLOR_LINE, pygame.Rect(
        WIDTH//4, 40, WIDTH//2, 40),  2)

    text = base_font.render(
        "Partie en cours : Nombre de lancés", 0, (10, 10, 10))
    textpos = text.get_rect(center=(WIDTH//4, 10))
    surface_down_header.blit(text, textpos)
    screen.blit(surface_down_header, (WIDTH//4, 700))
    surface_down.fill(COLOR_MAT)
    text = base_font.render("Joueur 1", 0, (10, 10, 10))
    textpos = text.get_rect(centerx=WIDTH/8, centery=10)
    surface_down.blit(text, textpos)
    text = base_font.render("Joueur 2", 0, (10, 10, 10))
    textpos = text.get_rect(centerx=3*WIDTH/8, centery=10)
    surface_down.blit(text, textpos)
    # number of player1's rolls
    dice = ""
    if player_turn == 1:
        dice = '► '
    text = base_font.render(dice + str(scores[2]), 0, (10, 10, 10))
    textpos = text.get_rect(centerx=WIDTH/8, centery=30)
    surface_down.blit(text, textpos)
    # number of player2's rolls
    dice = ""
    if player_turn == 2:
        dice = '► '
    text = base_font.render(dice+str(scores[3]), 0, (10, 10, 10))
    textpos = text.get_rect(centerx=3*WIDTH/8, centery=30)
    surface_down.blit(text, textpos)
    screen.blit(surface_down, (WIDTH//4, 720))

    pygame.draw.rect(screen, COLOR_LINE, pygame.Rect(
        WIDTH//4, 720, WIDTH//2, 40),  2)

    screen.blit(bck_ground, bckpos)

    for dice_index, dice_value in enumerate(dice_values):
        if dice_value != 0:
            dice_image = dices_images[dice_value-1]
            pos = (WIDTH//2, HEIGHT//2)
            dice_dim = dice_image.get_rect()
            offset = (dice_index-1)*120
            screen.blit(dice_image, (pos[0]+offset -
                        dice_dim[2]//2, pos[1]-dice_dim[3]//2))
    if victory is not None:
        text = "Le joueur " + str(victory) + "\ngagne cette manche."
        text = base_font.render(text, 1, (200, 10, 10))
        textpos = text.get_rect(center=(WIDTH//8, 20))
        surface_alert_victory.blit(text, textpos)
        surfpos = surface_alert_victory.get_rect(
            center=((WIDTH//2, 3*HEIGHT/4)))
        screen.blit(surface_alert_victory, surfpos)
        pygame.display.flip()
        time.sleep(2)
        screen_update()
    pygame.display.flip()
    # pygame.display.update()


# Main
pygame.init()
base_font = pygame.font.Font("assets/LiberationMono-Regular.ttf", 16)
screen = pygame.display.set_mode((HEIGHT, WIDTH))
screen.fill(COLOR_BCKGRD)
icon = pygame.image.load("assets/icon_dice.jpg").convert()
pygame.display.set_icon(icon)
pygame.display.set_caption("3D6")
bck_ground = pygame.image.load("assets/plateau_jeu.gif").convert()
bckpos = bck_ground.get_rect(centerx=WIDTH//2, centery=HEIGHT//2)

dices_images = []

for i in range(1, 7):
    dice_name = "assets/dice_" + str(i) + ".png"
    dices_images.append(pygame.image.load(dice_name).convert())

surface_up_header = pygame.Surface((WIDTH//2, 20))
surface_up_header = surface_up_header.convert()
surface_up_header.fill(COLOR_LINE)
surface_up = pygame.Surface((WIDTH//2, 40))
surface_up = surface_up.convert()
surface_up.fill(COLOR_MAT)

surface_down_header = pygame.Surface((WIDTH//2, 20))
surface_down_header = surface_down_header.convert()
surface_down_header.fill(COLOR_LINE)
surface_down = pygame.Surface((WIDTH//2, 40))
surface_down = surface_up.convert()
surface_down.fill(COLOR_MAT)

surface_alert_victory = pygame.Surface((WIDTH//4, 60))
surface_alert_victory = surface_alert_victory.convert()
surface_alert_victory.fill(COLOR_ALERT)

total_score_player1 = 0
total_score_player2 = 0
rolls_player1 = 0
rolls_player2 = 0
scores = [total_score_player1, total_score_player2,
          rolls_player1, rolls_player2]
player_turn = 2
dice_values = [mission, 0, 0]
dice_choice = None

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            dice_choice = nearest_dice(mouse_pos)

    if sum(dice_values) == mission:
        time.sleep(2)
        if player_turn == 2:
            if scores[2] > scores[3]:
                scores[1] += 1
                screen_update(2)
            elif scores[2] < scores[3]:
                scores[0] += 1
                screen_update(1)
            scores[2] = 0
            scores[3] = 0
            player_turn = 1
        else:
            player_turn = 2
        dice_values = [0, 0, 0]
        dice_values[0] = dice_roll(1)
        dice_values[1] = dice_roll(2)
        dice_values[2] = dice_roll(3)
        scores[player_turn+1] = 1
    else:
        if dice_choice is not None:
            dice_values[dice_choice] = dice_roll(dice_choice+1)
            scores[player_turn+1] += 1
            dice_choice = None

    screen_update()

pygame.quit()
