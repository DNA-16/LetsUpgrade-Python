 #Assignment1:Finding index of a substring in a given string

str1=input("Enter the string: ")
sub=input("Enter the substring: ")
length=len(str1)
temp=len(sub)
flag=0
for each in range(len(str1)):
    if(sub==str1[each:each+len(sub)]):
        print("The substring",sub,"is found at index:",each)
        flag=1
if(flag!=1):
    print("Entered substring is not found in the given string")
    

#Assignment2: islower() and isupper()
    
#islower()
str2=input("Enter the string: ")
if(str2.islower()==True):
    print("The entered string is in lowercase.")
else:
    print("The entered string is not in lowercase.")
    
#isupper()
str3=input("Enter the string: ")
if(str3.isupper()==True):
    print("The entered string is in uppercase.")
else:
    print("The entered string is not in uppercase.")