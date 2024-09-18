import random
def G(x):
   while True:
       R = random.randint(1, x)
       try:
           G = int(input(f"Please guess a random positive integer from 1 - {x}: "))
           while G != R:
               if G not in [i + 1 for i in range(x)]:
                   G = int(input("Sorry your guess is BEYOND RANGE, please try again: "))
               elif G < R:
                   G = int(input("Sorry your guess is LOWER, please try again: "))
               else:
                   G = int(input("Sorry your guess is HIGHER, please try again: "))
       except:
           G = -1
       if G == -1:
           print("Invalid value, try again!!")
       else:
           print("Congratulations, you have guessed right!!!")
           Continue = input("Do you wish to play again? y for yes and any value for no: ")
           if Continue.lower() == 'y':
               continue
           else:
               break
G(10)