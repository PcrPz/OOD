def find_power(place,group):
    size = len(group)
    if place >= size:
        return 0
    return group[place] + find_power(2*place+1,group) + find_power((2*place)+2,group)
    

group = []
mes,pair = input('Enter Input : ').split("/")
inp = [int(i) for i in mes.split()]
for i in inp:
    group.append(i)
print(sum(group))
for i in pair.split(","):
    first = find_power(int(i[0]),group)
    second = find_power(int(i[2]),group)
    if first > second :
        print(f"{i[0]}>{i[2]}")
    elif first == second :
        print(f"{i[0]}={i[2]}")
    elif first < second :
        print(f"{i[0]}<{i[2]}")

    





