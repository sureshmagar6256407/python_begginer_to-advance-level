#single inheritance
'''
class Car :
    @staticmethod
    def start() :
        print('car started')

    @staticmethod 
    def stop() :
        print('car stopped')

class ElectricCar (Car) :
    def __init__(self,name):
        self.name = name 

car1 = ElectricCar('tesla')
car2 = ElectricCar('nissan')

print(car1.start())



class Father :  
    name_F  = "tularam"
    age_F  = 30

    def get_father_name(self) : 
        return self.name_F 

    def father_age (self) :
        return self.age_F 

     
class Son (Father) :  
    def __init__(self, name, age):
        self.name   =    name 
        self.age  =age    

s1  =Son("suresh" , 30)   
print(f"my name is {s1.name} and age is {s1.age} . also my father name is {s1.get_father_name()} and his age is {s1.father_age()}")
'''


#multilevel inheritance
'''
class Animal :
    @staticmethod
    def eat():
        print('animal is eating')

    @staticmethod
    def stop():
        print('animal stooped eating')

class Dog(Animal):
    def __init__(self,name):
        self.name = name 

class BabyDog(Dog):
    def __init__(self,type):
        self.type = type

dog1 = BabyDog('tommy')
print(dog1.eat())'''

#multiple inheritance
'''
class A:
    car1 ='welcome to class A'

class B:
    car2 ='welcome to class B'

class C( A,B) :
    car3 ='welcome to class C'

c1 = C()
print(c1.car1)
print(c1.car2)
print(c1.car3)
'''

