height=float(input("enter the height in cm:"))
weight=float(input("enter the weight in kg:"))
bmi=weight/(height/100)**2
print("your body index is",bmi)
if bmi<=18.8:
    print("under weight")
if bmi<=24.9:
    print("healthy")
if bmi<=29.9:
  print("over weight")  