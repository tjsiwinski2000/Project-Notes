def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return float(n1) / float(n2)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

import art
print (art.logo)

def calculate(operation_choice,first_num,second_num):
    result_num= float(operations[operation_choice](first_num, second_num))
    return result_num


# first_num = float(input("What is the first number?:"))
# for op_output in operations:
#     print(op_output)
# operation_choice = input("Pick an operation:")
# second_num = float(input("What is the next number?:"))
# # output calculation
# result_num = calculate(operation_choice,first_num,second_num)
# print(f"{first_num} {operation_choice} {second_num} = {result_num }")

first_run=True
for i in range(1,10):
    if first_run == True:
        first_num = float(input("What is the first number?:"))
    else:
        next_calculation=input(f"Type 'y' to continue calculating with {result_num }, or type 'n' to start a new calculation: ")
        if next_calculation.lower()== 'y':
            first_num = result_num
        else:
            first_num = float(input("What is the first number?:"))

    for op in operations:
        print(op)

    operation_choice = input("Pick an operation:")
    second_num = float(input("What is the next number?:"))
    result_num= calculate(operation_choice,first_num,second_num)
    print(f"{first_num} {operation_choice} {second_num} = {result_num}")
    first_run = False



