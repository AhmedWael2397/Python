#Getting 2 numbers from the user
print("Please Enter Two Numbers\n")
x=int(input("1'st Number "))
y=int(input("2'nd Number "))
#Preforming arithmatic operations 
sum_result=x+y
diff_result=y-x
mul_result=x*y
div_result1=x/y
div_result2=y/x
#Storing results and printing them
Res=f"You Entered {x} and {y} and their results are as shown below \n 1.Addition = {sum_result} \n 2.Subtraction = {diff_result} \n 3.Multiplication = {mul_result} \n 4.Divison of 1'st number by 2'nd = {div_result1} \n Divison of 2'nd number by 1'st = {div_result2} \n"
print(Res)
#Checking which is bigger number
if y<x:
    print("you entered the first number greater than the second\n")
else:
    print("you entered the first number smaller than the second\n")
#checking if sum is even/odd
if sum_result %2==0:
    print("sum is an even number\n")
else:
    print("sum is an odd number\n")