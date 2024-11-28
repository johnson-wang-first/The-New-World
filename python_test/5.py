Money = input("please input money:")

if Money[-3:] in ['USD', 'usd']:
    RMB = int(Money[:-3]) * 7.23
    print("{:.2f}".format(RMB))
elif Money[-3:] in ['RMB', 'rmb']:
    USD = int(Money[:-3])/7.23
    print("{:.2f}".format(USD))
else:
    print("Input error")