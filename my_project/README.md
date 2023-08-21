# Hangman Game 




## Project Description

This is a hangman game where the user will attempt to guess the randomly generated secret word from the list. 
Everytime the user inputs a letter, the Shell will return a response depending on whether the user's guess was correct, incorrect or invalid. 
When the user guesses correctly, the computer will reveal where the letter is placed in the word.
The user can make up to 6 mistakes; once all attempts are used, the user will lose and the game will end. 


## How to play the game

* The player starts the game by moving their current directpry to the location of the file, then running the file 'hang_man_game.py' in Shell with:
  ```
  python hang_man_game.py

  ```
* The Shell will display the instructions of the game to the player and ask them to input a guess:
   ```
    #example guess
  Please guess a letter: a 
  ```
* The player will then input a guess and the shell will return a response depending on the guess inputted by the user:
  - If the player guesses correctly, the Shell will reveal to the player where the letter falls in the word 
  - If the guess is incorrect, the Shell will inform the player that the letter guessed is incorrect, remind the correct letters guess so far, as well as the number of guesses remaining
  - If the letter has already been guessed, the Shell will tell the player that the letter has already been guessed but won't reduce the remaning attempts, and will ask the player to guess again
  -If the player inputs an invalid guess e.g., number, multiple letters then the Shell will ask the player to guess again
* If the player guesses all the letters correctly within the allowed attempts, the game will end and the player wins
* If the player uses all guess attempts before they guess all the letters in the word, the game will end and the secret word will be revealed

## Credits
Rhian Walters