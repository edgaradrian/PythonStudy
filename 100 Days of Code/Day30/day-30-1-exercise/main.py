fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("No valid index. Max index 2")
    else:
        print(fruit + " pie")
    finally:
        new_index = int(input("Try again. Index? "))
        make_pie(new_index)

make_pie(4)