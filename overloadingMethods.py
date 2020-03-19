#iterators
list1=[4,8,6,9]

myiter=iter(list1)

print(next(myiter))

print(next(myiter))

print(myiter.__next__)
print(myiter.__next__)

next(myiter)