favorite_languages = {
    'adrian': 'objective-c',
    'dulce': 'c',
    'abril': 'rust',
    'alissa': 'kotlin'
}

language = favorite_languages['dulce'].title()
print(f"Dulce's favorite language is {language}")

#Using get() to Access Values
alien_51 = {'color': 'cyan', 'speed': 'slow'}

point_value = alien_51.get('points', 'No point value assigned.')
print(point_value)

#Looping Through All Key-Value Pairs
for name, language_loop in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language_loop.title()}")

#Looping Through All the Keys in a Dictionary
for name_key in favorite_languages.keys():
    print(name_key.title())

sisters = ['abril', 'alissa']
for name_loop_key in favorite_languages.keys():
    print(f"Hola {name_loop_key.title()}")

    if name_loop_key in sisters:
        lang = favorite_languages[name_loop_key].title()
        print(f"\t{name_loop_key.title()}, I see you love {lang.title()}")    


#Looping Through a Dictionary’s Keys in a Particular Order
for name_sorted in sorted(favorite_languages.keys()):
    print(f"{name_sorted.title()}, thank you for taking the poll")
