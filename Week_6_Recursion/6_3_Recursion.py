def keroro(start,stop,round):
    round +=1
    if start % 14 == 0 and start != 0:
        return 
    if start == stop:
        global max_way
        max_way += 1
        global distance
        distance.append(round)
        return
    if start > stop :
        return
    else:
        keroro(start+1,jump,round)
        keroro(start+5,jump,round)
        keroro(start+7,jump,round)


jump = int(input("Input number : "))
max_way = 0
distance = []
round = 0
start=0
keroro(start,jump,round)
if max_way == 0 :
    print("Mission Failed")
else:
    print(f"Minimum Distance is {min(distance)-1}")
    print(f"Maximum Way is {max_way}")