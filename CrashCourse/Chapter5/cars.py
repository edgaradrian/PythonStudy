cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Checking case for equality
for car in cars:
    if car.lower() == 'audi':
        print(f"Este sí es un carro {car.title()}")
    else:
        print("No es un carro audi")

