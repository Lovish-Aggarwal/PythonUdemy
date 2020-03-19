class bird:
	
	def fly(self):
		print("bird is fly")
	
	def swim(self):
	    print("bird cant swim")

class penguin(bird):
   
    def fly(self):
        print("penguin can swim")
    def swim(self):
	    print("penguin can swim")

def flying_test(birds):
       birds.fly()

b=bird()
p=penguin()
flying_test(b)
flying_test(p)     	        	