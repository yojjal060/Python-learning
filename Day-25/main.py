# with open("./227 - weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("./227 - weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#


# # print(type(data))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # # while total in temp_list:
# # #     total = sum(total,0)
# # #     average = total/len(temp_list)
# # #     print(average)
# #
# # average = sum(temp_list)/len(temp_list)
# # print(average)
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# #
# # print(data["day"])
# # print(data.condition)
#
# #Get data in rows
# # print(data[data.day == "Monday"])
# # temp_max = data["temp"].max()
# # print(data[data.temp == temp_max])
#
# # monday = data[data.day == "Monday"]
# # monday_temp = int(monday.temp)
# # monday_temp_f = monday_temp * 9/5 + 32
# # print(monday_temp_f)
#
# #Create a datafram from Scratch
# data_dict = {
#     "students" : ["Amy","James","Angela"],
#     "scores" : [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("229 - 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")