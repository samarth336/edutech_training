num=int(input("Enter the number:"))
l=[]
if num==0:
    print("0")
elif num==1:
    print("It not prime.")
for i in range(2,num):
    if num%i==0:
        if not l:
            l.append(1)
        l.append(i)
if not l:
    print("it is prime number because it can be divisible for",[1,num],"only")
else:
    l.append(num)
    print(l)
