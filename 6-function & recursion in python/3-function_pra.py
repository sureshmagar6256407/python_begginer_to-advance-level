'''citites = [ 'ktm' ,'rukum ' ,'dang' ,'chitwan']
nums = [ 1, 2, 3, 4, 5]
def print_len (list):
    print(len(list))
print_len (nums)
print_len(citites)
'''

'''heros  =  ['rajeshhamal' ,'nikhilupreti','birajbhatta' ,'anamolkc']
def print_list (list) :
    for item in list:
        print(item,end=' ')

print_list(heros)'''




'''def calc_fact(n):
    fact  = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
calc_fact(5)'''



# def converter (usd_val) :
#     NP_val = usd_val*141.81
#     print(usd_val,'Usd_val =' ,NP_val,'NP_Val')
# converter(11)


'''user= int (input('Enter the  currency you want to converting in to the dollar:: '))
def converter_to_NPR(usd_val):
    NP_Val=usd_val*141.81
    print(usd_val,'USD=',NP_Val,'NPR')
converter_to_NPR(user)'''

# cities = ['ktm ',' bhaktapur ','chitwan',' ghorahi' , 'tulsipur']
# def len_cites() :
#     print(len(cities))
# len_cites()

# n = 5 
# def calc_fact(n):
#     fact  = 1 
#     for i in range(1,n +1 ) :
#         fact *= i 
#     print(fact)
# calc_fact(4)

'''num  = int(input('Enter the number ::'))
def odd_even (num) :
    if num % 2 == 0 :
        print('This is a even number')
    else :
        print('This is a odd number ')
odd_even(num)
'''

'''def cal_Sum (n) :
    if (n==0):
        return 0
    return cal_Sum(n-1)+n

sum =cal_Sum(5)
print(sum)'''


# def print_list(list,idx=0):
#     if (idx== len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# fruits=['banana' ,'mango','chocolate','biscuit']
# print_list(fruits)