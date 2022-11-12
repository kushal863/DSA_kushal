# def greet(name):
#     name[1]=2 # if you make a change to the object via this ref variable
#     return name

# naam = [1,3,4]
# print(greet(naam))
# print(naam)

# def swap(num1,num2):
#     temp = num1
#     num1 = num2
#     num2 = temp
#     return num1,num2
# # This change will only be valid in this function scope only.
# a = 10
# b= 20
# print(swap(a,b))
# print(a)
# print(b)


# Function Overloading
# Function overloading happening when two function in the class is the same.
# its working fine when passed two different argument (those two functions)


# Question calculate armstrong number

# a =153
# sum = 0
# while (a>0):
#     rem = a%10
#     cube = rem*rem*rem
#     sum += cube
#     a=a //10
# if (a==sum):
#     print("This is armstrong number")
# else:
#     print("This is not")
# print(sum)

# print(type(a))
# print(type(sum))
# print(int(a)==int(sum))


# print(153%10)


def isarmstrong(n):
    sum=0
    original =n
    while (n>0):
        rem = n%10
        sum = sum+ rem*rem*rem
        n=n//10
    # print(sum)
    # print(n)
    return sum==original
# print(isarmstrong(153))



# Linear Search
import array as arr

from minnumber import min_num

a = arr.array('i',[3,4,5,6,7,4,67,73,1])

target = -1

def linearsearch(n, target):
    if (len(n)==0):
        return -1
    for i in range(len(n)):
        element = n[i]
        if element ==target:
            return element
    return -1
# print(linearsearch(a,target))

def min_number(a):
    if (len(a)==0):
        return -1
    ans = a[0]
    for i in range(len(a)):
        if a[i]< ans:
            ans = a[i]
    return ans
print(min_number(a))