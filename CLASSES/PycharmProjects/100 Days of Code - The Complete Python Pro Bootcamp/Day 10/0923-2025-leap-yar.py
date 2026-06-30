def is_leap_year(year):
    """ determine if year passed is leap True or not False"""
    if year % 4 ==0:
        Divisible_4 = True
    else:
        Divisible_4 = False
    if year % 100==0:
        Divisible_100 = True
    else:
        Divisible_100 = False
    if year % 400 == 0:
        Divisible_400 = True
    else:
        Divisible_400 = False
    if Divisible_4 == True and Divisible_100 == False:
        return True
    elif Divisible_4 == True and Divisible_100 ==  True and Divisible_400 == True:
        return  True
    else:
        return False

print(f"year 2000 is leap:{is_leap_year(2000)}")
print(f"year 2024 is leap:{is_leap_year(2024)}")
print(f"year 2023 is leap:{is_leap_year(2023)}")
print(f"year 2020 is leap:{is_leap_year(2020)}")
print(f"year 2019 is leap:{is_leap_year(2019)}")
print(f"year 2018 is leap:{is_leap_year(2018)}")
print(f"year 1000 is leap:{is_leap_year(1000)}")
print(f"year 1200 is leap:{is_leap_year(1200)}")