#Write your code below this line 👇

def prime_checker(number):
  divisors = 0
  for n in range(number):
    if number % (n+1) == 0:
      divisors += 1
  if divisors == 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



