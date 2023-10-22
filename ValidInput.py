def forMenu(value, isTypeOf, count):    #May rewrite to also return converted value.
    if isTypeOf(value):
        if int(value) > -1 and int(value) <= count or int(value) == 0:
            return True
    return False

def forInt():   #This one takes input inside itself, the one above doesn't... Room for improvement!
    while True:
        userInput = input()
        if userInput.isdecimal():
            returnValue = userInput
            break
    return int(returnValue)
