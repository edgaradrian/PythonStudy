file = open("my_file.txt")
content = file.read()
print(content)
file.close()

with open("my_file.txt", mode="w") as file:
    file.write("New text.")

with open("my_file.txt") as file:
    content = file.read()
    print(content)

with open("new_file.txt", mode="w") as file:
    file.write("New text.")

with open("new_file.txt") as file:
    content = file.read()
    print(content)
