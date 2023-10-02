def insertionSort(arr_old):
    for i in range(1,len(arr_old)):
        iEle = arr_old[i]
        for j in range(i,-1,-1):
            if iEle <  arr_old[j-1] and j>0:
                arr_old[j] = arr_old[j-1]
            else:
                arr_old[j] = iEle
                print(f"Round {i} {arr_old}")
                break
    return(arr_old)
    
inp = list(map(int, input("Enter list for number: ").split(",")))
print("Before sort:", inp)
insertionSort(inp)
print("After sort:", inp)