secretnumber = 5
tries = 1

maxTries=3
while tries<=maxTries :
    userInput = int(input('Guess: '))
    tries = tries + 1
    if userInput == secretnumber:
        print('you won')
        break
else:
    print('you lost')

