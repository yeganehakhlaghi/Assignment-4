row=input("Enter number of the rows: ")
column=input("Enter number of the columns: ")
#--------------------------------------------
for num1 in range(row):
    if num1 % 2 == 0:
        for num2 in range(column):
            if num2 % 2 == 0 or num2 == 0:
                print('# ', end='')
            elif num2 % 2 == 1:
                print('* ', end='')
    elif num1 % 2 == 1:
        for num2 in range(column):
            if num2 % 2 == 0 or num2 == 0:
                print('* ', end='')
            elif num2 % 2 == 1:
                print('# ', end='')
    print()
