import random

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

options = [rock, paper, scissors]
player_option = random.randrange(0,3,1)
cpu_option = random.randrange(0,3,1)
player = options[player_option]
print(f"You\n{player}")
cpu = options[cpu_option]
print(f"CPU\n{cpu}")

if player_option == cpu_option:
  print("Tie")
elif player_option <= cpu_option and (cpu_option - player_option) < 2:
  print("CPU win!")
elif cpu_option <= player_option and (player_option - cpu_option) < 2:
  print("You win")
elif cpu_option == 0 and player_option == 2:
  print("CPU win!")  
elif player_option == 0 and cpu_option == 2:
  print("You win")