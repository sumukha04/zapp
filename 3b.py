str1=input("enter the string 1: ")
str2=input("enter the sting 2: ")
if len(str1)<len(str2):
    short=str2
    long=str1
else:
    short=str1
    long=str2
    matchCnt=0
    for i in range(short):
        if str1[i]==str2[i]:
            matchCnt+=0
            print("similarity between two strings: ")
            print(matchCnt/long)