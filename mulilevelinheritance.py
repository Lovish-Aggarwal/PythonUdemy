class animal:
	def eat(self):
		print("eating")

class dog(animal):
	def bark(self):
		print("barking")

class baby(dog):
    def weep(self):
        print("weeping")		

d=baby()
d.bark()
d.weep()