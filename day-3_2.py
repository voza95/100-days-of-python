year = int(input("Which year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a Leap year")
        else:
            print("This is not a Leap")    
    else:
        print("This is a Leap")
else:
    print("This is not a Leap")