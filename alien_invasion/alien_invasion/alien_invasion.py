import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


def run_game():
    # Initialise pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    #Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    #Set the background colour
    bg_colour = (230, 230, 230)

    #Make an alien
    alien = Alien(ai_settings, screen)

    #Make a group to store aliens in
    aliens = Group()

    #Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Start the main loop for the game
    while True:
        
        #Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        #Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_colour)
        ship.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()

run_game()