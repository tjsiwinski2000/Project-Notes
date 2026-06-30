#✅ print average of selected student 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    #debug print(student_marks)
    #debug print(type(student_marks))
    
    # create list of grades for student named in query_name
    selected_grades = student_marks[query_name]
    # determine avg , fix to two decimals
    average_selected_grades = sum(selected_grades) / len(selected_grades)
    average_selected_grades = "{:.2f}".format(average_selected_grades)
    # output avg, fixed two decimals
    print(average_selected_grades)
    