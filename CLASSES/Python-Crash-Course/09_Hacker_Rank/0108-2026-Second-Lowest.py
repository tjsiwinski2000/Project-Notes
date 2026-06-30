#✅ 0108-2025 find students with second lowest score 
my_list= []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([name,score])
# One. Build list logic 
#debug print(my_list)

# Two. create list of all scores
score_list =[]
for records in my_list:
    score_list.append(records[1])

# Three. determine minimum score and remove it from the list, accomodate dups
min_score = min(score_list)
while min_score in score_list:
    score_list.remove(min_score)
#debug print(score_list)

# Four determine next minimum which is the second lowest
second_min_score = min(score_list)
#debug print(second_min_score)

# Five. return list of names with a specific score
out_list = [item[0] for item in my_list if item[1] == second_min_score]

# Six. output names alpha sorted, one line per name
for student in (sorted(out_list)):
    print(student)



# Example input
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# -- lowest grade is 37.2 , second lowest is 37.21  (Berry and Harry) return 
# -- names only alpha sorted
# Example output
# Berry
# Harry