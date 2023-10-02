def bi_search(l, r, arr, x):
    #l is start
    #r is len
    #x is value
    #arr is
    #findmiddle
    new_arr= arr
    if l <= r :
        mid = l + (r - l) // 2
        if arr[mid] == x:
            print("equal")
            return True
        elif arr[mid] < x:
            print("most")
            return bi_search(mid+1,r,new_arr,x)
        else:
            print("less")
            return bi_search(l,mid-1,new_arr,x)
    else:
         return False
    

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))