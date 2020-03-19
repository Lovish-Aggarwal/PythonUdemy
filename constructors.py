class person:
	name=""
	age=0

	def __init__(self,personname,personage):
		self.name=personname
		self.age=personage

	def showname(self):
	     print(self.name)

	def showage(self):
	     print(self.age)

person1=person("denis",26)	
person2=person("tarun",20)

person1.showname()
person2.showage()	
