# Dictionary

student_dict = {
    "student" : ["A", "J", "L"],
    "score" : [56, 76, 98]
}

for (key,value) in student_dict.items():
    print(key)
# student
# score

for (key,value) in student_dict.items():
    print(value)
# ['A', 'J', 'L']
# [56, 76, 98]

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#  student  score
# 0       A     56
# 1       J     76
# 2       L     98

#Loop thr. DataFrame , key shows key
for (key,value) in student_data_frame.items():
    print(key)
#student
#score

#Loop thr. DataFrame , value shows entire row, [not particularly useful]
for (key,value) in student_data_frame.items():
    print(value)
# Name: student, dtype: object
# 0    56
# 1    76
# 2    98
# Name: score, dtype: int64

#Loop thr. row of DataFrame instead of columns
for (index,row) in student_data_frame.iterrows():
    print(index)
# 0
# 1
# 2

#Loop thr. row of DataFrame instead of columns
#...each row is a panda series
for (index,row) in student_data_frame.iterrows():
    print(row)
# student     A
# score      56
# Name: 0, dtype: object
# student     J
# score      76
# Name: 1, dtype: object
# student     L
# score      98
# Name: 2, dtype: object

#Loop thr. row of DataFrame instead of columns
#...each row is a panda series
for (index,row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
# A
# 56
# J
# 76
# L
# 98