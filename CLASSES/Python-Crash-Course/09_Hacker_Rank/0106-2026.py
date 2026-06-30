def test(n):
    if n %2 != 0:
        print("Weird")
    elif n in range(2,5):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    elif n > 20:
        print("Not Weird")

     
my_list = [1,2,3,4,5,6,20,21,22]

# for num in my_list:
#     print(num)
#     test(num)

def test2(a,b):
    print(a+b)
    print(a-b)
    print(a*b)

# while True:
#     n1 =input("enter first num")
#     n2 = input("enter second num")
#     test2(int(n1), int(n2))

a=3
b=5
# print(int(a/b))
# print(float(3)/float(5))
n=5
# for count in range(0,n,1):
#     print(count**2)
