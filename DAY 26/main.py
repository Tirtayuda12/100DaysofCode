# LIST COMPREHENSION

# numbers = [1,2,3]
# new_numbers = [item*item for item in numbers]
# print(new_numbers)

# name = "Tirta"
# letter_list =[letter for letter in name]
# print(letter_list)

# new_list = [item*2 for item in range(1,5)]
# print(new_list)

# Conditional list comprehension

# names = ["Tirta","Yuda","Alief","Nadhifi","Phillia",'Juan']

# long_names = [name.upper() for name in names if len(name)>5]

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(number) for number in list_of_strings]
# result = [number for number in numbers if number%2 == 0]
# print(result)

# with open('file1.txt','r') as file1:
#     list1 = file1.readlines()

# with open('file2.txt','r') as file2:
#     list2 = file2.readlines()

# print(list1 in list2)

# import random
# names = ["Tirta","Yuda","Alief","Nadhifi","Phillia",'Juan']

# student_score = {student:random.randint(10,100) for student in names}
# passed_students = {student:score for (student, score) in student_score.items() if score >=60}
# print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = sentence.split()
result = {sentences:len(sentences) for sentences in sentence}
print(result)