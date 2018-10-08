# Ian Michael Jesu Alvarez
# CPSC 386 (Friday)
# This creates the window for the whole game

import pygame, sys
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from bunker import Bunker

import game_functions as gf

# Initialize game, settings, and screen object.
pygame.init()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Alien Invasion")


def message_to_screen(msg, color, position, font_size):
    font = pygame.font.SysFont(None, font_size)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, position)


def start_text():
    # Title
    message_to_screen("SPACE", WHITE, [ai_settings.screen_width / 2 - 100, 50], 100)
    message_to_screen("INVADERS", GREEN, [ai_settings.screen_width / 2 - 80, 110], 55)

    # Play game text
    play_game = message_to_screen("PLAY GAME", GREEN, [ai_settings.screen_width / 2 - 55, 350], 35)
    highscores = message_to_screen("HIGH SCORES", WHITE, [ai_settings.screen_width / 2 - 70, 400], 35)

    pygame.display.update()


def game_intro():

    start_text()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run_game()


def run_game():

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make an alien.
    # alien = Alien(ai_settings, screen)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # bunker = Bunker(ai_settings, screen)
    bunkers = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create the row of bunkers
    gf.create_bunkers(ai_settings, screen, bunkers)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # Redraw and update screen
            ship.update()
            bullets.update()

            print(len(bullets))

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, bunkers)


game_intro()
run_game()
