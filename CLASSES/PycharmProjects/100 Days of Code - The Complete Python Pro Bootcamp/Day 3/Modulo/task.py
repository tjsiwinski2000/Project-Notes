number_input=int(input("Please enter a number\n"))
print(f"You entered {number_input}")
if (number_input % 2) == 0:
    print(f"{number_input} is even.")
else:
    print(f"{number_input} is odd.")