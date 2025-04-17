# Assignment: HW10
# File: TicTacToe.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
# 
# Date: 03/31/2025
# Description of Program: This program implements a simple Tic-Tac-Toe game where a human plays against a random computer opponent.
    
    
# Import the random module for generating random moves for the machine
import random

# Define global constants for players
HUMAN = 0  # Human player is represented as 0
MACHINE = 1  # Machine player is represented as 1

# Messages for different game scenarios
ILLEGAL_MOVE = "Illegal move. Try again!\n"
OCCUPIED_SPACE = "Space is occupied. Try again!\n"
YOU_WON = "Congratulations! You won!\n"
YOU_LOST = "Sorry! You lost!\n"
YOU_TIED = "Looks like a tie. Better luck next time!\n"
WELCOME = "Welcome to our Tic-Tac-Toe game!\nPlease begin playing.\n"

# Function to create an initial empty Tic-Tac-Toe board
def getInitialBoard():
    return [[" ", " ", " "],  
            [" ", " ", " "],  
            [" ", " ", " "]]

# Class representing the Tic-Tac-Toe game
class TicTacToeBoard:
    def __init__(self):
        """Initialize a Tic Tac Toe board and initial player."""
        self.__board = getInitialBoard()  # Create an empty board
        self.__current_player = HUMAN  # Set the first player as HUMAN

    def __str__(self):
        """Return a string representation of the board"""
        board_representation = ""
        # First row
        board_representation += self.__board[0][0] + "|" + self.__board[0][1] + "|" + self.__board[0][2] + " \n"
        board_representation += "-----\n"
        # Second row
        board_representation += self.__board[1][0] + "|" + self.__board[1][1] + "|" + self.__board[1][2] + " \n"
        board_representation += "-----\n"
        # Third row
        board_representation += self.__board[2][0] + "|" + self.__board[2][1] + "|" + self.__board[2][2] + " \n"
        return board_representation

    def getPlayer(self):
        """Return the current player."""
        return self.__current_player

    def isWin(self):
        """Does the current board configuration represent a win
        the current player."""
        token = "X" if self.__current_player == HUMAN else "O"

        # Check rows, columns, and diagonals
        for row in self.__board:
            if row[0] == token and row[1] == token and row[2] == token:
                return True
        for col in range(3):
            if self.__board[0][col] == token and self.__board[1][col] == token and self.__board[2][col] == token:
                return True
        if self.__board[0][0] == token and self.__board[1][1] == token and self.__board[2][2] == token:
            return True
        if self.__board[0][2] == token and self.__board[1][1] == token and self.__board[2][0] == token:
            return True
        return False

    def swapPlayers(self):
        """Swap current player: HUMAN for MACHINE or vice versa."""
        self.__current_player = MACHINE if self.__current_player == HUMAN else HUMAN

    def humanMove(self):
        """Accept and validate a move from the HUMAN.  Keep trying
        until a valid move is entered.  Update the board accordingly."""
        while True:
            move = input("\nYour turn:\n  Specify a move r c: ").strip()
            parts = move.split()
            
            # Validate input format
            if len(parts) != 2 or not all(part.isdigit() for part in parts):
                print(ILLEGAL_MOVE)
                continue
            
            row, col = map(int, parts)
            
            # Validate range
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print(ILLEGAL_MOVE)
                continue
            
            # Validate if the space is empty
            if self.__board[row][col] != " ":
                print(OCCUPIED_SPACE)
                continue
            
            # Place the move
            self.__board[row][col] = "X"
            return

    def machineMove(self):
        """Generate a random legal move by MACHINE. Make and report the move."""
        print("\nMachine's turn:")
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if self.__board[r][c] == " ":
                print("  Machine chooses: ", r, c)
                self.__board[r][c] = "O"
                return

# Function to drive the game
def driver():
    """This plays tic-tac-toe in a pretty simple-minded fashion. The human player goes first with token "X" and alternates with the machine using token "O". We print the board before the first move and after each move."""
    print(WELCOME)  # Print welcome message
    ttt = TicTacToeBoard()  # Initialize the game board
    print(ttt)  # Display the initial empty board

    for move in range(9):  # Maximum 9 moves in Tic-Tac-Toe
        if ttt.getPlayer() == HUMAN:
            ttt.humanMove()
            print(ttt)
            if ttt.isWin():
                print(YOU_WON)
                return
        else:
            ttt.machineMove()
            print(ttt)
            if ttt.isWin():
                print(YOU_LOST)
                return
        ttt.swapPlayers()

    print(YOU_TIED)  # If no one wins after 9 moves, it's a tie

driver()  # Start the game