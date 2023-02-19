#converting roman number into decimal
a = input("enter the letter:")
d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
ans = 0
#using for loop method
for i in range(len(a)): 
    if i+1 != len(a) and d[a[i]]<d[a[i+1]]:
        ans = ans - d[a[i]]
        
    else:
        ans = ans + d[a[i]]  
print(ans)

