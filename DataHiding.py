#method overloading
# class human:
# 	def sayhello(self,name=None):
# 		if name is not None:
# 			print("hello "+ name)
# 		else:
# 		    print("hello")
# obj=human()
# obj.sayhello()
# obj.sayhello("denis")

def product(a,b):
	c=a*b
	print(c)

def product(a,b,d):
    c=a*b*d
    print(c)

product(5,9,6)    	#uses latest