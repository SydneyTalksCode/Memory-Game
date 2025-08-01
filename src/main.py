"""
Sydney Umezurike
main.py
CS 5001 - Memory Game
Main file for Memory Game
Manages game setup, user input, and 
controls the flow of the game, 
including the main game loop and 
interactions like starting the 
game and displaying results.
"""

import turtle
import time
import os
from game_logic import MemoryGameLogic
from leaderboard import Leaderboard
from ui_components import GameUI
from constants import (
    ASSETS_PATH, SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, INITIAL_BG_COLOR,
    VALID_CARD_COUNTS, DEFAULT_CARD_COUNT, WARNING_DURATION,
    SPLASH_SCREEN_DURATION, END_CREDITS_DURATION
)

class MemoryGame:
    def __init__(self):
        """
        Initialize the game screen and components.
        
        Sets up the screen, initializes UI components, leaderboard, and game variables.
        """
        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.title("CS5001 Memory Game")
        self.screen.bgcolor(INITIAL_BG_COLOR)
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)
        
        # Initialize UI and leaderboard
        self.ui = GameUI(self.screen)
        self.leaderboard = Leaderboard(self.screen)
        
        # Initialize game
        self.player_name = ""
        self.card_count = DEFAULT_CARD_COUNT
        self.matches = 0
        self.guesses = 0
        self.cards = []
        self.selected_cards = []
        self.game_active = True
        self.current_deck = 'default_deck.txt'

    def load_deck(self):
        """
        Load the card images from the selected deck configuration.
        
        Checks if the deck file exists, reads the images, and adds them as shapes.
        If there is an issue loading the deck, it defaults to the default deck.
        
        Returns:
            bool: True if deck loading is successful, False if there is an error.
        """
        try:
            deck_path = os.path.join(ASSETS_PATH, self.current_deck)
            
            if not os.path.exists(deck_path):
                # If deck not found, default to the default deck
                if self.current_deck != 'default_deck.txt':
                    print(f"Error: Could not find deck file {self.current_deck}. Using default deck.")
                    self.current_deck = 'default_deck.txt'
                    return self.load_deck()
                raise FileNotFoundError(f"Default deck not found!")
                    
            with open(deck_path, 'r') as file:
                self.card_faces = [line.strip() for line in file if line.strip()]
                
                # Verify card images exist
                for card_face in self.card_faces:
                    card_path = os.path.join(ASSETS_PATH, card_face)
                    if not os.path.exists(card_path):
                        if self.current_deck != 'default_deck.txt':
                            print(f"Error: Could not find card image {card_face}. Using default deck.")
                            self.current_deck = 'default_deck.txt'
                            return self.load_deck()
                        raise FileNotFoundError(f"Card image not found: {card_face}")
                
                for card_face in self.card_faces:
                    self.screen.addshape(os.path.join(ASSETS_PATH, card_face))
                        
        except Exception as e:
            print(f"Error loading deck: {e}")
            if self.current_deck != 'default_deck.txt':
                print("Using default deck.")
                self.current_deck = 'default_deck.txt'
                return self.load_deck()
            raise
                
        return True

    def load_new_deck(self):
        """
        Load a new deck configuration file from user input.
        
        Prompts the user to input a file name for a custom deck, checks if the file exists in the assets folder,
        and reloads the game if valid. If the file is not found, it defaults to the default deck.
        
        Returns:
            None
        """
        try:
            message = "Please add your config file to the assets folder.\nEnter the name of your config file (e.g., custom_deck.txt):"
            deck_file = self.screen.textinput("Load New Deck", message)
            
            if deck_file:
                deck_path = os.path.join(ASSETS_PATH, deck_file)
                if os.path.exists(deck_path):
                    self.current_deck = deck_file
                    self.start_reload()
                else:
                    print(f"Error: Could not find {deck_file} in assets folder. Using default deck.")
                    self.current_deck = 'default_deck.txt'
                    self.start_reload()
                    
        except Exception as e:
            print(f"Error loading new deck: {e}")
            self.current_deck = 'default_deck.txt'
            self.start_reload()

    def start_reload(self):
        """
        Reset the game and reload the game board.
        
        Clears the screen, resets game variables, and sets the game back up.
        
        Returns:
            None
        """
        self.screen.clear()
        self.screen.bgcolor(BG_COLOR)
        self.matches = 0
        self.guesses = 0
        self.selected_cards = []
        self.cards = []
        self.setup_game()

    def setup_game(self):
        """
        Set up the game board and UI components.
        
        Draws the game border, leaderboard, status bar, and card buttons, then sets up click handling.
        
        Returns:
            None
        """
        try:
            self.screen.clear()
            self.screen.bgcolor(BG_COLOR)
            
            # Draw components
            self.ui.draw_game_border()
            self.leaderboard.draw_border()
            self.leaderboard.display_scores()
            self.ui.draw_status_bar(self.guesses, self.matches)
            self.create_cards()
            self.ui.create_buttons()
            
            # Set up click handling
            self.screen.onclick(self.handle_click)
            
            self.screen.update()
            
        except Exception as e:
            print(f"Error setting up game: {e}")

    def create_cards(self):
        """
        Create and position the cards on the game board.
        
        Loads the deck, shuffles card faces, and arranges them 
        in a grid. Each card is created as a turtle
        with its back facing up.
        
        Returns:
            None
        """
        import random
        
        # Load the deck first
        self.load_deck()
        
        # Create shuffled pairs of cards
        pairs_needed = self.card_count // 2
        card_faces = random.sample(self.card_faces, pairs_needed) * 2
        random.shuffle(card_faces)

        card_back = os.path.join(ASSETS_PATH, "CardBack.gif")
        self.screen.addshape(card_back)  
        
        cols = 4
        for i in range(self.card_count):
            row = i // cols
            col = i % cols
            
            card = turtle.Turtle()
            card.hideturtle()
            card.speed(0)
            card.penup()
            card.shape(card_back)
            card.face = os.path.join(ASSETS_PATH, card_faces[i])
            card.is_flipped = False
            card.goto(-550 + col * (100 + 50),
                     300 - row * (150 + 50))
            card.showturtle()
            self.cards.append(card)

    def handle_click(self, x, y):
        """
        Handle user clicks on cards and buttons.
        
        Checks if the click occurred on the quit button, load new deck button, or a card. 
        If on a card, it flips the card and checks for matches.
        
        Args:
            x (int): The x-coordinate of the mouse click.
            y (int): The y-coordinate of the mouse click.
        
        Returns:
            None
        """
        if y < -220 and y > -320:
            if 250 < x < 350:
                self.show_quit_message()
            elif 120 < x < 220:
                self.load_new_deck()
        else:
            for card in self.cards:
                card_x, card_y = card.pos()
                if (abs(card_x - x) < 50 and abs(card_y - y) < 75):
                    self.flip_card(card)
                    break
        
        self.screen.update()

    def flip_card(self, card):
        """
        Flip the selected card and check for matches.
        
        Flips the card and checks if two cards are flipped. If the two cards match, they stay flipped.
        If they don't match, they are flipped back.
        
        Args:
            card: The card that was clicked.
        
        Returns:
            None
        """
        if len(self.selected_cards) >= 2 or card in self.selected_cards:
            return
        
        card.shape(card.face)
        card.is_flipped = True
        self.selected_cards.append(card)
        
        # If two cards have been selected, check for a match
        if len(self.selected_cards) == 2:
            self.guesses += 1
            if self.selected_cards[0].face == self.selected_cards[1].face:
                self.matches += 1
                self.screen.ontimer(lambda: self.remove_matched_cards(), 1000)
                self.screen.ontimer(self.check_win, 1100)
            else:
                self.screen.ontimer(self.flip_back_cards, 1000)
            
            self.ui.update_status(self.guesses, self.matches)

    def remove_matched_cards(self):
        """
        Hide matched cards from the game board.
        
        Marks the matched cards as hidden and resets the selected cards.
        
        Returns:
            None
        """
        for card in self.selected_cards:
            card.hideturtle()
        self.selected_cards = []

    def flip_back_cards(self):
        """
        Flip non-matching cards back to their face-down position.
        
        Reverts the non-matching cards back to their card back image.
        
        Returns:
            None
        """
        card_back = os.path.join(ASSETS_PATH, "CardBack.gif")
        for card in self.selected_cards:
            card.shape(card_back)
            card.is_flipped = False
        self.selected_cards = []
        self.screen.update()

    def check_win(self):
        """
        Check if the player has won the game.
        
        If all cards are matched, update the leaderboard and show the winner message.
        
        Returns:
            None
        """
        if self.matches == self.card_count // 2:
            self.leaderboard.update_scores(self.player_name, self.guesses)
            winner = self.ui.show_winner()
            self.screen.ontimer(lambda: self.show_end_credits(), 2000)

    def show_end_credits(self):
        """
        Show the end credits after the game is won.
        
        Displays the end credits and exits the game.
        
        Returns:
            None
        """
        try:
            #Make end credits fullscreen
            canvas = self.screen.getcanvas()
            root = canvas.winfo_toplevel()
            root.attributes('-fullscreen', True)
            
            self.screen.clear()
            self.screen.bgcolor("black")
            
            credits_path = os.path.join(ASSETS_PATH, "EndCredits.gif")
            self.screen.bgpic(credits_path)
            self.screen.update()
            
            # Wait 5 seconds then close game
            self.screen.ontimer(lambda: self.screen.bye(), 5000)
            
        except Exception as e:
            print(f"Error showing end credits: {e}")

    def show_quit_message(self):
        """
        Show the quit message and end the game.
        
        Displays the quit message and then shows the end credits before exiting.
        
        Returns:
            None
        """
        quit_msg = self.ui.show_quit_message()
        self.screen.ontimer(lambda: self.show_end_credits(), 3000)

    def get_player_name(self):
        """
        Ask the player for their name.
        
        Requests the player's name through an input box.
        
        Returns:
            bool: True if a name is entered, False otherwise.
        """
        name = self.screen.textinput("Player Name", "Enter your name:")
        if name:
            self.player_name = name.strip()
            return True
        return False

    def get_card_count(self):
        """
        Ask the player for the number of cards to play with.
        
        Requests and validates the number of cards to be used in the game (8, 10, or 12).
        
        Returns:
            None
        """
        try:
            count_str = self.screen.textinput("Card Count", 
                "Enter number of cards (8, 10, or 12):")
            
            if count_str:
                count = int(count_str)
                
                if count not in VALID_CARD_COUNTS:
                    warning = self.ui.show_warning()
                    time.sleep(WARNING_DURATION)
                    warning.hideturtle()
                    
                    count = min(VALID_CARD_COUNTS, key=lambda x: abs(x - count))
                
                self.card_count = count
                
        except ValueError:
            self.card_count = DEFAULT_CARD_COUNT
        except Exception as e:
            print(f"Error getting card count: {e}")
            self.card_count = DEFAULT_CARD_COUNT

def main():
    """Run the main game sequence."""
    try:
        game = MemoryGame()
        
        splash = game.ui.show_splash_screen()
        time.sleep(SPLASH_SCREEN_DURATION)
        splash.hideturtle()
        game.screen.clear()
        game.screen.bgcolor(BG_COLOR)
        
        if game.get_player_name():
            game.get_card_count()
            game.setup_game()
            game.screen.mainloop()
            
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
