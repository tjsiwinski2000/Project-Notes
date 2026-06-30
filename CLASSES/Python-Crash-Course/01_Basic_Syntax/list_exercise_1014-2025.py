#1014-2025 python practice TJS - Python Crash Course
my_list =["Abraham Lincoln" , "Tony Lazzari", "Helen keller"]
invite_text= "I would like to invite you to dinner at my house."

  
cant_make="Abraham Lincoln"
first_alternate="Rafael Nadal"
my_list.remove(cant_make)
print(f"Updated List {my_list}")

my_list.append(first_alternate)
print(f"Updated List {my_list}")
  
n1="Michael Jordan"
n2="Hank Aaron"
n3="Babe Ruth"
my_list.insert(0,n1)
print(f"Updated List {my_list}")

middle=int(len(my_list)/2 )
print(f"middle is {middle}")
#insert n2 name into the middle of the list
my_list.insert(middle,n2)
print(f"Updated List {my_list}")

my_list.append(n3)
print(f"Updated List {my_list}")

#sorting a list 
my_list.sort()
print(f"Sorted List {my_list}")
my_list.sort(reverse=True)
print(f"Sorted List {my_list}")