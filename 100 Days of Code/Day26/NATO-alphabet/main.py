student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

import pandas

data_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
student_data_frame = pandas.DataFrame(student_dict)

users_nato = []

for (index, row) in student_data_frame.iterrows():
    users_dict = {}
    for user_letter in row.student:
        row_csv = data_csv[data_csv.letter == user_letter.upper()]
        users_dict[user_letter] = row_csv.iloc[0]["code"]
        users_nato.append(users_dict)
print(users_nato)

