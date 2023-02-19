mark = []
tot = 0
print("Enter Number of Subjects: ")
subNo = int(input())
print("Enter Marks Obtained in " + str(subNo) + " Subjects: ")
for i in range(subNo):
    mark.append(input())

for i in range(subNo):
    tot = tot + int(mark[i])
avg = tot/subNo
if avg>=91 and avg<=100:
    print("Grade = A1")
elif avg>=81 and avg<91:
    print("Grade = A2")
elif avg>=71 and avg<81:
    print("Grade = B1")
elif avg>=61 and avg<71:
    print("Grade = B2")
elif avg>=51 and avg<61:
    print("Grade = C1")
elif avg>=41 and avg<51:
    print("Grade = C2")
elif avg>=33 and avg<41:
    print("Grade = D")
elif avg>=21 and avg<33:
    print("Grade = E1")
elif avg>=0 and avg<21:
    print("Grade = E2")
else:
    print("Invalid Input!")
    #to find grade