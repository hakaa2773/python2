weight = float(input("what is your weight?  "))
unit = input("(L) bs or (K)g:")

if unit.upper() == "L" :
   converted= (weight)*0.45
   print(f"you are {converted} KG")
else:
   converted= (weight)/0.45
   print(f"you are{converted} pounds")

