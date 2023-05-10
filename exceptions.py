#how to handling error inpython
try:
    age =int (input("age: "))
    income = 2000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("age can not be 0..")
except ValueError:
    print("invalid value")
