#downward star
for i in range (1,5):
    for j in range(1,6-i):
        print("*",end="")
    print()
#row star
for i in range (1,5):
    for j in range(1,6+i):
        print("*",end="")
    print()
#downword number
for i in range (1,5):
    for j in range(i):
        print(i,end='')
    print('')
#diffrent downward number
rows = int(input("Enter the number of rows: "))   
for i in range(1, rows+1):  
    for j in range(1, i + 1):  
        print(j, end=' ')  
    print("")
