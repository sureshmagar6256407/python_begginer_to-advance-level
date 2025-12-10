strude={
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

nwupadate={'city':'ghorahi'}
strude.update(nwupadate)
print(strude)