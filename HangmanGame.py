import random
from random_words import words
import string
def choose_word(words):
   word = random.choice(words)
   while '_' in word or ' ' in word:
       word = random.choice(words)
   return word
def hangman():
   word = choose_word(words)
   #print(word)
   word_letters = set(word)
   A = len(word)
   #word_letters = ['a', 'n', 't']
   alphabet = set(string.ascii_lowercase)
   used_letters = set()#what the user has guessed
   # getting user input
   print(f'This is a {A}-letter word' )
   while len(word_letters) > 0:
       guess_letter = input('Guess a letter: ').lower()
       if guess_letter in alphabet - used_letters:
           used_letters.add(guess_letter)
           if guess_letter in word_letters:
               word_letters.remove(guess_letter)
       elif guess_letter in used_letters:
           print('You have already used that letter. Please try again: ')
       else:
           print('Invalid character, please try again.')
       print('You have used these letters: ', ' '.join(sorted(used_letters)))#.join converts list to string
       word_list = [i if not (i in word and i in word_letters) else '-' for i in word]
       print('Current word is: ', ' '.join(word_list))
   Again()
def Again ():
   A = input('Congratulations!! You have guessed correctly.\nDo you want to play again? y or n: ').lower()
   while A not in ['y', 'n']:
       A = input('Invalid entry, please type y for yes and n for no: ')
   if A == 'y':
       hangman()
   else:
       print('Bye, see you another time!')
       exit()
hangman()
