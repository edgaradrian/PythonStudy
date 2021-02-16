
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["no-key"])
except FileNotFoundError:
    print("There was an error")
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    print("Complete!")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

