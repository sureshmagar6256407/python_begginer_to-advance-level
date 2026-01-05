'''class Student :
    def __init__(self,name) :
        self.name =name 

s1= Student('suresh')
print(s1.name)
del s1'''  # del means delete the object after this line




#private variable
'''class Account :
    def __init__(self,acc_no,pw):
        self.acc_no=acc_no
        self.__pw =pw #private variable
    def reset_pw (self):
        print(self.__pw)
acc1= Account(1243,'asbca')
print(acc1.acc_no)
print(acc1.reset_pw())'''

'''class Person:
    __name = 'suresh'

p1 = Person()
print(p1.__name)'''

"""
class Person :
    __name = 'suresh' 

    def __hello(self) :
        print('hello person')

    def greet (self):
        self.__hello()

    def call_name(self):
        Person.__name

p1 = Person()
print(p1.greet())
"""

class Account : 
    def __init__(self,acc_no,acc_pass):
        self.acc_no  = acc_no
        self.__acc_pass =acc_pass

    def reset_pw(self) : 
        print(self.__acc_pass)

    def __greet(self) :  
        print("hello new world")

    def greet_call(self) : 
        self.__greet()


acc1 = Account("122344","abcde")
# print(acc1.acc_no)
# print(acc1.reset_pw())
print(acc1.greet_call())
