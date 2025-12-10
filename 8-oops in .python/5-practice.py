# class Student :
#     def __init__(self,name, marks):
#         self.name = name 
#         self.marks = marks

#     def avarage (self):
#         num = 0 
#         for i in self.marks:
#             num += i 
#             print('hello' ,self.name,'your avg scrore is ' ,num/3)

# s2 = Student('tekma',[33,4,45])
# s2.avarage()
 
'''
class Car :
    def  __init__ (self,color,model):
        self.color = color 
        self.model = model 
    
    def greet(self):
        return 'hello welcome to car world'
    
    def car_info (self) :
        print('car color is ,' ,self.color)
    def car_model (self) :
        for i in self.model:
            print('car model is ' ,i)


car1 = Car('red' ,[2020, 2021, 2022])
print(car1.greet())
car1.car_info()
car1.car_model()'''


# class Account :
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no =acc

#     #debit 
#     def debit(self,amount):
#         self.balance -= amount
#         print('rs ,' ,amount, 'was debited')
#         print('your current balance is ' ,self.get_balance())
#      #credit
#     def credit(self,amount):
#         self.balance += amount
#         print('rs' ,amount,'was credited')
#         print('your current balance is ' ,self.get_balance())

#     def get_balance (self):
#         return self.balance
# Account1= Account(10000,'9329194suresh')
# Account1.debit(2000)
# Account1.credit(5000)



# class Student :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s1 = Student('suresh', 20 )
# print(s1.name,s1.age)


'''
class Student :
    def __init__(self , name , score):
        self.name = name
        self.score  = score

    def f_student(self):
        # print(self.name)
        return self.name

    def avg_score (self) :
        # print (self.score)
        return self.score

    def save_result(self):
        if self.score >= 40 :
            with open ('pass.txt', 'a') as f:
                f.write(f'{self.name} :{self.score} (pass) \n')
            print(f'{self.name} passed and saved to pass.txt')

        else:
            with open('fail.txt','a' ) as f:
                f.write(f'{self.name} :{self.score} (fail) .\n')
            print(f'{self.name} failed and saved to fail.txt')
      

s1 = Student('suresh' , 50)
# print(s1.f_student(),s1.avg_score())
# s1.save_result()

s2 = Student('chandra' , 40)
s2.save_result()

s3 = Student('rahul' , 10)
s3.save_result()
# s4 = Student('anmol' , 90) '''