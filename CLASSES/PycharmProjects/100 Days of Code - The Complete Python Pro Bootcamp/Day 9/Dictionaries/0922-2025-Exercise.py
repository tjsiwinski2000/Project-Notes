student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    current_grade = ""
    if student_scores[name] >= 91:
        current_grade = "Outstanding"
    elif student_scores[name] >= 81:
        current_grade = "Exceeds Expectations"
    elif student_scores[name] >= 71:
        current_grade = "Acceptable"
    else:
        current_grade = "Fail"
    student_grades[name] = current_grade

#0922-2025
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
order["main"][2]
# prints => ['Steak']
order["main"][2][0]
# prints => 'Steak'