age = 17
if age < 4:
    price = 0
elif age < 18:
    price = 15
elif age < 65:
    price = 25
else:
    price = 20

print(f"Your admission cost is ${price}.")