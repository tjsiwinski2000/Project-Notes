#CrashCourse p142 ex 8.7
def make_album(name,title,song_count=None):
    album_dict ={}
    if song_count:
        album_dict[name] = f"Album Title:{title}, Songs: {song_count}"
        return album_dict
    elif name and title:
        album_dict[name] = f"Album Title:{title}"
    return album_dict

# print(make_album("ELO","Mr.Blue Sky"))
# print(type(make_album("ELO","Mr.Blue Sky")))
# print(make_album("Beatles","Abbey Road","12"))

group =""
while group != "quit":
    group = input("Please enter a group name or 'quit' to leave\n")
    if group == 'quit':
        continue
    title = input("Please enter an album title\n")
    songs = input("Please enter song count on the album if you know it\n")
    my_dict = make_album(group,title,songs)
    print(my_dict )
    print(type(my_dict ))
    print(my_dict[group])

print("code outside while loop")
   
    