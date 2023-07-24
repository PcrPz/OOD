class Queue:
    def __init__(self):
        self.queue =[]

    def enqueue (self,data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue)==0
    
    def __len__(self):
        return len(self.queue)
    
    def __str__(self):
        return f"{', '.join(str(x) for x in self.queue)}"
    
queue_f = Queue()
queue_m = Queue()
queue_massage_m = Queue()
queue_massage_f = Queue()

activity = {"0": "Eat","1": "Game","2":"Learn","3":"Movie"}
loc = {"0": "Res.","1": "ClassR.","2":"SuperM.","3":"Home"}
all_score = 0
massage = input("Enter Input : ").split(",")
for act in massage:
    male,female = act.split(" ")
    queue_m.enqueue(male)
    queue_f.enqueue(female)
print(f"My   Queue = {queue_m}")
print(f"Your Queue = {queue_f}")
#read act male
while not queue_m.is_empty() and not queue_f.is_empty():
    today_m = queue_m.dequeue()
    now_f = queue_f.dequeue()
    work_f,location_f = now_f.split(":")
    work_m,location_m = today_m.split(":")
    if work_m == work_f :
        if location_m == location_f:
            all_score +=4
        elif location_m != location_f:
            all_score +=1
    if work_m != work_f :
        if location_m == location_f:
            all_score +=2
        elif location_m != location_f:
            all_score -=5
    str_act_m=activity[work_m]+":"+loc[location_m]
    str_act_f=activity[work_f]+":"+loc[location_f]
    queue_massage_m.enqueue(str_act_m)
    queue_massage_f.enqueue(str_act_f)    
print(f"My   Activity:Location = {queue_massage_m}")
print(f"Your Activity:Location = {queue_massage_f}")
if all_score >= 7:
    print(f"Yes! You're my love! : Score is {all_score}.")
elif 7>all_score>0:
    print(f"Umm.. It's complicated relationship! : Score is {all_score}.")
elif all_score<=0:
    print(f"No! We're just friends. : Score is {all_score}.")

# while not queue_f.is_empty():
#     now = queue_f.dequeue()
#     work1,location1 = now.split(":")




