# pyhton program for for loop
num = int(input("enter the number"))
for i in range(1, 15):
    # print(str(num) + "x" + str(i) + "=" + str(i*num))
 print(f"{num}X{i}={num*i}")
 
#  python program for while loop
num = int(input("enter the number"))
sum1=0
while(num>0):
    sum1=sum1 + num 
    num=num-1
    print("the sum of first n numbers is",sum1)
      
# python program to find factorial of num 
num = int(input("enter the number:"))
factorial=1 
for i in range(1, num+1):
    factorial = factorial * i
    print(f"the factoroal of the  {num} is {factorial}")
    
#   star pattern  
n = 5 

for i in range(5):
    print("*" * (i+1))
    
n = 3
for i in range(3): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i-1), end="")
    print(" " * (n-i-1) )
    
#   python program to print multiplication table in reversed order.  
num = int(input("enter the num to print multiplication table in reverse order: "))
for i in range (10,0,-1):
    print(num*i)