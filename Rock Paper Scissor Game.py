import random
# r>s, s>p, p>r
def play():
   comp = random.choice(['r', 'p', 'c'])
   print(comp)
   usr = input("Type r for rock, p for paper, and s for scissor: ")
   if usr == comp:
       #return 'It\'s a tie'
       print('It\'s a tie!!!')
   elif win(usr, comp):
       #return 'You won'
       print('You won!!!')
   #return "You lost"
   else:
       print('You lost!!!')
def win(u, c):
   if (u == 'r' and c == 's') or (u == 's' and c == 'p') \
           or (u == 'p' and c == 'r'):
       return True
play()
