# def greet (name):
# 	print("hello "+ name)
# 	return

# greet("tarun")

# def abc(num):
# 	if num>=0:
# 		return num
# 	else:
# 	    return -num

# print(abc[6])

def changename(list1):
	print("values inside function before changing",list1)
	list1[2]=50
	print("values inside the function after change",list1)

	return

list1=[10,50,60]	
changename(list1)
print("values outside the function",list1)