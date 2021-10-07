# 1,1,2,3,5,8,

# First method
def fibonacci(num):

    if num<=1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

for i in range(1,8):
    {
        print(fibonacci(i), end=" ")
    }

print()

# Next method

list=[]
def fibonacci_series(previous_num, current_num, total_num):
    if len(list)<total_num:
        # print(current_num)
        list.append(current_num)
        return fibonacci_series(current_num, previous_num+current_num, total_num)

fibonacci_series(0, 1, 7)

print(", ".join(map(str,list)))
# print(' '.join(list))
