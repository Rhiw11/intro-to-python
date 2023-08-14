# Hang man game instructions:

#Computer needs to choose random word from the list that the end user will guess
import random
import hangman_stages

words = ["apple","beach","brain","bread","brush","chair","chest","chord","click","clock","cloud","dance","diary","drink","earth","flute","fruit","ghost","grape","green","happy","heart","house","juice","light","money","music","party","pizza","plant","radio","river","salad","sheep","shoes","smile","snack","snake","spice","spoon","storm","table","toast","tiger","train","water","whale","wheel","woman","world","write","youth"]

#list of all the variables for hangman
hangman_word = random.choice(words)
guesses_remaining = 6
letters_guessed = []
intro = (" _ " * len(hangman_word))
hangman_letter = False

#functions for hangman
def return_word(hangman_word):
  for l in hangman_word:
        if l in letters_guessed:
          print (l,end=" "),    
        else:  
          print (" _ ",end="")
  
# Instructions + welcme 
print("\nHello! Welcome to the game of hangman.\n\nCan you guess the word:\n\n" + str(intro) + "\n\nIf you make 6 mistakes you will lose!\n\nGood luck...")

print(hangman_word)

# print("Hello user, welcome to the game of Hangman! Insert instructions ")

while guesses_remaining >= 1:
    guess = input(str("\n\nPlease guess a letter (lowercase): ")).lower()  
    
    if guess in letters_guessed:
      print("\nHmm that letter's already been guessed, try again...\n")

  
    elif guess in hangman_word:
      letters_guessed.append(guess)
      print("\nWell done, that's correct!\nHere's the word so far:\n\n")
      return_word(hangman_word)  
      
  
    elif guess not in hangman_word:
      guesses_remaining -= 1
      letters_guessed.append(guess)
      print("Oh dear, that's not in the word! You have " +     str(guesses_remaining) + " guesses remaining.\n\nHere's the word so far:\n\n")
      return_word(hangman_word) 
      

    else:
      print("Hmm, that doesn't look right... please enter a letter")

    if guesses_remaining == 0:
      print("\n\nOh no, you lost!\nThe word you were looking for was:\n\n" + str(hangman_word).upper() + "\n\nBetter luck next time!")
      break

  
    for i in hangman_word:
      if i in letters_guessed:
        hangman_letter = True 
      else:
        hangman_letter = False
        break
    if hangman_letter == True:
      print("\nCongrats, you won! You guessed the word " + str(hangman_word).upper() + " correctly.\n\nThanks for playing!" )
      break
    
    

