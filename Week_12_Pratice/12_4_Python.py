print("*** String Rotation ***")
str1,str2 =input("Enter 2 strings : ").split()
new1 = str1[-2:] + str1[0:-2]
new2 = str2[3:]+ str2[0:3]
round =1 
while(new1 != str1 or new2!=str2):
    if round <= 5:
        print(str(round), new1 , new2)
    new1 = new1[-2:] + new1[0:-2]
    new2 = new2[3:]+ new2[0:3]
    round=round+1
if round > 5:
    print(' . . . . . ')
print(str(round), new1 , new2)
print(f"Total of  {round} rounds.")




