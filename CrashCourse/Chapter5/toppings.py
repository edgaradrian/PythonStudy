requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'extra cheese' in requested_toppings:
    print("Adding cheese")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni")

print("\nFinished making your pizza!")