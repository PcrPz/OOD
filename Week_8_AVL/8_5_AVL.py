class Van:
    def __init__(self) -> None:
        self.status = 0
    
cus = 0
van,time = input("Enter Input : ").split("/")
van = int(van)
time = list(map(int,time.split()))
garage = []
for i in range(van):
    garage.append(Van())
while time:
    for i in range(len(garage)):
        if garage[i].status == 0 and time:
            cus+=1
            day = time.pop(0)
            garage[i].status = day
            print(f'Customer {cus} Booking Van {i+1} | {day} day(s)')
            garage[i].status -= 1
        elif garage[i].status > 0:
            garage[i].status -= 1