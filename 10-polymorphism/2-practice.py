"""
class Circle : 
    def __init__(self,radius):
        self.radius  =radius

    def  Area(self) :  
        return 3.14 *self.radius**2
     
    def perimeter(self) : 
        return 2 *3.14 *self.radius


c1  =Circle(21)
print(c1.Area())
print(c1.perimeter())

"""

class Employe : 
    def __init__(self,roll ,department, salary):
        self.roll   =roll
        self.department = department
        self.salary = salary

    def Shodetainl(self) : 
        print(f"roll = {self.roll}")
        print(f"department = {self.department}")
        print(f"salary = {self.salary}")

class Enginer(Employe)    :  
    def __init__(self, roll, department, salary, name ,age):
        super().__init__("enginer" ,"bit" , 3000)
        self.name =name 
        self.age  =age 

e1 = Enginer("cheerman" , "BIT" ,40000 , "tekam",20)
e1.Shodetainl()