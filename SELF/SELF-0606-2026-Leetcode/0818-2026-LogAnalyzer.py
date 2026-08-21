# It should return a dictionary containing:

# Total number of log entries
# Number of entries by log level (INFO, ERROR, WARNING)
# Number of errors per user
# The user with the most errors
# A set of all unique actions

# Don't use external libraries.
# Parse each log line rather than hardcoding the results.
# Handle an empty logs list.
# Try to make your solution reasonably clean and Pythonic.
# Bonus: Handle malformed log lines without crashing

logs = [
    "2026-08-18 10:01:23 INFO user=alice action=login",
    "2026-08-18 10:02:11 ERROR user=alice action=payment",
    "2026-08-18 10:03:45 INFO user=alice action=view",
    "2026-08-18 10:04:02 ERROR user=alice action=payment",
    "2026-08-18 10:05:17 WARNING user=charlie action=login",
    "2026-08-18 10:06:33 ERROR user=bob action=payment",
    "2026-08-18 10:07:01 INFO user=bob action=logout",
]

output_dict ={}
error_dict ={}
action_set=set()
info_count=0
error_count=0
warning_count=0

for entry in logs:
    line = entry.split(' ')
    print(f'Analyzing: {entry}')
    for index in range(0,len(line)):
        print(line[index])
        if index == 2:
            if line[2] == 'INFO':
                info_count +=1
            elif line[2] == 'ERROR':
                error_count +=1
                user = line[3].split('=')[1]
                error_dict[user] = error_dict.get(user,0) +1
            elif line[2] == 'WARNING':
                warning_count +=1
        if index == 4:
            current_action=line[index].split('=')[1]
            action_set.add(current_action)
            

total_count = info_count + error_count + warning_count

output_dict["total"]=total_count
output_dict["levels"]={"INFO":info_count,"ERROR":error_count,"WARNING":warning_count}
output_dict["errors_by_user"] = error_dict
output_dict["most_errors"] = max(error_dict,key=error_dict.get)
output_dict["actions"] = action_set
print(output_dict)

print('-' *30)
print(error_dict)
print(max(error_dict))
print(max(error_dict,key=error_dict.get))
# For the example above, the result should be equivalent to{
#     "total": 7,
#     "levels": {
#         "INFO": 3,
#         "ERROR": 3,
#         "WARNING": 1
#     },
#     "errors_by_user": {
#         "bob": 2,
#         "alice": 1
#     },
#     "most_errors": "bob",
#     "actions": {"login", "payment", "view", "logout"}
# }