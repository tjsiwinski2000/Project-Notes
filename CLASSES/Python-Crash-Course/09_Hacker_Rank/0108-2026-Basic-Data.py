# ✅Return second highest number 
n=int(input())
arr=input().split()

my_list =[]
# strings-> int : my_list 
for n in arr:
    my_list.append(int(n))
    
max_num = max(my_list)
#print(max_num)
while max_num in my_list:
    my_list.remove(max_num)
    
print(max(my_list))
# Example Input 5  \n   2 3 6 6 5
# Exaple Output 5
# Hacker Rank had map for second imput which threw me off a bit "little things take you for a ride "