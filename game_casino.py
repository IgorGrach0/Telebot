def Black_or_Red(PeopleColor):
    import random
    WinNum = random.randint(0, 36)
    print(WinNum)
    RedNum = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    if WinNum in RedNum:
        WinColor = "Red"
    elif WinNum != 0:
        WinColor = "Black"
    else:
        WinColor = "Zero"

    if WinColor == PeopleColor:
        return True, WinNum
    else:
        return False, WinNum
print(Black_or_Red('Black'))