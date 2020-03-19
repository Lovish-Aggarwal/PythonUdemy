class stack:
	def __init__(self):
		self.stack=[]

	def add(self,dataval):
	    
	    if dataval not in self.stack:
	       self.stack.append(dataval)
	       return True

	    else:
	        return False

	def peek(self):
	     return self.stack[0]
	
	def remove(self):
	    if len(self.stack)<=0:
	       return("No element in stack")
	    else:
	       return self.stack.pop()        

obj=stack()
obj.add("Python")
obj.add("cpp")
#obj.peek()
#print(obj.peek())
print(obj.remove())
obj.add("Python 3")
obj.add("Java")
print(obj.remove())	                	