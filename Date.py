dates = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("Enter a date in the format YYYY MM DD")
while True:
    inputString = input()
    try:
        year, month, day = inputString.split(" ")
        if (int(month) < 3 ):
            month=month+12
            year=year-1
        dateCode = int((13*int(month)+3)/5 + int(day) + int(year) +int(year)/4 - int(year)/100 + int(year)/400) % 7
        print(day + " / " + month + " / " + year + " is a " + dates[dateCode])
    except:
        print("Error: Invalid date format")