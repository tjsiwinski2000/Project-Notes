try:
    file = open("foo.txt")
except FileNotFoundError:
    file = open("foo.txt", "w")
    file.write("monkey meat")
    print("created file")
    
my_dict = {"batman": "Bruce Wayne"}
try:
    print(my_dict["flash"])
except KeyError as error_message:
    print(f"The key {error_message} does not exists.")