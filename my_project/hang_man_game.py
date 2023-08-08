# Hang man game instructions:

#Computer needs to choose random word from the list that the end user will guess
import random

words = ["Apple","Beach","Brain","Bread","Brush","Chair","Chest","Chord","Click","Clock","Cloud","Dance","Diary","Drink","Earth","Flute","Fruit","Ghost","Grape","Green","Happy","Heart","House","Juice","Light","Money","Music","Party","Pizza","Plant","Radio","River","Salad","Sheep","Shoes","Smile","Snack","Snake","Spice","Spoon","Storm","Table","Toast","Tiger","Train","Water","Whale","Wheel","Woman","World","Write","Youth"]

hangman_word = random.choice(words)

#list of all the variable s for hangman
guesses_remaining = 6
letters_guesses = []

#User needs to start the game and guess the first word 

# print("Hello user, welcome to the game of Hangman! Insert instructions ")