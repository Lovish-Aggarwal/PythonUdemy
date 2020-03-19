class queue:
	def __init__(self):
		self.queue=list()

	def add(self,dataval):
	    
	    if dataval not in self.queue:
	       self.queue.insert(0,dataval)
	       return True
	       return False

	# def size(self):
	#     return len(self.queue)
	def remove(self):
		if len(self.queue)>0:
			return self.queue.pop()
		return ("no element")	


obj=queue()
obj.add("Python")
obj.add("cpp")
obj.add("Python 3")
obj.add("Java")
#print(obj.size())
print(obj.remove())
print(obj.remove())
print(obj.remove())
