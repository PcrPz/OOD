def sortedAlphabet(value_dict,arr_old):
    for i in range(1,len(arr_old)):
        item = arr_old[i]
        for j in range(i,-1,-1):
            if value_dict[item] < value_dict[arr_old[j-1]] and j > 0:
                arr_old[j] = arr_old[j-1]
            else:
                arr_old[j] = item
                break
    return arr_old

inp = list(map(str, input("Enter Input : ").split()))
value_list={}
for message in inp:
    for x in message:
        if x.isalpha():
            value=ord(x)
            value_list[message] = value
            break
sort_list = sortedAlphabet(value_list,inp)
print(*sort_list)