def forMenu(value, isTypeOf, count):
    if isTypeOf(value):
        if int(value) > 0 and int(value) <= count:
            return True
    return False

def forInt(value):
    if value.isdecimal():
        return True, value
    return False, 0
