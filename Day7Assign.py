#Assignment1: Exchanging Keys and Values

port1={21:"FTP",22:"SSH",23:"Telnet",80:"http"}
list1=list(port1.keys())
list2=list(port1.values())
port2={}
len1=len(port1)

for each in range(len(list1)):
    port2[list2[each]]=list1[each]

print("Port1 before: ",port1)     
print("Port1 after: ",port2)    

#Assignment2:

list3=[(1,2),(3,4),(5,6),(4,5)]
list4=[]
tup1=()
for each in range(len(list3)):
    tup1=list3[each]
    a,b=tup1
    list4.insert(each,a+b)
print("Input: ",list3)
print("Output: ",list4)

#Assignment3:

list5=[(1,2,3),[1,2],['a','hit','less']]
list6=[]
list7=[]
list8=[]
for each in range(0,len(list5)):
    if type(list5[each])==tuple:
        a,b,c=list5[each]
        list6=[a,b,c]
    else:
        list7.append(list5[each])

for each in list7:
    list8.extend(each)
list6=list6+list8
print("Input: ",list5)
print("Output: ",list6)        
 