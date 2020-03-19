#genertor
def gen():
	n=1
	print("this first")
	yield n
	n+=1
	print("this is printed second")
	yield n

	