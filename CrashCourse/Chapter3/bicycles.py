from os import remove


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#To access an element in a list
print(bicycles[0])

#To look more presentable
print(bicycles[0].title())

#The following asks for the bicycles at index 1 and index 3:
print(bicycles[1])
print(bicycles[3])

#the last element in a list
print(bicycles[-1])

#pulling the first bicycle from the list and composing a message using that value
message = f"The first bicycle is {bicycles[0].title()}"
print(message)

#Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding elements to the end of a List
motorcycles.append('honda')
print(motorcycles)

motorcycles2 = []
motorcycles2.append('ducati')
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)

#Inserting elements into a List
motorcycles.insert(0, 'Kawasaki')
print(motorcycles)

#Removing an item using the 'del' statement
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

#Removing an item using the pop() method
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

#Preparing next exercise
motorcycles.append('honda')
motorcycles.insert(0, 'Kawasaki')
print(motorcycles)

#Popping items from any positionin a List
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

#Removing an item by value
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

motorcycles.append('Kawasaki')
motorcycles.insert(0, 'honda')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")

