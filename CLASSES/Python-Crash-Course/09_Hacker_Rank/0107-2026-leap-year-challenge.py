def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True
    if year % 4 == 0 and year % 100 == 0:
        leap = False
    if year % 4 == 0 and year % 100 == 0 and year % 400 ==0:
        leap = True

    
    return leap

# while True:
#     year = int(input())
#     print(f"year:{year} leap is: {is_leap(year)}")

# n=3
# temp=""
# for count in range(1,n+1):
#     temp += str(count)
# print(temp)

