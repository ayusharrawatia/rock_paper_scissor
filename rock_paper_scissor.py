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
import random
choice=input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.:")
if choice=="0":
        print(rock)
elif choice=="1":
        print(paper)
elif choice=="2":
        print(scissors)
else:
        print("Invalid Choice...!")

computer=(random.randint(0,2))
comp_choice=str(computer)

if comp_choice=="0":
        print(rock)
        if choice=="0":
            print("DRAW")
        elif choice=="1":
            print("You won..!")
        else:
            print("You Loose..")
elif comp_choice=="1":
        print(paper)
        if choice=="1":
            print("DRAW")
        elif choice=="2":
            print("You won..!")
        else:
            print("You Loose..")
else:
        print(scissors)
        if choice=="2":
            print("DRAW")
        elif choice=="0":
            print("You won..!")
        else:
            print("You Loose..")