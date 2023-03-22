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

while True:

  game = input("\nDo you want to play Rock-Paper-Scissors? y/n: ").lower()

  if game == 'y':
    user = input('''
What do you choose? 

0 - rock 
1 - paper 
2 - scissors
: ''')

    list_game = [rock, paper, scissors]

    computer = random.randint(0, 2)

    if user == '0' or user == '1' or user == '2':
      print(list_game[int(user)])
      if computer >= 0 and computer < 3:
        print("\nComputer chose: ")
        print(list_game[computer] + '\n')

      if int(user) == computer:
        print("It's a draw. (◐.̃◐)")
      elif user == '0' and computer == 1:
        print("You lose. ( ◡́.◡̀)")
      elif user == '0' and computer == 2:
        print("You win! ٩(̃-̮̮̃-)۶ 🎉")
      elif user == '1' and computer == 0:
        print("You win! ٩(̃-̮̮̃-)۶ 🎉")
      elif user == '1' and computer == 2:
        print("You lose. ( ◡́.◡̀)")
      elif user == '2' and computer == 0:
        print("You lose. ( ◡́.◡̀)")
      elif user == '2' and computer == 1:
        print("You win! ٩(̃-̮̮̃-)۶ 🎉")
    elif user != '0' and user != '1' and user != '2':
      print("You typed an invalid number, you lose. •ิ.•")
  else:
    print("\n--------")
    print("Goodbye!")
    print("--------")
    break

