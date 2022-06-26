a = input("enter your string\n")
b = len(a)
reverse_string = ""
for i in range(b-1,-1,-1):
    reverse_string = reverse_string + a[i]
print("reverse string is",reverse_string)
if(reverse_string == a):
    print("string is palindrome")
else:
    print("string is not palindrome")