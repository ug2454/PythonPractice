numbers =[5,2,1,1,7,4]
numbers1 = [2,2,4,6,3,4,6,1]
numbers.insert(3,20)
numbers.remove(5)
numbers.pop()
print(numbers.index(2))
print(1 in numbers)
print(numbers.count(1))
print(numbers.sort())
numbers2 = numbers.copy()
print(numbers)
print(numbers2)

uniques=[]
for number in numbers1:
    if number not in uniques:
        uniques.append(number)
print(uniques)