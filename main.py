rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
mychoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

if mychoice >= 3 or mychoice < 0:
  print("Wrong input you lose")
else: 
  if mychoice == 0:
     print(rock)
  elif mychoice == 1:
     print(paper)
  elif mychoice == 2:
     print(scissors)
  
  
  
  
  PC_choice = random.randint(0,2)
  print ("Computer chose")
    
  
  if PC_choice == 0:
     print(rock)
  if PC_choice == 1:
     print(paper)
  if PC_choice == 2:
     print(scissors)
  
  if mychoice == 0 and PC_choice == 0:
    print ("Its a draw")
  elif mychoice == 0 and PC_choice == 1:
    print(" You lose")
  elif mychoice == 0 and PC_choice == 2:
    print(" You Win")
  elif mychoice == 1 and PC_choice == 0:
    print(" You Win")
  elif mychoice == 1 and PC_choice == 1:
    print(" Its a draw")
  elif mychoice == 1 and PC_choice == 2:
    print(" You lose")
  elif mychoice == 2 and PC_choice == 0:
   print(" You lose")
  elif mychoice == 2 and PC_choice == 1:
    print(" You Win")
  elif mychoice == 2 and PC_choice == 2:
    print(" Its a draw")
