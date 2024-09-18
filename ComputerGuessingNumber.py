import random
try:
    x = int(input('Please provide the max number of your range > 1 (e.g. 10): '))
    x > 1
except:
    print('You did not input a valid value, the default value 10 will be used.')
    x = 10
def CG(x):
  (Check, low, high) = ('', 1, x)
  print(f"Keep a number between {low} and {high} in your head. I will try to guess that number...\n")
  while Check != 'c':
      try:
          R = random.randint(low, x)
      except:
          print('Your input is inconsistent. Please play again or quit.')
          Again()
      Check = input(f"My guess is {R}...\nType h if it is higher, l lower, or c for correct guess: ").lower()
      while Check not in ('h', 'l', 'c'):
          print(f'Invalid input, my last value was {R}')
          Check = input("Please use h-higher, l-lower, and c-correct: ").lower()
      if Check == 'h':
          x = R - 1
      elif Check == 'l':
          low = R + 1
      elif low != high:
          print(f"My guess is {R}")
  Again()
  print('\nYieeeeey, I have guessed correctly!!!!')
def Again():
   A = input('\nDo you want to play again? y or n: ').lower()
   while A not in ['y', 'n']:
       A = input('Invalid entry, please type y for yes and n for no: ')
   if A == 'y':
       try:
           x = int(input('Please provide the max number of your range (e.g. 10): '))
       except:
           x = 10
       CG(x)
   else:
       print('Bye, see you another time!')
       exit()
CG(x)