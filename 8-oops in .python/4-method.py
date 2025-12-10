class Student :
    def __init__ (self ,name,marks):
        self.name = name 
        self.marks = marks
    def hello(self):
        print('hello' ,self.name)

    def get_marks(self):
        return self.marks

s1 = Student('suresh',44)
s1.hello()
print(s1.get_marks())

s2 = Student('tekam',53)
s2.hello()
print(s2.get_marks())