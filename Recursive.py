def fact(x):
	if x==1:
		return 1
	else:
	 return(x*fact(x-1))
num=4
print("the fact ",num, "is", fact(num))	  	