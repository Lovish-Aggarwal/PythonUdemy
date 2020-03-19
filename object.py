class student:
    def __init__(self,rollno,name):
           self.rollno=rollno
           self.name=name
    def displaystudent(self):
        print("rollno",self.rollno,",name",self.name)

emp1=student(147,"Malik")
emp1.displaystudent()
