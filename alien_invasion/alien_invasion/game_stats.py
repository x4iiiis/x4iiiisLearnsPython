import os  
import json 

class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialise stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Start Alien Invasion in an inactive state
        self.game_active = False

        #Check if highscore.json exists
        
        if os.path.isfile('./highscore.json'):    # True 
            #High score should never be reset
            with open('highscore.json', 'r') as infile:
                self.high_score = json.load(infile)

        else:
            self.high_score = 0



    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1