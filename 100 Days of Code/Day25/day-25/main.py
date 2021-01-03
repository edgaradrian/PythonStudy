#import csv

#with open("weather_data.csv") as csv_file:
#    data = csv.reader(csv_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(int(sum(temp_list)/len(temp_list)))
print(data["temp"].mean())

print(data.temp.max())

#Data in rows
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(int(monday.temp))

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Jones", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")