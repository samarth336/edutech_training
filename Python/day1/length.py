pas=input("Enter a password: ")
x=pas.isalnum()
if len(pas)>=8 and len(pas)<=16 and x==True:
    print("Correct")
else:
    print("Incorrect")

        