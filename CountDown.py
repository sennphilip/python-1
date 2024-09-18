import time
while True:
   try:
       n = int(input("Type a number to count down: "))
   except:
       n = -1
   if n == -1:
       print("Please provide a correct number and let's try again!!")
   else:
       while n > 0:
           print(n)
           time.sleep(1)
           n = n - 1
       print("Go!!!!")
       continue
