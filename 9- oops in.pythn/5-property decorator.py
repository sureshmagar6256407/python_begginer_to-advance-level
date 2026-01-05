"""
class Student :  
    def  __init__(self,cem ,eng,comp):
        self.cem  =cem 
        self.eng =eng  
        self.comp  = comp
        
    @property
    def calculate (self) :
        return  (self.cem + self.eng +self.comp)/3
        

stu  = Student (98,94,99)
print(stu.calculate)

stu.cem  = 50
print(stu.calculate)
"""