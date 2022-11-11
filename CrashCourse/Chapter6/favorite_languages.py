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

