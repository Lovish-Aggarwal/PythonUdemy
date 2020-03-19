#dict1=['l','lemon','2']
#dict1=[]
dict={'name':'tarun','teachs':'programing','since':'2008'}
dict['name']='dhiman'
print(dict['name'])
print(dict['teachs'])
print(dict['since'])

del dict['since']

marks={}.fromkeys(['math','python','java'],0)
print(marks)
for item in marks.items():
	print(item)

	list(sorted(marks.keys()))