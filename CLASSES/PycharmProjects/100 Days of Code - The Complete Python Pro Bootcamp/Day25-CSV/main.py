#1026-2025 Day25

#below works but "dirty"
# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
# print(data)

# temperatures=[]
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data)) # <class 'pandas.core.frame.DataFrame'>
# print(data["temp"])
# print(type(data["temp"])) #<class 'pandas.core.series.Series'>
# data_dict = data.to_dict()
# print(data_dict)
#
# # Panda converts Series to list
# temp_list=data["temp"].to_list()
# print(temp_list)
# average = sum(temp_list)/len(temp_list)
# print(f"Average temp {average}")
#
# # Panda has computations [baked in] e.g. mean, mode, max
# print(data["temp"].mean())
# print(f"Max temp: {data["temp"].max()}")
#
# print(data["condition"])
# print(data.condition)

# return row of data for Monday
# print(data[data.day == "Monday"])
#
# # return row of data for maximum temperature
# print("max temp day below")
# print(data[data.temp == data.temp.max()])

# return Monday's temp in F
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print(monday_temp)
# print(monday_temp * 9/5 +32)

#Create dataframe from scratch
# data_dict = {
#     "students" : ["Amy" , "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# my_df = pandas.DataFrame(data_dict)
# print(my_df)
# print(type(my_df))
#
# #Convert DF to CSV file from [thin air!]
# my_df.to_csv("new_data.csv")


# GOAL: create CSV file of squirrels colors from RAW squirrel data
import pandas
#Create DataFrame from CSV
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#Create separate DataFrame for each Color
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels  = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

#Create var for each total
gray_squirrels_count = len(gray_squirrels)
red_squirrels_count = len(red_squirrels)
black_squirrels_count = len(black_squirrels)

#Create a data_dict, note: vars w/o f{string}
data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

#Create a DF from data dictionary
squirrel_data_frame = pandas.DataFrame(data_dict)
#Create CSV from newly created DF
squirrel_data_frame.to_csv("squirrel_count.csv")


