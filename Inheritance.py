class bird:
	
	def __init__(self):
		print("bird is ready")

	def whoisthis(self):
	    print("bird")
	
	def swim(self):
	    print("swim faster")

class penguin(bird):
   
     def __init__(self):
        super().__init__()  #inherit
        print("penguin is ready")
   
     def whoisthis(self):
        print("penguin")

     def run(self):
        print("Run faster")


peggy=penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()             	        	