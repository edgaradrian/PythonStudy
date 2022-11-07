requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'extra cheese' in requested_toppings:
    print("Adding cheese")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings: 
    for topping in requested_toppings:
        if topping == 'green peppers':
            print("Sorry, we are out of green peppers.")
        else:
            print(f"Adding {topping}")
else:
    print("Are you sure you want a plain pizza?")

print("\nFinished making your pizza!")    