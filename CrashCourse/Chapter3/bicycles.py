from email import message


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