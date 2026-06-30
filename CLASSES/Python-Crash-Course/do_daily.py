#create file named todays date
import time
timestr = time.strftime("%m%d-%Y-%H%M")

file_name = timestr +"-review.py"

with open("review-list.py") as review_file:
    review_content = review_file.read()
    
with open(file_name, 'w') as daily_file:
    daily_file.write(review_content) 