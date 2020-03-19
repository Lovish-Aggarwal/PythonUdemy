class abc(object):
	def __init__(self):
		super(abc,self).__init__()
		print("Base 1")

class xyz(object):
    def __init__(self):
        super(xyz,self).__init__()	
        print("Base 2")

class child(abc,xyz):
    def __init__(self):
        super(child,self).__init__()
        print("Heloo 3rd class for child class")

child()
