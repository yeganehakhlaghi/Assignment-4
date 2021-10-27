num = int(input())
r = [None for _ in range(num)]
def fib(num):
    if num == 0:
        return num
    elif num == 1:
        return num
    else:
       return fib(num - 1) + fib(num - 2)
for num  in range(num):
    r[num] = fib(num)
    print(r[num],end=", ")
print("\b\b",end=" ")
print("")