PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("Input/Letters/starting_letter.docx") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_content = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/{stripped_name}.docx", mode="w") as letter:
            letter.write(new_content)
