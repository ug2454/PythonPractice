try:
    age=int(input('age: '))
    income=20000
    risk =income/age
    print(age)
except ZeroDivisionError:
    print('cannot divide by 0')
except ValueError:
    print('Invalid Value')