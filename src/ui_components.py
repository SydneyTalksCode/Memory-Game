"""
Sydney Umezurike
ui_components.py
CS 5001 - Memory Game
Contains methods for handling game UI elements 
such as the game border, status bar, 
splash screen, buttons, etc.
"""

import turtle
import os
from constants import ASSETS_PATH, CARD_SPACING, CARD_WIDTH, CARD_HEIGHT, START_X, START_Y

class GameUI:
    def __init__(self, screen):
        """Initialize UI components
        
        Args:
            screen (turtle.Screen): The turtle screen to draw on
        """
        self.screen = screen

    def draw_game_border(self):
        """Draw the main game border.
            
        Returns:
            None
        """
        border = turtle.Turtle()
        border.hideturtle()
        border.penup()
        border.goto(-675, 400)
        border.pendown()
        border.pensize(3)
        for i in range(2):
            border.forward(700)
            border.right(90)
            border.forward(600)
            border.right(90)

    def draw_status_bar(self, guesses, matches):
        """Draw the status bar.
        
        Args:
            guesses (int): The number of guesses made.
            matches (int): The number of matches found.
        
        Returns:
            None
        """
        # Draw the status border
        border = turtle.Turtle()
        border.hideturtle()
        border.speed(0)
        border.penup()
        border.goto(-675, -250)  # Start position for border
        border.pendown()
        border.pensize(3)
        border.color("black")
        for _ in range(2):
            border.forward(700)  # Width of status bar
            border.right(90)
            border.forward(100)  # Height of status bar
            border.right(90)
        
        # Draw the status text
        status = turtle.Turtle()
        status.hideturtle()
        status.speed(0)
        status.penup()
        status.goto(-650, -300)  # Position for status text
        status.color("black")
        status.write(f"Status: {guesses} moves, {matches} matches", 
                    font=("Arial", 20, "bold"))

    def update_status(self, guesses, matches):
        """Update the status bar text only.
        
        Args:
            guesses (int): The number of guesses made.
            matches (int): The number of matches found.
        
        Returns:
            None
        """
        status = turtle.Turtle()
        status.hideturtle()
        status.speed(0)
        status.penup()

        # Clear the previous text by drawing a rectangle over it
        status.fillcolor("#A0D6D8") 
        status.goto(-650, -280)
        status.begin_fill()
        status.forward(400)
        status.right(90)
        status.forward(40)
        status.right(90)
        status.forward(400)
        status.right(90)
        status.forward(40)
        status.end_fill()

        # Write new status
        status.penup()
        status.goto(-650, -300)
        status.color("black")
        status.write(f"Status: {guesses} moves, {matches} matches", 
                    font=("Arial", 20, "bold"))

    def create_buttons(self):
        """Create the game buttons.
        
        Args:
            None
        
        Returns:
            None
        """
        # Register button images
        quit_path = os.path.join(ASSETS_PATH, "quitbutton.gif")
        load_path = os.path.join(ASSETS_PATH, "load_deck_button.gif")
        self.screen.addshape(quit_path)  
        self.screen.addshape(load_path) 
        
        # Create quit button
        quit_btn = turtle.Turtle()
        quit_btn.penup()
        quit_btn.shape(quit_path)
        quit_btn.goto(275, -290)
        quit_btn.showturtle()
        
        # Create load deck button
        load_btn = turtle.Turtle()
        load_btn.penup()
        load_btn.shape(load_path)
        load_btn.goto(160, -290)
        load_btn.showturtle()

    def show_splash_screen(self):
        """Display the splash screen.
        
        Args:
            None
        
        Returns:
            splash: The splash screen
        """
        try:
            # Create and position splash screen
            splash = turtle.Turtle()
            splash.hideturtle()
            splash.penup()
            
            # Load and show splash image
            splash_path = os.path.join(ASSETS_PATH, "splashscreen.gif")
            self.screen.addshape(splash_path)
            splash.shape(splash_path)
            splash.showturtle()
            self.screen.update()
            
            return splash  
            
        except Exception as e:
            print(f"Error showing splash screen: {e}")
            return None

    def show_warning(self):
        """Show card count warning message telling the user that
        it will be rounded to the nearest value.
        
        Args:
            None
        
        Returns:
            warning: The warning message
        """
        warning = turtle.Turtle()
        warning.hideturtle()
        warning.penup()
        
        warning_path = os.path.join(ASSETS_PATH, "card_warning.gif")
        self.screen.addshape(warning_path)
        warning.shape(warning_path)
        warning.goto(0, 0)
        warning.showturtle()
        self.screen.update()
        
        return warning  

    def show_winner(self):
        """Show winner message.
        
        Args:
            None
        
        Returns:
            winner: The winner message
        """
        winner = turtle.Turtle()
        winner.hideturtle()
        winner.penup()
        
        winner_path = os.path.join(ASSETS_PATH, "winner.gif")
        self.screen.addshape(winner_path)
        winner.shape(winner_path)
        winner.goto(0, 0)
        winner.showturtle()
        self.screen.update()
        
        return winner

    def show_quit_message(self):
        """Show quit message.
        
        Args:
            None
        
        Returns:
            quit_msg: The quit message
        """
        quit_msg = turtle.Turtle()
        quit_msg.hideturtle()
        quit_msg.penup()
        
        quit_path = os.path.join(ASSETS_PATH, "quitmsg.gif")
        self.screen.addshape(quit_path)
        quit_msg.shape(quit_path)
        quit_msg.goto(0, 0)
        quit_msg.showturtle()
        self.screen.update()
        
        return quit_msg
