class laptop(object):

	def __init__(self):
		self.version=2018

	def getversion(self):
	    print(self.__version)
	
	def setversion(self):
	    self.__version=version


obj=laptop()
obj.getversion()
obj.setversion(2019)
obj.getversion()
print(obj.__version)
