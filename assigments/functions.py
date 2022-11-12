# 1 Define two methods to print the maximum and minmum numbers repectivily among three numbers entered by user.

def max_number(a,b,c):
    #calculate the Maximum number
    maxx =a
    if (maxx<b):
        maxx=b
    elif(maxx<c):
        maxx=c
    return maxx

def min_number(a,b,c):
    # calculate the minimum number
    # code var =a, var>b, var=b, var>c, var=c
    min =a
    if (min>b):
        min=b
    elif(min>c):
        min=c
    return min

def cal_min_max():
    # calling min_number and max_number funcitons to calculate min anc max number respectivly
    # first number
    # a = int(input("Enter the first number : "))
    # b = int(input("Enter the second number: "))
    # c = int(input("Enter the third number: "))
    min = min_number(a,b,c)
    max= max_number(a,b,c)

    return f"Min Number : {min} and Max Number : {max}"

# print(cal_min_max())


# 2 Define a program to find out wheather a number is even or odd

def even_odd():
    """
    To check wheather the number is odd or even
    
    """
    ans=0
    try:
        num = int(input("Enter the number: "))
        if (num%2==0):
            return f"Number {num} is even"
        else:
            return f"Number {num} is odd"
    except Exception as e:
        print("Please enter the integer format. Getting error: ", e)
    # checking the even condition

    
# print(even_odd())

# write a program to calculate maximum whealth.


a = [[2,3,54],[54,56,4],[34,56,3]]

max =0
for row in range(len(a)):
    row_sum=0
    for col in range(len(a[row])):
        row_sum = row_sum+ a[row][col]
    print(row_sum)
    if row_sum>max:
        max = row_sum
print(max)

# A person is eligble  to vote if his/her age is greater































      
