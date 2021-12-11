# Sudoku Game   

This is a sudoku game based on the [pygame package](https://www.pygame.org/news) in python.
> Never played before? Don't worry, check out the rules [here](https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/).

## Feature

> + The original and pure Sudoku game.
> + Multiple player files can be created.

### Level mode

> 1. More than twenty levels to challenge.
> 2. Difficulty gradually increases throughout the game.
> 3. Earn hint points during playing.

### Endless mode

*Tired of playing level by level? We got endless mode!*

> * Five different levels of difficulty are set in endless mode.

### How to earn hint points?

> + Every time you clear a puzzle, you will get fixed `clearance points` according to the difficulty and `bonus points` based on your game speed. 
> + The faster you solve, the more points you will receive.
> + Every 100 points can be exchanged for one hint.

## Usage  

### To start the game

> + Install and configure the `python 3.9` environment.
> + Run `pip install -r requirements.txt` before playing.
> + Run `python start_game.py` to start the program.
> + Input your name to register a new profile to start playing!  

**User name should only conclude English letters and numbers, the following special symbols are forbidden:**  

 ` '?' '"' '/' '\' '|' '*' '<' '>' '; ' `

### To delete archive

Delete the file with the user name in ` ~\Sudoku_Project\data\users ` .

### To reset puzzles in level mode

*Not recommended, will affect the old profiles.*

> + Make sure you have cleared the game in at least one archive.
> + Run `python generate_level.py` .

###
