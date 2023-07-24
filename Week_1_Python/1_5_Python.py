num1 = [int(x) for x in input("Enter All Bid : ").split()]
if len(num1)== 1:
    print("not enough bidder")
else: 
    num1.sort()
    num1.reverse()
    if num1[0] > num1[1]:
        print(f"winner bid is {num1[0]} need to pay {num1[1]}")
    elif num1[0] == num1[1]:
        print(f"error : have more than one highest bid")

    
     

