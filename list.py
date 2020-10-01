# list=[1,2,3]
# list=[]
# list=[1,"f",3.9]
# list1=['l','e','r','n','e','r']
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])

# list2=["learn",[0,2,3,5,6]]
# print(list2[0],[1])
# print(list2[1],[3])

# od=[2,4,6,8]
# od[0]=1
# print(od)
# od[1:4]=[1,3,5,7]
# print(od)

list3=['l','e','r','n','e','r']
list3.remove("e")
#del list3[2]
#del list3[1:5]
print(list3)

#List Are also initializes by an New Methode 
#Called List Comprehension 

l=[i for i in range(10)]
print(l)

#here we iterate i to a range and insert every element

l1=[i for i in range(10) if i%2==0]
print(l1)

# WE Can also use if condition

l2=[]

for i in range(10):
  if i%2==0:
    l2.append(i)

print(l2)

#this is the expanded for of the above list comprehension form
