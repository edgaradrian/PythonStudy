from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def minus(n1, n2):
  return n1 - n2

def product(n1, n2):
  return n1 * n2

def division(n1, n2):
  return n1 / n2  

first_number = int(input("What's the first number? "))
print("+\n-\n*\n/\n")
operation = input("Pick an operation: ")
second_number = int(input("What's the next number? "))
result = 0
if operation == "+":
  result = add(first_number, second_number)
elif operation == "-":
  result = minus(first_number, second_number)
elif operation == "*":
  result = product(first_number, second_number)
elif operation == "/":
  result = division(first_number, second_number)

print(result)

