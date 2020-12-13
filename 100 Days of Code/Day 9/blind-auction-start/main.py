from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

other_users = True
people = {}

while other_users:
  name = input("What's your name? ")
  bid = int(input("What's your bid? "))
  people[name] = bid
  are_there = input("Are there other users 'yes' or 'no'? ")
  if are_there == "yes":
    clear()
  else:
    other_users = False

winner = {}
max_user = ""
max_bid = 0
for person in people:
  if people[person] > max_bid:
    max_bid = people[person]
    max_user = person
winner[max_user] = max_bid

print(winner)
