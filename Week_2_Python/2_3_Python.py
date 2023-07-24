print("*** New Range ***")
argu = [float(x) for x in input('Enter Input : ').split()]

def range(arg1, arg2=None, arg3=1):
    result = []
    if arg2 == None:
        start = 0.0
        stop = arg1
        while start < stop:
            result.append(start)
            start+=1
    else:
        start = arg1
        stop = arg2
        step = arg3
        while start < stop:
            result.append(start)
            start+=step
    return [round(x, 3) for x in result]


print('(', end='')
print(*range(*argu), sep=', ', end='')
print(')')