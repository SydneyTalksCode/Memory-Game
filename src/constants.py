"""
Sydney Umezurike
constants.py
CS 5001 - Memory Game
Contains constant values and 
configurations used in the game.
"""

import os

# Screen settings
SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600  
BG_COLOR = "#A0D6D8"  
INITIAL_BG_COLOR = "pink"  

# Card settings
CARD_SPACING = 50  
CARD_WIDTH = 100  
CARD_HEIGHT = 150  
START_X = -550  
START_Y = 300  
COLUMNS = 4  

# Button coordinates
QUIT_BUTTON_X = (250, 350)  
QUIT_BUTTON_Y = (-320, -220)  
LOAD_BUTTON_X = (120, 220)  
LOAD_BUTTON_Y = (-320, -220)  

# Timing constants
SPLASH_SCREEN_DURATION = 2  
CARD_FLIP_DURATION = 1  
END_CREDITS_DURATION = 5  
QUIT_MESSAGE_DURATION = 3  
WARNING_DURATION = 3  

# Valid card counts
VALID_CARD_COUNTS = [8, 10, 12]  
DEFAULT_CARD_COUNT = 8  

# File names
DEFAULT_DECK = "default_deck.txt"  
CARD_BACK = "CardBack.gif"  
SPLASH_SCREEN = "splashscreen.gif"  
WINNER_IMAGE = "winner.gif"  
END_CREDITS = "EndCredits.gif"  
QUIT_MESSAGE = "quitmsg.gif"  
CARD_WARNING = "card_warning.gif"  
QUIT_BUTTON = "quitbutton.gif"  
LOAD_BUTTON = "load_deck_button.gif"  
LEADERBOARD_FILE = "leaderboard.txt"  

# Assets path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  
ASSETS_PATH = os.path.join(CURRENT_DIR, "..", "assets")  
