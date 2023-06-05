import re
n=int(input("Number of factorial:"))
num_fac = 1
for i in range(1,n+1) :
    num_fac = num_fac*i
value = str(num_fac)
print(value)
cnt_zero = re.findall(r'[0]+',value)
print(cnt_zero)    
print(len(cnt_zero[-1]))



# import re

# s = '+-55+-5+++55+++66555'

# occurs = re.findall(r'[5]+',s)
# # print(max([len(i) for i in occurs]))
# print(occurs)
# print(len(occurs[-1]))

#   array = re.findall(r'[0-9]+', str)


# num_max = 0
# a_number = arr.array("i", [])
# n=int(input("Number of elements in array:"))
# for i in range(0,n):
#     l=int(input())
#     a_number.append(l)
    
#     if l>num_max :
#         num_max = l

# # a_number.index(num_max)
# print('max value index is : '+str(a_number.index(num_max)))