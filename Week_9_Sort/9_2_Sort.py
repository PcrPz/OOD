def findmax(arr):
    return arr.index(max(arr))

def straightSort(arr,leng,leftarr):
    if leng <= 1:return arr
    else:
        temp1 = arr[findmax(leftarr)]
        temp2 = arr[leng-1]
        if temp1 == temp2:
            return straightSort(arr,leng-1,arr[0:leng-1])
        else:
            arr[findmax(leftarr)] = temp2
            arr[leng-1] = temp1

            print (f"swap {temp2} <-> {temp1} : {arr}")
            return straightSort(arr,leng-1,arr[0:leng-1])


message = list(map(int,input("Enter Input : ").split()))
leng = len(message)
check = straightSort(message,leng,message)
print(check)