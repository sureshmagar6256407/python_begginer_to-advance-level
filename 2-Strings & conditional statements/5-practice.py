#1-Wap to check if a number entered by the user is odd or even.
# user =int(input('Enter a number : '))
# if(user%2==0):
#     print("your Enter number is 'Even'")
# else:
#     print("your Enter number is 'odd'")



#2-wap to find the gratest of 3 numbers entered by the user.
# user1=int(input("Enter the first number :"))
# user2=int(input("Enter the second  number :"))
# user3=int(input("Enter the third number :"))

# if (user1 > user2 and user1  > user3):
#     print("this is a greatest number user1 :",user1)
# elif(user2 > user3 and user2 > user1):
#     print("this is a gratest number  user2: ",user2)
# else:
#     print("this is a greatest number user3 :",user3)




# #3-Wap to check if a number is a multiple of 7 or not
# number = 21
# if (number%7==0):
#     print('this is a multiple of 7')
# else:
#     print('this is not multiple of 7')

#4-largest of 4 number
# user1=int(input("Enter the first number :"))
# user2=int(input("Enter the second number :"))
# user3=int(input("Enter the third number :"))
# user4=int(input("Enter the fourth number :"))

# if (user1 >= user2 and user1 >= user3 and user1 >=user4):
#     print("the largest number is user1 :",user1)
# elif(user2 >= user3 and user2 >= user4):
#     print("the largest number is user2",user2)
# elif(user3 >= user4):
#     print("the largest number is user3",user3)
# else:
#     print("the largest number is user4",user4)


#5- wap to input 2 number and print that number which number is bigger
# user1= int(input("Enter a first number--:"))
# user2= int(input("Enter a second number--:"))

# if(user1 > user2 ) :
#     print('user1 is bigger number than user2--:',user1)

# else:
#     print('user2 is bigger number than user1--:',user2)


#6- if the user name is "suresh " text them 'welcome back suresh' if user name is randomly print'hello stranger'
# name = "suresh"
# User=input("Enter your name--:")
# if (User ==name):
#     print("welcome backs,\n\t Suresh")
# else:
#     print('Hello ,\n\tStranger')


#7-wap to input user age and if age > 18 print"you are underage" else age>=18 print'you can vote '
# User=int(input('Enter your age'))
# age =18
# if (User >= age):
#     print('you can vote')
# else:
#     print('you are underage')


#8-wap to input 3 number and find the biggest number
# user1=int(input("ENTER A FIRST NUMBER--:"))
# user2=int(input("ENTER A SECOND NUMBER--:"))
# user3=int(input("ENTER A THIRD NUMBER--:"))

# if(user3> user2 and user3 > user1):
#     print('user3 is the largest number ::',user3)
# elif(user2 > user1):
#     print('user2 is the largest number ::',user2)
# else:
#     print('user1 is the largest number ::',user1)



#9-even or odd 
# num = int(input("enter the number"))
# if(num%2==0):
#     print('this is a even number',num)
# else:
#     print('this is a odd number',num)

#10-grading sysstem
# marks=39 
# if (marks >= 80 and marks <= 100):
#    grade="A"
# elif (marks >= 60 and marks <= 79):
#     grade="b"
# elif(marks>= 40 and marks <=59):
#     grade="c"
# else:
#     grade="fail"
# print(grade)

    
#11-sequecne 
# user =input("Enter everything ::")
# print(len(user))
# print(user[0],'-',user[-1],'-',user.upper(),'-',user.strip())


#12- right a sentence but not coming eror
# print('\'He said,\' \'Python is fun!\'')


#13-if string's in "a " letter then print "contain 'a'",don't a print "doesnot containa 'a'"
# user=input("Enter a random letter :")
# if(user.count('a')):
#     print("contain  :'a'")
# else:
#     print("dosen\'t containa :\"a\"")


#14-wap program to ask the input pw if pw character more than 8 and they use '#' '@' tell them strong pw else tell them weak pw 
# user=input("Enter the password :: ")
# if (len(user)>= 8 or ('#'in user or '@' in user)):
#     print("Strong password")
# else:
#     print("Weak password")


#-this is reserved keyword in python herne code ho
# import keyword
# print(keyword.kwlist)

#15-password checking
# pw= input("enter the pw  :: ")
# if (len(pw) >= 8 or ('#' in pw or '@' in pw ) or any(ch.isdigit()for ch in pw)):
#     print('Very strong password')
# else:
#     print('weak password')

#-16 wap to input the user password check if pwindex is greater than 8 or pw using special character '#''@' or first letter is uper chase print (strong password ) else (weak password)
# pw = input("Enter the password ::")
# if (len(pw) >= 8 or ('@' in pw or '#' in pw)  or pw[0].isupper()):
#     print('Strong password')
# else:
#     print('weak password')


#16-str analyze
# User=input("enter the letter :")
# if (User[0:].isupper()):
#     print("all uper case")
# elif(User[0:].islower()):
#     print("all lower case")
# else:
#     print("all mixed")



#17- Email validator
# email =input("Enter your Email::")
# if('.' in email and '@' in email):
#     print('valid Email')
# else:
#     print('invalid Email')


#18-check the last string index and first index string
# User= input('Enter a letter ==')
# if (User[0]==User[-1]):
#     print("match")
# else:
#     print("not match")


#19-tempreture
tempreture = int(input("Enter the current tempreture of your location =="))
if (tempreture > 30):
    print("hot day")
elif(tempreture<= 30 and tempreture>=15) :
     print("warm day")
else:
    print("cold  day")