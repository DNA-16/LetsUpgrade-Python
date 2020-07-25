#Assignment1: Sorting the given list such that all 0's are in right hand side.

list1=[0,1,2,10,4,1,0,56,0,1,3,0,56,0,4]
list2=[]
for each in list1:
    if(each==0):
        list1.remove(0)
        list2.insert(-1,0)
list1.sort()
list1=list1+list2
print(list1)

#Assignment1: Merging and sorting the given sorted lists using only 1 loop.

list1=[10,20,30,40,50,60,70]
list2=[5,15,25,35,45,55,65]
list3=list1+list2
list4=[]
for i in range(len(list3)):
    list3min=min(list3)
    list4.append(list3min)
    list3.remove(list3min)
print(list4)
    
