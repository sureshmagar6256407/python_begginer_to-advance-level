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

student = {
    'name' :'suresh pun magar' ,
    'age' :20,
    'from' :'rukum(west)'
 }

# student.setdefault('ghar' ,0)#returns the value of the specified key. if the key does not exis: insert the key, with specified value , if key exist it did'nt chang value 

# student.update({'marks' :20})#updates the dictionary with the speicied key-values pairs


# student.clear()#remove all the element from the dictionary

# `new_Copy = student.copy()#returns a copy of the dictionary

# keys  = ['name','age','sex']
# new_dict = dict.fromkeys(keys)#returns a dictionary with the specified keys and values . ra split(jastai ho yo ) list,tuple,string,set lai dictionary banauxa
# print(new_dict)

# get = student.get('name')#returns the value of the specified key
# print(get)

# pop  =student.pop('name') romoves the element with the speciefied key
# print(pop)
# print(student)

# student.popitem()#Removes the last inserted key_value pair
# print(student)







# student   = {
#     'name' :'suresh pun magar' ,
#     'age' :20,
#     'roolno' :12,
#     'from' :'rukum(west)'
# }
# print(student.items())
# print(student.update({'roolno':14,'now' :'ghorahi'}))
# print(student)