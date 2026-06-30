import random
report_problem = ""
report_solution = ""
report=""
def generate_math_problem(max):
    # Randomly choose an operation
    operation = random.choice(['+', '-', '*', '/'])
    

    # Generate two random numbers
    num1 = random.randint(-1 * max, max)
    num2 = random.randint(-1 * max, max)

    # Make sure we don't divide by zero
    if operation == '/' and num2 == 0:
        num2 = random.randint(1, 100)

    # Create the problem based on the operation
    if operation == '+':
        problem = f"{num1} + {num2} = "
        solution = num1 + num2
    elif operation == '-':
        problem = f"{num1} - {num2} = "
        solution = num1 - num2
    elif operation == '*':
        problem = f"{num1} * {num2} = "
        solution = num1 * num2
    elif operation == '/':
        num1 = num1 * num2
        problem = f"{num1} / {num2} = "
        solution = round(num1 / num2, 2)  # Rounded to 2 decimal places

    return problem, solution

# Example usage
for _ in range(10):  # Generate 5 random math problems
    problem, solution = generate_math_problem(5)
    report += str(problem) + "," + str(solution)+";"

    #print(problem)
    #print(f"Answer: {solution}\n")

print(report)
