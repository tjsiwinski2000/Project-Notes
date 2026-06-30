print("Welcome to the tip calculator!")
total_bill=input("What was the total bill?")
tip_percent=input("How much tip would you like to give? 10, 12, or 15?")
num_people=input("How many people to split the bill?")
total_tip= float(total_bill) * float(tip_percent)/100
each_person_pay=(float(total_bill)+float(total_tip))/float(num_people)
print(f"Each person should pay: ${round(each_person_pay,2)}")