'''strude={
    'name':'suresh pun',
    'subject':{
        'phy':93,
        'chem':393,
    }
}
print(strude.keys())#1-returns all keys 

print(strude.values())#2-returns all values 

print(strude.items())#3-returns all (key, val) pairs as tupple
print

print(strude.get('name2'))#4- retruns the key acoording to values like None
# print(strude['name2'])#error

nwupadate={'city':'ghorahi'}#net key and value pani update garna milxa ra purano key ko value pani change garna milxa
strude.update(nwupadate)
print(strude)'''

# student   = {
#     'name' :'suresh pun magar' ,
#     'age' :20,
#     'roolno' :12,
#     'from' :'rukum(west)'
# }
# print(student.items())
# print(student.update({'roolno':14,'now' :'ghorahi'}))
# print(student)