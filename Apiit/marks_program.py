subject1 =int(input("Enter the first marks?"))
subject2 =int(input("Enter the second marks?"))
subject3 =int(input("Enter the third marks?"))

total = subject1 + subject2 +subject3
avg = total/3
print(total)
print(avg)

if 75 <= avg <= 100 :
    print("your grade is A")
elif 65 <= avg <= 75 :
    print("your grade is B")
elif 55 <= avg<= 65 :
    print("your grade is C")
elif 45 <= avg < 55 :
    print("your grade is S")
else:
    print("you are fail")

