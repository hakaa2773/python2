customer = {
    "name" : "muditha hakmana",
    "age" : 30,
    "is verified":True
}
print(customer["name"])

#----------------------------------
phone =input("phone number?")
num ={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output =""
for ch in phone:
   output += num.get(ch, "!")+""
print(output)