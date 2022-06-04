n=int (input ("Enter a number:"))
while(n<0):
    print("please enter valid number")
    n=int (input ("Enter a number:"))

fact=1
for i in range (1, n+1):
    fact= fact* i
print("factorial of",n,"is",fact)
