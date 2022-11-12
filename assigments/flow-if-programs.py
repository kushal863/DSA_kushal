
# 1 Input a year and find wheather it is a leap year or not
def leapyear():
    year = int(input("Please Enter Year:"))

    if (len(str(year)) ==4):
        if (year %4==0):
            print(f"Year {year} is leap year")
            if(year%100==0):
                print(f"Year {year} is leap year")
            else:
                print(f"Year {year} is not a leap year")
        elif(year%400!=0):
            print(f"Year {year} is not a leap year")
        else:
            print(f"Year {year} is not a leap year")
    else:
        print("Please Enter a correct year")
        
# leapyear()

# 2 Take two numbers and print the sum of both

# a = int(input("Enter First Number:"))
# b = int(input("Enter Second Number:"))
def sum(a,b):
    c = a+b
    return f"Sum of {a} and {b} is {c}"
# print(sum(a,b))

# print(type(sum(a,b)))

# 3 Take a number as input and print the multiplication table of it.



def multiplication_table():
    n = int(input("Enter the number"))
    if (n<=1):
        print("Enter a valid number for multiplication table")
    else:
        for num in range(1,11):
            product = n*num
            print(f"{n} * {num} = {product}")
# multiplication_table()


# 4 Take two numbers as input and find their HCF and LCF

def hcf_lcf(a,b):
    for i in range(1, max(a,b)):
        if (a%i==b%i==0):
            hcf =i
    lcm = (a*b)//hcf
    return f"Hcf and Lcf of {a} and {b} are {hcf} , {lcm}"
   
# print(hcf_lcf(12,14))

# 5 Keep taking numbers as input till the user enter x, after that print sum of all


def sum_w():
    """
    Enter the numbers to sum.
    Enter X or x to quit the program
    """
    sum = 0    
    while True:
        num = input("Enter Number:")
        if (num =='x') or (num =='X'): break
        num = int(num)
        sum = sum+num
    return sum
        
# print(sum_w())


