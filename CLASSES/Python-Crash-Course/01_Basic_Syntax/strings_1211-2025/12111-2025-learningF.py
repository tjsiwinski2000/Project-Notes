while 1==1:
    number_entered = input("Please enter a number\n")
    number_entered2 = input("Please enter a second number\n")
    try:
        number_entered = int(number_entered)
        number_entered2 = int(number_entered2)
    except ValueError:
        print("Next time pls enter a number.")
    else:
        print(f"The sum of {number_entered} and {number_entered2} is: {number_entered + number_entered2}")