a = input("enter your string\n")
print("first way of traversing through string in python \n")
for i in a:
    print(i)
print("second way of traversing through string in python \n")
b =len(a)
for i in range(0,b):
    print(a[i]);
print("reverse transversal in string \n")
for i in range(b-1,-1,-1):
    print(a[i])