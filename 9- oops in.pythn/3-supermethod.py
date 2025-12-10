
#super method 
class Grandfather:
    @staticmethod
    def name():
        print('grandfather name is john')

    @staticmethod
    def age() :
        print('grandfather age is 80')

class Father(Grandfather):
    def __init__(self,height):
        self.height = height
    @staticmethod
    def Father_name():
        print('father name is tularam pun')

    @staticmethod
    def Father_age ():
        print('father age is 50')

class Son(Father):
    def __init__(self,Name,Age,height):
        self.Name = Name
        self.Age =Age 
        super().__init__(height)#super method to access parent class constructor
        super().Father_name()

Son1 = Son('suresh',20,5.5)
print(Son1.name(),Son1.age())
print(Son1.height)
