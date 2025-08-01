"""
Sydney Umezurike
leaderboard.py
CS 5001 - Memory Game
This file contains methods for managing and 
displaying the leaderboard for the memory game.
It draws the leaderboard's border, updates 
scores, and displays the leaderboard on the screen.
"""

import os
import turtle
from constants import ASSETS_PATH

class Leaderboard:
    def __init__(self, screen):
        """Initialize the leaderboard.

        Args:
            screen: The turtle screen to draw on.
        """
        self.screen = screen
        self.leaderboard_path = os.path.join(ASSETS_PATH, "leaderboard.txt")

    def draw_border(self):
        """Draw the leaderboard border.

        This method draws the border for the leaderboard area on the screen.
        
        Returns:
            None
        """
        border = turtle.Turtle()
        border.hideturtle()
        border.speed(0)
        border.penup()
        border.goto(100, 400)  # Start position for the border
        border.pendown()
        border.pensize(3)
        border.color("pink")
        for _ in range(2):
            border.forward(250)  # Width of leaderboard
            border.right(90)
            border.forward(600)  # Height of leaderboard
            border.right(90)

        # Write "Leaders:" inside the border
        leader = turtle.Turtle()
        leader.hideturtle()
        leader.speed(0)
        leader.penup()
        leader.goto(120, 350)  # Adjusted position inside the border
        leader.color("black")
        leader.write("Leaders:", font=("Arial", 16, "bold"))

    def update_scores(self, player_name, moves):
        """Update leaderboard with current player's score.

        This method reads the existing scores, adds the new player's score,
        sorts the scores, and writes the top 6 scores back to the leaderboard file.
        
        Args:
            player_name (str): The name of the player.
            moves (int): The number of moves taken by the player.
        
        Returns:
            None
        """
        try:
            # Read existing scores from the leaderboard file
            scores = []
            if os.path.exists(self.leaderboard_path):
                with open(self.leaderboard_path, 'r') as file:
                    for line in file:
                        name, score = line.strip().split(',')
                        scores.append((name, int(score)))
            
            # Add the current player's score
            scores.append((player_name, moves))
            
            # Sort the scores in ascending order based on the number of moves
            scores.sort(key=lambda x: x[1])
            
            # Keep only the top 6 scores
            scores = scores[:6]
            
            # Write the updated scores back to the file
            with open(self.leaderboard_path, 'w') as file:
                for name, score in scores:
                    file.write(f"{name},{score}\n")
            
            # Update the leaderboard display
            self.display_scores()
            
        except Exception as e:
            print(f"Error updating leaderboard: {e}")

    def display_scores(self):
        """Display the leaderboard scores.

        This method clears the previous leaderboard scores and displays the current top scores.
        
        Returns:
            None
        """
        try:
            # Clear the previous leaderboard display
            leader = turtle.Turtle()
            leader.hideturtle()
            leader.speed(0)
            leader.penup()
            leader.goto(120, 350)
            leader.color("black")
            leader.write("Leaders:", font=("Arial", 16, "bold"))
            
            # Display the current leaderboard scores
            if os.path.exists(self.leaderboard_path):
                with open(self.leaderboard_path, 'r') as file:
                    y = 300  # Starting position for displaying scores
                    for line in file:
                        name, moves = line.strip().split(',')
                        leader.goto(120, y)
                        leader.write(f"{name}: {moves} moves", font=("Arial", 14))
                        y -= 30  # Space between entries
                        
        except Exception as e:
            print(f"Error displaying leaderboard: {e}")
