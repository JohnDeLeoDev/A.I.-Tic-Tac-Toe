# John DeLeo
# CS534
# Individual Project Assignment 3

## Included Files
- README.md
- TicTacToeGameApp.py
- TicTacToeClass.py

## Running the Program
To run the program, execute the following command in the terminal:
```
python3 TicTacToeGameApp.py
```

## Description
A python implementation of A.I. algorithms for the game Tic-Tac-Toe. The program allows the user to play against the computer, which can use a variety of algorithms to determine its moves. The user can choose between the following algorithms:
- Random
- MiniMax
- Alpha-Beta
- Heuristic Alpha-Beta 
- Monte Carlo Tree Search

## Implementation
The program is implemented using the following classes:
- `TicTacToeGameApp`: The main app that creates a TicTacToe object, runs the game and handles user input.
- `TicTacToe`: A class that represents the game board and contains methods for checking the game state and making moves. Also contains methods for the computer to make moves using various algorithms.
- `Player`: An abstract class that represents a player in the game.
- `Board`: A class that represents the game board and contains methods for making moves and checking the game state.
- `Node`: A class that represents a node in the game tree for the Monte Carlo Tree Search algorithm.

## Algorithms
- Random: The computer makes a random move.
- MiniMax: The computer uses the MiniMax algorithm to determine its move.
- Alpha-Beta: The computer uses the Alpha-Beta algorithm to determine its move.
- Heuristic Alpha-Beta: The computer uses the Alpha-Beta algorithm with a heuristic evaluation function to determine its move.
- Monte Carlo Tree Search: The computer uses the Monte Carlo Tree Search algorithm to determine its move.
