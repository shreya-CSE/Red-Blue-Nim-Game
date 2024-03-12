# Red-Blue Nim Game

Welcome to the Red-Blue Nim game! This is a simple console-based game where you compete against the computer. The goal is to strategically remove red and blue balls to maximize your score or win, depending on the game version. Below, you'll find an explanation of the game, how to run it, and some additional details.

## Game Overview
- **Objective**: Remove red and blue balls strategically to achieve the highest score or win the game.
- **Scoring**: Score is calculated based on the remaining red and blue balls. Red balls contribute 2 points each, while blue balls contribute 3 points each.
- **Game Versions**: Two game versions are available: "Standard" and "Misere." In the "Misere" version, the player aiming for the lowest score wins.

## How to Play
1. The game starts with a given number of red and blue balls.
2. Players take turns removing one ball at a time, choosing either red or blue.
3. If you are playing as the "Computer," the AI will make strategic moves based on the game version and depth.
4. If you are playing as the "Human," you will be prompted to choose a color to remove.

## Running the Game
To run the game, use the following command in your terminal:

```bash
python red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>
```

- `<num-red>`: Number of initial red balls.
- `<num-blue>`: Number of initial blue balls.
- `<version>`: Game version ("Standard" or "Misere").
- `<first-player>`: Starting player ("Computer" or "Human").
- `<depth>`: Depth of the game tree for AI moves. Use 0 for unlimited depth.

## Example Usage
```bash
python red_blue_nim.py 5 7 Standard Computer 3
```

This example initiates a game with 5 red and 7 blue balls, using the "Standard" version. The "Computer" starts, and the AI considers moves up to a depth of 3.
