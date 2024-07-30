def Black_or_Red(PeopleColor):
    import random
    WinNum = random.randint(0, 36)
    RedNum = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    if WinNum in RedNum:
        WinColor = "red"
        WinColor_return = 'Красное'
    elif WinNum != 0:
        WinColor = "black"
        WinColor_return = 'Черное'
    else:
        WinColor = "zero"
        WinColor_return = 'Zero'
    if WinColor == PeopleColor:
        return True, WinNum, WinColor_return
    else:
        return False, WinNum, WinColor_return
