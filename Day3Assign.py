#Assignment1:Sum of N numbers using while

sum=0
N=eval(input("Enter the number "))
flag=0
n=0
while n!=N+1:
    if(type(N)==float):
        flag=1
        break
    sum=sum+n
    n+=1
if(flag==1):
    print(N,"is not a natural number")
else:
    print("Sum of first",N,"natural number is ",sum)
    

#Assignment2:To check whether the number is prime or not

num=int(input("Enter the number "))
flag1=0
for each in range(2,int((num+1)/2)):
    if(num%each==0):
        flag1=1
        break
if(num==1):
    print("1 is neither prime nor composite.")
elif(flag1==1):
    print(num,"is not a prime number.")
else:
    print(num,"is a prime number.")