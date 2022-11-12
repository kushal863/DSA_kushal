# 1 Write a program to print wheather a number is even or odd, also take input from user.
# number = int(input("Enter the number to check even or odd"))
def even_odd(number):
    """
    Checking even odd
        """
    if (number%2==0):
        print(f"Number {number} is Even Number")
    else:
        print(f"Number {number} is Odd Number")


# even_odd(number)


# 2 Take a name as input and print a greeting message for that perticular name.

# name = input("Enter Name for greeting :")
def greeting(name):
    print(f"Hello, Good Morning {name}")

# greeting(name)

# 3 Write a program to input  principal,time and rate (P,T,R) from the user and find simple intrest.

# p = int(input("Enter Principal : "))
# t = int(input("Enter Time(In Months) : "))
# r = float(input("Enter Percentage Rate : "))

def simple_intrest(principal,rate,time):
    return int(principal*((1+(rate/100)*(time/12))))

# print(simple_intrest(p,r,t))

# 4 Take in two numbers and an operator(+,-,&,/) and calculate the value(Use if conditions)




# 5 Take 2 numbers as input and print the largest number

# num1, num2 = map(int,input("Enter two numbers with space").split())

def largest_num(a,b):
    if (a>b):
        return f"Largest Number {a}"
    else:
        return f"Largest Number {b}"
# print(largest_num(num1,num2))

# 6 Input currency in ruppes and output in usd

# curr_rs = int(input("Enter ammount in RS : "))
# curr_usd = round((0.012*curr_rs),3)
# print(f"Currency ruppes {curr_rs} in USD {curr_usd}")

# 7 To canculate Fibonacci Series up to n numbers

# a= 0
# b=1
# n=7
# count = 2
# while(count <=n):
#     prev =b
#     b = a+b
#     a = prev
#     count +=1
#     print(b)


# 8 To find out whether the given string is palidrome or not

# s = ['apple','radar','level','red']

# for word in s:
#     if word[::-1] ==word:
#         print(word)



n = 3445

ans =0
while(n>0):
    rem = n %10

    ans=ans*10+rem
    n =n//10
print(ans)
    

# 9 To find Armstrong Number between two given number

n = 134
ans =0
for i in range(len(str(n))):
   summ= int(str(n)[i]) *int(str(n)[i])*int(str(n)[i])
   print(summ)
   ans +=summ
print(ans)

n = 134
ans =0
while (n>0):
    rem = n%10
    summ = rem*rem*rem
    ans +=summ
    n= n//10
print(ans)