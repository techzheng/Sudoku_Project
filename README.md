# Sudoku Game   
This is a sudoku game based on the ```pygame``` package in python.

## Feature
> + The original and pure Sudoku game.
> + Multiple player files can be created.
> + There are more than twenty levels to challenge.
> + The difficulty of the level gradually increases throughout the game.
> + Earn hint points during playing.
> + Tired of playing level by level? We got endless mode.
> + Five different levels of difficulty are set in endless mode.
> + Puzzles in level mode can be reset easily.  

## Usage  
### To start the game
> + Install and configure the ```python 3.9``` environment.
> + Run ```pip install -r requirements.txt``` before playing.
> + Run ``` python setip.py``` to start the program.
> + Input your name to register a new profile to start playing!  

**User name should only conclude English letters and numbers, the following special symbols are forbidden:**  
```'?' '"' '/' '\' '|' '*' '<' '>' ';' ```
### To delete archive
Delete the file with the user name in ```~\Sudoku_Project\data\users```.
### To reset puzzles in level mode
*Not recommended, will affect the old profiles.*
> + Make sure you have cleared the game in at least one archive.
> + Run ```python generate_level.py```
###