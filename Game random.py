import random
winning_number=random.randint(1,100) 
guess=1
number=int(input("Enter your guess number between 1 and 100:"))
game_over=False
while not game_over:
   if number==winning_number:
      print(f"you  win !,and you guessed this number in :{guess}:times")
      game_over=True
   else:  
      if number<winning_number:
         print("your number is low")
         guess+=1
         number=int(input("Enter again number:"))
      else:
         print("your number is high")
         guess+=1
         number=int(input("Enter again number:"))
    
