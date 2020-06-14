import datetime

name = input('Enter Name: ')
age = int(input('Enter Age: '))


yeartoday = datetime.datetime.now()
year = (yeartoday.year-age)+100
number = int(input('Enter a number: '))
count=0
while count<number:
    print(f'{name} will turn to 100 years old in {year}')
    count+=1

