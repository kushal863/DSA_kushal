while (True):
    # take operator as input
    op =input("Enter Operator:")
    if (op=='+' or op=='-'or op=='*' or op=='/'):
         # take two number as input
         num1 = int(input("Enter First Number:"))
         num2 = int(input("Enter Second Number:"))
         if(op=='+'):
            sum = num1+num2
            print(f"Sum of the {num1} and {num2} = {sum}")
         elif(op=='-'):
            subtract = num1-num2
            print(f"Difference between the {num1} and {num2} = {subtract}")
         elif(op=='*'):
            product = num1*num2
            print(f"Product the {num1} and {num2} = {product}")
         elif(op=='/'):
            Devision = num1/num2
            print(f"Deivision of the {num1} and {num2} = {Devision}")
    elif(op=='X' or op =='x'):
        print("Please Enter correct value")
        break
    else:
        print("Please end the correct operator")


         
