class abc:
    def __init__(self,name,age):
        self.age=age
        self.name=name
        
    def xyz(self,song):
        return "{} is now dancing".format(self.name,song)

    def qwe(self):
        return "{} is now dancing".format(self.name)

a=abc("denis",25)

print(a.xyz("happy"))
print(a.qwe())                   