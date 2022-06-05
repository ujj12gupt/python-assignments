a=int(input("Enter marks sub1 :"))
b=int(input("Enter marks sub2 :"))
c=int(input("Enter marks sub3 :"))
d=int(input("Enter marks sub4 :"))
e=int(input("Enter marks sub5 :"))
avg= (a+ b+ c+ d+ e)/5
if avg <40 :
    print ("fail")
elif avg<50:
    print ("third division")
elif avg<60:
    print ("second division")
else:
    print ("first division")
print (f" Total percentage marks of student is {avg}")
