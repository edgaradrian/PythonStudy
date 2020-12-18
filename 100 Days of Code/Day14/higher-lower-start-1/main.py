import random
from art import logo
from art import vs
from game_data import data

print(logo)


contender_two = random.choice(data)

def print_data(contender):
  contender_name = contender["name"]
  contender_descrip = contender["description"]
  contender_country = contender["country"]
  return f"{contender_name} - {contender_descrip} - {contender_country}"

is_game_over = False
score = 0

while not is_game_over:
  contender_one = contender_two
  contender_two = random.choice(data)
  
  while contender_one == contender_two:
    contender_two = random.choice(data)
  print(f"{print_data(contender_one)}")
  print(vs)
  print(f"{print_data(contender_two)}")

  selection = input("Who has more follers '1' or '2'? ")

  
  followers_one = contender_one["follower_count"]
  followers_two = contender_two["follower_count"]

  if followers_one > followers_two and selection == "1":
    print("you got it!")
    score += 1
  elif followers_one < followers_two and selection == "2":
    print("you got it!") 
    score += 0
  else:
    print("you lose")   
  print(f"Your score: {score}")
  answer = input("Do you want play again? 'Y' or 'N' ").lower()  
  if answer != "y":
    is_game_over = True