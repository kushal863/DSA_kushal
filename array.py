# Why we need array?


# Store a role number
kushal = 23

name = 'kushal'

rol1 = 10
rol2 =20
rol3 = 30
rol4 = 40
rol5 = 50

"""
Array
# It is a collection of datatype.


Important Points

All the data types of the data in the array should be same.
     You can not mix and match data dtypes.

 In java premitive are stored in the stack memory.

 In python there are no premitive types.. everything stored as object


 Two Dimentional Array:
 You can call this the array of array

"""


# Creating a array
# import array as arr
# a =arr.array('i' ,[1,2,3])
# for i in a :
#     print(i)

# print(a[1])    

# n = arr.array('f',[2.2,4,5])
# for i in n:
#     print(i)

# d= arr.array('f',[5,5,6,7.4])

# for i in d:
#     print(i)

# Checking the size of each row

d=[[1,2,3],[3,5],[6,7,8,10]]
     
for row in d:
    print(f"Length of each rows is :{len(row)}")
