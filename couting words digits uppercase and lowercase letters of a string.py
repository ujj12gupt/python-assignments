
sen = input("enter your sentence\n")
# task1: to calculate number of words
cnt = 0;
b= sen.split()
for i in b:
    cnt = cnt + 1
print("number of words in the sentence is/are",cnt)

# task2: to calculate number of digits
cnt = 0
for i in sen:
    if(i in "0123456789"):
        cnt = cnt + 1
print("number of digits in the sentence are/is",cnt)
# task: to find Uppercase letters and lowercase letters
cnt1 = 0
cnt2 = 0
for i in range(0,len(sen)):
    if(sen[i].isupper() == True):
        cnt1 = cnt1 + 1
    elif(sen[i].islower() == True):
        cnt2 = cnt2 + 1
print("number of uppercase letters",cnt1)
print("number of lowercase letters",cnt2)
