import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_total = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_total = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_total = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_total)
print(cinnamon_squirrels_total)
print(black_squirrels_total)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_total, cinnamon_squirrels_total, black_squirrels_total]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")