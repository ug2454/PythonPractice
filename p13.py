phone = input('Phone: ')


digitsMap = {
    "0":"Zero",
    "1": "One",
    "2": "Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
output=""
for i in phone:
    output=output+digitsMap[i] + " "
print(output)