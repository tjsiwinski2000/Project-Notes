# find second lowest score
my_list= [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]



# create list of all scores
score_list =[]
for records in my_list:
    score_list.append(records[1])

# determine minimum score and remove it from the list
min_score = min(score_list)
while min_score in score_list:
    score_list.remove(min_score)
    
#debug 
print(score_list)

# determine next minimum which is the second lowest
second_min_score = min(score_list)
#debug 
print(second_min_score)

# return list of names with a specific score
out_list = [item[0] for item in my_list if item[1] == second_min_score]

# output names alpha sorted, one line per name
for student in (sorted(out_list)):
    print(student)
    

    

