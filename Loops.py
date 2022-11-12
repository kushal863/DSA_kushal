# print numbers from 1 to 5
# Three types of loops will discuss


## FOR LOOPS
# Why different from while loops
# When you know how many times loop going to run
# initialisation, Condition, Increment/decrement
# for i in range(1,6):
#     print(i)

# print numbers from 0 to n

# n = int(input())
# for i in range(0,n):
#     print(f"{i} Hello Word")

# While Loops
# While (Condition)
# Body

# Why use and how different from for loop
# When you don't know how many times loops going to run
# Another reason for while loop is to look code more clearner

# num =1
# while (num<=5):
#     print(f"{num} Hello World")
#     num=num+1


# Find the largest number from three numbers

# a=10
# b=5
# c=500
# max =a
# if (b>max):
#     max =b
# if (c>max):
#     max =c
# print(max)

# Write a program to check alphabet is upper case or lower case
# text = input("Enter Text :")

# if text.islower():
#     print(f"Lower Case {text}")
# else:
#     print(f"Upper Case {text}")

# Calculate fibonaci series using for loop
# a =0
# b=1
# n=5
# count=2

# while (count<=n):
#     prev =b
#     b = a+b
#     a =prev
#     count+=1
# print(b)



# Figure out the number in numbers like how many time occurred

# num = int(input("Enter Number:"))
# count =0
# while (num>0):
#     # n = num%10
#     rem = num%10 # last digit
#     if (rem==3):
#         count+=1
#     num= num//10
# print(count)
# print(134//10)

# Return the reverse of some number
# num =str(102032)
# print(num[::-1])

# num =345657

# ans =0
# while (num>0):
#     rem = num%10 # te get remainder
    
#     num=num//10

#     ans = ans*10+rem
# print(ans)