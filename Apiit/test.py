name = "Muditha Hakmana"
age = "20"
new = True

print(f"patient name {name} and the age is {age} years old. And he is a new {new}")

num1 = float(input("enter a number"))
num2 = float(input("enter the second number"))

sum= num1+num2
print(sum)

weight = float(input("what is your weight"))
type = str.upper(input("kg or l"))

if type == "K":
    print(weight*2.2)
elif type == "L":
    print(weight/2.2)

else:
    print("can not convert")

#----------------------------------------------
#while loop
i=1
while i<=5 :
    print(i)
    i= i+1

#------------------------------------
#for loop

number = [1,2,3,4,5]
for item in number:
    print(item)





