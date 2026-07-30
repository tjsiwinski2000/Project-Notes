# The challenge: Given an integer n, print a string that alternates between the phrases "Loves me" and "Loves me not" for each number from 1 to n.

def message(n):
    for i in range(1,int(n)+1):
        if i % 2:
            print( "Loves me")
        else:
            print("Loves me not" )

message(5)
