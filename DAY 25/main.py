# with open('weather_data.csv','r') as csv_file:
#     data = csv_file.readlines()
#     print(data)

# import csv

# with open('weather_data.csv', 'r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv('weather_data.csv')

# print(data['temp'])
# pandas dataframe data types
# data_dict = data.to_dict()
# print(data_dict)

# pandas data series data types
# data_temp= data['temp']
# print(data[data_temp == 14].temp.to_list())
# print(data[data.temp == max_temp])
# print(f"Average temperatur is : {max_temp}")

# Get data in row
monday = data[data.day == "Monday"]
# print(monday.temp[0])
print(data[data.day.str.lower() == "monday"])


#create dataframe from scratch
# data_dict = {
#     'students': ["Mulyono",'Biden','Tirta'],
#     'scores': [76,56, 100]
# }

# data = pandas.DataFrame(data_dict)

# data.to_csv('New_data.csv')


# take the squirrel color data and calculate the sum of each color of grey, red and blue. Then make it to new dataframe
# import pandas

# squirrel = pandas.read_csv('2018_Central_Park_Squirrel_Census.csv')

# squirrel_color = squirrel['Primary Fur Color'].to_list()
# squirrel_gray = squirrel_color.count('Gray')
# squirrel_red = squirrel_color.count('Cinnamon')
# squirrel_black = squirrel_color.count('Black')
# print(squirrel_gray)
# print(squirrel_red)
# print(squirrel_black)
# squirrel_count = {
#     'Fur Color': ['grey','red','black'],
#     'Count':[squirrel_gray,squirrel_red,squirrel_black]
# }

# new_dataframe = pandas.DataFrame(squirrel_count)
# new_dataframe.to_csv("Squirrell.csv")

