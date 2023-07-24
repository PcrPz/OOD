

def findzerosum(numList, checknum, result):
    if len(checknum) == 3 and sum(checknum) == 0 and set(checknum) not in [set(x) for x in result]:
        checknum.sort()
        result.append(checknum)
        return
    elif len(checknum) == 3 or not numList:
        return
    
    findzerosum(numList[1:], checknum + [numList[0]], result)
    findzerosum(numList[1:], checknum, result)
numpast = [int(x) for x in input('Enter Your List : ').split()]
result = []
checknum = []
if len(numpast) < 3:
        print('Array Input Length Must More Than 2')
else:
    findzerosum(numpast, checknum, result)
    print(result)