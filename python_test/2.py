a = "abcaccbb"
b1 = list(a)
b2 = list(reversed(list(a)))

def cmp(str):
    b1 = list(str)
    b2 = list(reversed(list(str)))
    if b1 == b2:
        return True
    else:
        return False

cmp(a)
    


