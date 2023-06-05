import array as arr

# Array
num_max = 0
a_number = arr.array("i", [])
n=int(input("Number of elements in array:"))
for i in range(0,n):
    l=int(input())
    a_number.append(l)
    
    if l>num_max :
        num_max = l

# a_number.index(num_max)
print('max value index is : '+str(a_number.index(num_max)))





# a=[]
# n=int(input("Number of elements in array:"))
# for i in range(0,n):
#    l=int(input())
#    a.append(l)
# print(a)