n=int (input ("Enter number of terms in fibonacci:"))
f= 0 #first number
s= 1 #second number
while(n<= 0):
    print("not an appropriate number")
    n=int (input ("Enter number of terms in fibonacci:"))
if(n>=1):
    for i in range (1, n+1):
        print (f, end=" ")
        third= f + s
        f= s
        s= third
