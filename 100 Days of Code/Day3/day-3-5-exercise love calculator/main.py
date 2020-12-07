# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_lowercase = name1.lower() + name2.lower()
total_true = names_lowercase.count("t") + names_lowercase.count("r") + names_lowercase.count("u") + names_lowercase.count("e")
total_love = names_lowercase.count("l") + names_lowercase.count("o") + names_lowercase.count("v") + names_lowercase.count("e") 

score = (total_true * 10) + total_love

if score < 10 and score > 90:
  print(f"your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")