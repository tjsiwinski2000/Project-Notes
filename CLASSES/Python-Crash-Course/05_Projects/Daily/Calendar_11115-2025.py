# Show calendar , temperatures / open top three articles / coppy paste list
import calendar
import requests 
import pyperclip
from tkinter import messagebox
from datetime import datetime
import TopThreeHackerNews #0115-2026
import find_aws_users

def Get_Temp(URL):
    response = requests.get(URL)
    data = response.json()
    return data["current"]["temp_f"]

# determine current month, year
today = datetime.today()

year = datetime.today().year
month = datetime.today().month

# --- 1. Display Calendar for a Specific Month ---
# print(f"## 📅 Calendar for {calendar.month_name[month]} {year} ##")
# print("---")

# # --- 2. Display Calendar for the Entire Year ---
# print("## 🗓️ Full Year Calendar for 2025 ##")
# print("---")
# # calendar.calendar() returns a multiline string for the entire year's calendar
# year_calendar = calendar.calendar(year)
# print(year_calendar)
URL_SA ="http://api.weatherapi.com/v1/current.json?key=02d8de7fa6594eefb81213151242011&q=78247&aqi=no"
URL_SD ="http://api.weatherapi.com/v1/current.json?key=02d8de7fa6594eefb81213151242011&q=92101&aqi=no"
URL_BR ="http://api.weatherapi.com/v1/current.json?key=02d8de7fa6594eefb81213151242011&q=11235&aqi=no"

response = requests.get(URL_SA)
data = response.json()
#clear screena
print('\n'*10)
print('='*60)


my_copy_list=[]
file_path = "C:/Users/TJ/source/repos/Project-Notes/SELF/SELF-POSH-DESK-10102025/desktop2025.txt"
with open(file_path ) as f1:
    for line in f1:
        my_copy_list.append(line)
        
        
count=0
quit = False

while quit == False:
    count=0
    total_lines =""
    for line in my_copy_list:
        #print(f"{count}.{line}") 11-21-2025 adds extr CRLF
        total_lines +=f"{count}.{line}"
        count +=1
    
    print(total_lines)   
    choice = input("Enter the number of your choice please\n")
    # capture choice non-numeric / number too high
    if choice == str(99):
        quit= True
    else:
        try:
            pyperclip.copy(my_copy_list[int(choice)])
        except ValueError:
            print(f"Please enter a number from 0 - {len(my_copy_list)-1}") #11-21-2025 msgbox might be better , msg gets lost 
            messagebox.showwarning(title="Warning", message="Please enter a number ")
        except IndexError:
            print(f"Please enter a number from 0 - {len(my_copy_list)-1}") #11-21-2025 msgbox might be better , msg gets lost 
            messagebox.showinfo(title="oops", message="No Data File Found")
#Open Three Most Popular Articles 
TopThreeHackerNews.main_function()  
print('='*60)
# calendar.month() returns a multiline string for the month's calendar
month_calendar = calendar.month(year, month)
print(month_calendar)
# Print temperatures of favorite cities    
print(f'San Antonio {Get_Temp(URL_SA)} || San Diego {Get_Temp(URL_SD)} || Brooklyn {Get_Temp(URL_BR)}')
print('='*60)
find_aws_users.main_function()


