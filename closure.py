#do thing not possible

def printmsg(msg):
	def printer():
		print(msg)
		
    return printer()

another=printmsg("This is printer")
another()    		