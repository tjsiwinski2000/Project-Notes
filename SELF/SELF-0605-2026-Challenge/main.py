# Imagine your server generates a messy text log of user actions. Each line looks like this:
# "2026-06-05 14:32:01 [INFO] User: jsmith_99 logged_in successfully"
# "2026-06-05 14:35:22 [ERROR] User: amartinez failed_login password_error"

# Your task is to write a function extract_users(log_data) that takes a multi-line string of logs and returns a list of unique usernames that experienced an [ERROR].


def log_parser(input):
    count=1
    #declare a set
    users=set()
    for line in input.split('\n'):
        if '[ERROR]' in line:
            # divide line in half e.g. User: alex_g failed_login database_timeout
            temp = line.split('[ERROR]')[1]
            # username is second element 
            user = temp.split()[1]
            print(f'{count} : {temp}')
            print(f'user: {user}')
            users.add(user)
            count +=1
    return list(users)
    
raw_logs = """
2026-06-05 14:32:01 [INFO] User: jsmith_99 logged_in successfully
2026-06-05 14:33:10 [ERROR] User: alex_g failed_login database_timeout
2026-06-05 14:35:22 [ERROR] User: amartinez failed_login password_error
2026-06-05 14:36:00 [INFO] User: alex_g logged_in successfully
2026-06-05 14:38:15 [ERROR] User: alex_g failed_login password_error
"""

print(f"users with errors = {log_parser(raw_logs)}")

#LESSONS LEARNED
# To make your function reliable, use .split() without arguments. 
# This automatically groups any amount of consecutive whitespace and strips leading/trailing spaces. 
# You can also add a quick guard clause to skip empty lines.
# Here is the robust, corrected version of your function

# NEED TO REVEIW THIS
def extract_users_fast(log_data):
    return list({line.split()[4] for line in log_data.strip().split('\n') if '[ERROR]' in line})

