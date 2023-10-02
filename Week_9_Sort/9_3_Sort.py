def checkIndex(arr_sort,check_num,index_check=0):
    i = index_check
    if i < len(arr_sort):
        if arr_sort == []:
            return 0
        elif arr_sort[i] >= check_num:
            return i
        elif arr_sort[i] < check_num:
            return checkIndex(arr_sort,check_num,i+1)
    else:
        return i
    

def readyInsertionSort(arr_old,size,arr_sort=[],x=0):
    list_sort = arr_sort
    if size != 0:
        item= arr_old.pop(0)
        index_push = checkIndex(list_sort,item)
        list_sort.insert(index_push,item)
        if x != 0 :
            if arr_old != []:
                print(f"insert {item} at index {index_push} : {list_sort} {arr_old}")
            else:
                print(f"insert {item} at index {index_push} : {list_sort}")
            return readyInsertionSort(arr_old,len(arr_old),list_sort,x+1)
        return readyInsertionSort(arr_old,len(arr_old),list_sort,x+1)
    else:
        print("sorted")
        return list_sort
        


message = list(map(int,input("Enter Input : ").split()))
size = len(message)
arr_sort = []
sort_list = readyInsertionSort(message,size)
print(sort_list)
