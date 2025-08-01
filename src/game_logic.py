"""
Sydney Umezurike
game_logic.py
CS 5001 - Memory Game
This file handles the core game mechanics 
for the Memory Game, including card behavior 
and game logic like creating and shuffling 
the deck, and checking for matches.
"""

import random
import turtle
import os
from constants import ASSETS_PATH

class Card:
    def __init__(self, image):
        '''Initializes the card with a given image.
        
        Args:
            image (str): The path to the image representing the card.
        
        Returns:
            None
        '''
        self.image = image  # Sets the card's image
        self.face_up = False  # Tells if the card is face up
        self.matched = False  # Tells if the card has been matched

    def flip(self):
        '''Flips the card to show its face.
        
        Returns:
            None
        '''
        self.face_up = not self.face_up

    def match(self, other_card):
        '''Compares this card with another card. Returns True if they match.
        
        Args:
            other_card (Card): Another card object to compare with.
        
        Returns:
            bool: True if the cards match, False otherwise.
        '''
        return self.image == other_card.image

class MemoryGameLogic:
    def __init__(self, card_images=None):
        '''Initializes the game logic with the provided card images or the default deck.
        
        Args:
            card_images (list): List of image paths for the cards. Defaults to None, if the default deck is used.
        
        Returns:
            None
        '''
        if card_images is None:
            card_images = self.get_default_deck()  # Use the default deck if no custom images are provided
        self.card_images = card_images
        self.cards = self.create_deck()

    def create_deck(self):
        '''Creates the deck of cards based on the images.
        
        Returns:
            list: A shuffled deck of cards.
        '''
        deck = []
        # Duplicate each image for matching pairs
        for image in self.card_images:
            deck.append(Card(image))
            deck.append(Card(image))
        random.shuffle(deck)  # Shuffle the deck
        return deck

    def get_default_deck(self):
        '''Returns a list of image paths from the default deck configuration file.
        
        The default deck is loaded from the default_deck.txt file in the assets directory.
        
        Returns:
            list: Paths to the images in the default deck.
        
        Raises:
            Exception: If the `default_deck.txt` file is not found or cannot be read.
        '''
        try:
            default_deck_path = os.path.join(ASSETS_PATH, "default_deck.txt")
            with open(default_deck_path, "r") as file:
                return file.read().splitlines()  # Read all the lines and return them as a list
        except Exception as e:
            turtle.write(f"Error loading default deck: {e}", align="center", font=("Arial", 16, "bold"))
            return []  # If default deck can't be loaded, return an empty list

    def check_for_match(self, card1, card2):
        '''Checks if two cards match.
        
        Args:
            card1 (Card): The first card to compare.
            card2 (Card): The second card to compare.
        
        Returns:
            bool: True if the cards match, False otherwise.
        '''
        if card1.match(card2):
            card1.matched = card2.matched = True  # Mark both cards as matched
            return True
        return False

    def check_all_matched(self):
        '''Checks if all cards have been matched.
        
        Returns:
            bool: True if all cards are matched, False otherwise.
        '''
        return all(card.matched for card in self.cards)
