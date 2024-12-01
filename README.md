# Tic Tac Toe Game

## Overview

As a software developer, I strive to create engaging and interactive applications that enhance user experience. This project focuses on developing a simple yet addictive Tic Tac Toe game using Django, allowing players to challenge each other. The goal is to provide an intuitive interface for players while implementing core game mechanics.

The game is built using HTML, CSS, and Python(Django), featuring a clean design and responsive layout. Players can take turns placing their markers (X or O) on a 3x3 grid, with the objective of getting three in a row—either horizontally, vertically, or diagonally.

This software aims to offer an enjoyable gameplay experience and help me further develop my web development skills while applying best practices in Django and web design.

**Software Demo Video:** ()

## Web Pages

1. **Home Page**:
   - **Description**: The home page serves as the main entry point for users. It displays a brief description of the game and allows players to start a new game. The page also features a leaderboard that dynamically shows the top 5 players with the most wins.
   - **Dynamic Elements**:
     - **Leaderboard**: The top 5 players, along with their win counts, are pulled dynamically from the SQLite database using Django's ORM.

2. **Player Setup Page**:
   - **Description**: This page allows players to enter their names before starting a game. Each player inputs their name, which will be displayed during the game.
   - **Dynamic Elements**:
     - **Player Name Inputs**: Fields are provided for entering player names. The names are used throughout the game to indicate whose turn it is.

3. **Game Page**:
   - **Description**: This is the main game board where the Tic Tac Toe game is played. Two players alternate turns, marking either an X or O on the 3x3 grid. The page tracks the current player's turn and updates the board after each move.
   - **Dynamic Elements**:
     - **Game Board**: The 3x3 grid dynamically updates to reflect the players' moves.
     - **Turn Indicator**: The game displays which player’s turn it is, dynamically changing between turns.
     - **Win Detection**: After each move, the game checks for a winner or a draw and dynamically displays the result.
     - **Reset Button**: A reset button allows players to restart the game without leaving the page or having to change player names.

## Development Environment

- **Tools Used:** Visual Studio Code, GitHub
- **Programming Languages:** HTML, CSS, Python(Django)

## Useful Resources

* [Django Documentation](https://docs.djangoproject.com/en/stable/)
* [MDN Web Docs - HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [W3Schools - CSS](https://www.w3schools.com/css/)

## Future Work

* Implement AI for practicing by yourself without storing wins.
* Introduce mobile responsiveness and touch support for better gameplay on mobile devices.
* Add difficulty by making new boards with more cells that would make the player connect 4 in a row.