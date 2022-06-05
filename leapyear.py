yr=int(input("Enter a year:"))
if yr%4 == 0:
    if (yr%100 == 0 and yr%400 == 0):
       print("leap year")
    elif (yr%100 != 0):
        print("leap year")
    elif (yr%100 ==0 and yr %400 != 0):
        print("not a leap year") 
else:
    print("not a leap year")
