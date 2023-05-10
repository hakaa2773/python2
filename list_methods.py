#how to add a number in the begining

#numbers = [5,6,7,8,9,3]
#numbers.insert(0,10)
#print(numbers)

#REMOVE
#numbers = [5,6,7,8,9,3]
#numbers.remove(5)
#print(numbers)


#CLEAR
#numbers = [5,6,7,8,9,3]
#numbers.clear()
#print(numbers)


#remove last number (pop)
#numbers = [5,6,7,8,9,3]
#numbers.pop()
#print(numbers)

#how to  find the index
#num =[3,4,5,6,7]
#print(num.index(5))


#remove duplicate in a  list
#append use to add number directly
numbers = [2,3,4,5,5,2,2]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


