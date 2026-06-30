from datetime import datetime, timedelta
date_string = "2024-12-25"
format_string = "%Y-%m-%d"

datetime_object = datetime.strptime(date_string, format_string)
date_object = datetime_object.date()

print(date_object)
print(type(date_object))

d = date_object - timedelta(days=1)
print(d)
print(type(d))
