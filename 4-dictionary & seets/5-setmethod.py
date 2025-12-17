num1  = {1,2,3,4,5} 
num2   = {3,4,5,6,1,2,7,8,9,10}
# num3   = {1,2,3,4,5}
# num4 = {6,7,8,9,10}

# union() this is a most important
# ✅ update()
# ✅ intersection()
# ✅ difference()
# ✅ difference_update()
# ✅ discard()
# ✅ issubset() / issuperset()

# num2.difference_update(num1)
# print(num2)
# num1.clear()
# print(num1)

# nwe = num1.copy()
# print(nwe)

# new_set  =num2.difference(num1)
# print(new_set)

# num1.add(6)
# print(num1)

# new_set = num1.intersection(num2)
# print(new_set)

# print(num1)
# num1.intersection_update({3})
# print(num1)

# print(num1.isdisjoint(num4))


# print(num1.issubset(num2))
# print(num2.issubset(num1))

# print(num1.issuperset(num2))
# print(num1.issuperset(num3))

# num1.discard(10)
# print(num1)


# num1.pop()
# print(num1)

# num1.remove(1)
# print(num1)

# new_set  = num1.symmetric_difference(num2)
# print(new_set)

# num1.update({11})
# print(num1)

# num1.symmetric_difference_update(num2)
# print(num1)
# num2.symmetric_difference_update(num1)
# print(num2)

# new_set  = num1.union(num2) 
# print(new_set)



'''collection = set ( )

collection.add(1)#adds an element 
collection.add(2)
collection.add(2)

collection.remove(2) # remove the element an

collection.clear()# clear the full set
print(collection)


set1 = { 1,3 ,4 }
set_2 = { 3,4,5}
# print(set1.union(set_2))
# print(set1.intersection(set_2))
'''

num1 = {1,2,3,4,5}
num2 ={3,4,6,7,8}

# num1.symmetric_difference_update(num2)#insert the symmetric differences from this set and another 
# print(num1)

# uni= num1.union(num2) #returns a set containing the union of sets 
# print(uni)

# num1.update({10})#update the set with the union of this set and others
# print(num1)

# sym=num1.symmetric_difference(num2)#returns a set with the symmetric difference ot two sets
# print(sym)

# num1.pop()#removes an element from the set
# print(num1)

# num1.remove(3)#removes the specified element
# print(num1)

# super_set =num1.issuperset(num2) #returns true if all item of another set is present in this set
# print(super_set)

# sub =num1.issubset(num2)#returns true if all item of this set is present in another set
# print(sub)

# new = num1.isdisjoint(num2) #returns whether tow sets have a intersection or not
# print(new)

# num1.intersection_update(num2)#remove the items in this set that are not present in other,specified set(s)
# print(num1)



# print(num1.intersection(num2))# returns a set,that is the intersection of two other sets(yesle 2 set ma bhako similar value dinxa)


# num1.add(10)#adds an element to the set 

# num1.clear()#removes all the elements from the set

# num1_copy = num1.copy()#returs a copy of the set
# print(num1_copy)

# difference_set = num1.difference(num2)#returns a set containing the difference two or more sets(yesle a ma bhako tara b ma nabhako value dinx or b ma bhako value a ma nabhako dinxa) naya set banauxa
# print(difference_set)

# num1.difference_update(num2) #yesle difference jastai garxa but yesle real set bata noi hatauxa
# print(num1)

# num1.discard(1)# remove the specified item (yelse element hatauxa if set bhitra xa bhane xaina bhane kehi hudaina erro aaudaina)

