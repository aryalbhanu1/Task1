#Input age
age = int(input("enter age : "))

#condition to check voting eligibility
if age>=18:
    status="eligible"
else:
    status="not eligible"

print("you are",status,"for vote")