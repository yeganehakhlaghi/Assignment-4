num1 = int(input())
num2 = int(input())

def Table(num1,num2):
    for i in range(num1):
        for j in range(num2):
            sum = (i + 1) * (j + 1)
            if sum < 10:
                print(sum , '        │', end="")
            elif sum < 100:
                print(sum , '       │', end="")
            elif sum < 1000:
                print(sum , '      │', end="")
            elif sum < 10000:
                print(sum , '     │', end="")
            elif sum < 100000:
                print(sum , '    │', end="")
            elif sum < 1000000:
                print(sum , '   │', end="")
            elif sum < 10000000:
                print(sum , '  │', end="")
            elif sum < 100000000:
                print(sum , ' │', end="")
            elif sum < 1000000000:
                print(sum , '│', end="")
        print()
        for num in range(num2):
            print("──────────┼",end="")
        print()


Table(num1,num2)