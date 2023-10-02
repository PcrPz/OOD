def insertionSort(arr_old):
    for i in range(1,len(arr_old)):
        iEle = arr_old[i]
        for j in range(i,-1,-1):
            if iEle <  arr_old[j-1] and j>0:
                arr_old[j] = arr_old[j-1]
            else:
                arr_old[j] = iEle
                break
    return(arr_old)

def generate_subsets(original_list):
    if not original_list:
        return [[]]  # Return an empty list as the base case
    
    first_elem = original_list[0]
    rest_of_list = original_list[1:]
    
    subsets_without_first = generate_subsets(rest_of_list)
    subsets_with_first = [[first_elem] + subset for subset in subsets_without_first]
    
    return subsets_without_first + subsets_with_first

def sortsubset(subset,listSortSize =[],listSortNum =[]):
    #findmaxword
    temp1 = 0
    for x in subset:
        if len(x) >= temp1:
            temp1 = len(x)

    for i in range(1,temp1+1):
        for j in subset:
            if len(j) == i :
                listSortSize.append(j)

    #findmaxword
    temp2 = 0
    for x in listSortSize:
        if len(x) >= temp2:
            temp2 = len(x)
    #sortNum         
    for i in range(1,temp2+1):
        temp = []
        for j in listSortSize:
            if len(j) == i:
                temp.append(j)
        after = sortNum(temp)
        listSortNum+=after
    return listSortNum

def sortNum(temp):
    for i in range(1,len(temp)):
            back = temp[i]
            for j in range(i,-1,-1):
                front = temp[j-1]
                x=0
                while back[x] == front[x]:
                    x+=1
                if back[x] < front[x] and j>0:
                    temp[j] = temp[j-1]
                else:
                    temp[j] = back 
                    break
    return(temp)

                               

result,inp = input("Enter Input : ").split("/")
before = list(map(int,inp.split()))
sort_list=insertionSort(before)
sub_list = generate_subsets(sort_list)
subset_result =[]
for i in sub_list:
    if sum(i) == int(result):
        subset_result.append(i)
if subset_result == []:
    print("No Subset")
else:
    show_list = sortsubset(subset_result)
    for i in show_list:
        print(i)

