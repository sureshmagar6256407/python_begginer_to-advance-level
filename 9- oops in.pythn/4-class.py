# class Person :
#     name  = 'rahul ' 

#     def ChangeName (self ,name) :
#         Person.name  = name 

# p1 = Person()
# p1.ChangeName('tekam')
# print(p1.name)
# print(Person.name)


class Person :
    name = 'jajaja'

    @classmethod
    def ChangeName(cls,name):
        cls.name = name 

p1 = Person()
p1.ChangeName('tekam')
print(p1.name)
print(Person.name)