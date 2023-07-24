print(" *** Divisible number *** ")
x= int(input("Enter a positive number : "))
if x == 0 :
    print("0 is OUT of range !!!")
elif x != 0 :
    list = []
    for i in range(1, x + 1):
       if x % i == 0:
           list.append(i)
    str = ' '.join(map(str, list))
    long = len(list)
    print("Output ==> "+str)
    print("Total ==>",long)
