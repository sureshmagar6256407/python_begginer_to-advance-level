class Student :
    @staticmethod
    def greet() :
        print('hello students')

    def __init__(self, name ,age):
        self.name = name 
        self.age =age
    def about(self):
        print(f'hello {self.name} and age is {20} years old boy come to the offince')

    
s1  = Student('suresh' ,20)
s1.greet()
s1.about()

# v.i = 
''' 1 - abstraction = hiding the internal details and showing only functionality
2 - encapsulation = wrapping the data
and methods into a single unit
3- inheritance = acquiring the properties of parent class to child class
4- polymorphism = ability to take more than one form '''