# The "Tribonacci sequence" challenge is a twist on the famous Fibonacci sequence, where each number is the sum of the preceding three numbers.

# For example, 0, 1, 1, 2, 4, 7 …

def tribonacci(n):
    n = int(n)
    if n ==1:
        return 0
    elif n ==2:
        return 1
    elif n == 3:
        return 1
    else:
        # n > = 4
        final_value = 2
        my_list = [0,1,1]
        for i in range(2,n-1):
            next_value = my_list[i] +my_list[i-1] +my_list[i-2]
            my_list.append(next_value)
            print(f'iteration:{str(i)}\tmy_list:{my_list}')
        return(my_list[-1])
        
print(tribonacci(5))