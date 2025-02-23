num=int(input("Enter a number:"))
if num%5==0:
    if num%2==0:
        print("Given number is Divisible by 5 and also even number")
    else:
        print("Number is divisible by 5 but not a even number")
else:
    if num%2==0:
        print("Number is not divisible by 5 but it is even number")
    else:
        print("Number is not divisible by 5 and not even number")