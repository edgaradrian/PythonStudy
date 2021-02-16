
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
    file.close()