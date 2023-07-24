print(" *** Wind classification *** ")
speed = float(input("Enter wind speed (km/h) : "))
if speed < 52 and  speed > 0 :
    print("Wind classification is Breeze.")
elif speed >= 52 and  speed < 56 :
    print("Wind classification is Depression.")   
elif speed >= 56 and  speed < 102 :
    print("Wind classification is Tropical Storm.")   
elif speed >= 102 and  speed < 209 :
    print("Wind classification is Typhoon.")   
elif speed >= 209 :
    print("Wind classification is Super Typhoon.")
else:print("!!!Wrong value can't classify.")


