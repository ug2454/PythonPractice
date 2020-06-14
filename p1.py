weight = int(input('Enter weight'))
unit = input('Enter (L)bs or (K)gs ')

if unit == "k" or unit == "K":
    weight = weight/0.45
    print(f"you are {weight} pounds")
elif unit == "l" or unit == "L":
    weight = weight*0.45
    print(f"you are {weight} kgs")