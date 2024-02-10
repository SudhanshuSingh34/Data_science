# python program for If else statement 
i = 20
if (i < 15): 
    print("i is smaller than 15") 
    print("i'm in if Block") 
else: 
    print("i is greater than 15") 
    print("i'm in else Block") 
print("i'm not in if and not in else Block")

#  python program to calculate digit.
Number=int(input("enter your number :"  ))
if(Number>=0 and Number<=9):
    print("single digit number")
elif(Number>=10 and Number<=99):
    print("two digit number")
elif(Number>=100 and Number<=999):
    print("three digit number")
elif(Number>=1000 and Number<=9999):
    print("foor digit number")
else:
    print("not found number")

# if.else chain statement
letter = "S"

if letter == "B":
	print("letter is B")

else:

	if letter == "C":
		print("letter is C")

	else:

		if letter == "S":
			print("letter is A")

		else:
			print("letter isn't A, B and C")

