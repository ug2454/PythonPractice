helps = 'help'
isCarStarted = False
isCarStopped = False
userInput = ''
while True:
    userInput = input('>').lower()
    if helps == userInput:
        print('''
start - to start the car
stop - to stop the car 
quit - to exit
        ''')
    elif userInput == "start":
        if isCarStarted:
            print('car is already started. it doesnt make sense to start it again')
        else:
            print('car is started ... ready to go')
            isCarStarted=True
    elif userInput == "stop":
        if isCarStopped:
            print('car is already stopped. what are you doing!')
        else:
            print('car is stopped')
            isCarStopped=True
    elif userInput == "quit":
        break
    else:
        print("i don't know that")
