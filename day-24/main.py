# # import csv
#
# # with open('weather_data.csv', mode='r') as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for line in data:
# #         if line[1] != 'temp':
# #             temperatures.append(int(line[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# temp_list = data["temp"].tolist()
# # print(temp_list)
#
# # average_temp = sum(temp_list) / len(temp_list)
# # print(average_temp)
#
# # average_temperature = data["temp"].mean()
# # print(average_temperature)
#
# # max_temp = data["temp"].max()
# # print(max_temp)
#
# # print(data[data["temp"] == data["temp"].max()])
#
# # monday = data[data.day == "Monday"]
# # monday_temp_fahr = (monday.temp * 9 / 5) + 32
# # print(monday_temp_fahr)
#
# data_dict = {
#     "students": ["Amy", "Brian", "Angela"],
#     "score": [100, 57, 95]
# }
#
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# new_data.to_csv("new_data.csv")

import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")
grouped_data = data.groupby(['Primary Fur Color']).size().reset_index(name='Count')
grouped_data.to_csv("Grouped_Squirrel_Data")