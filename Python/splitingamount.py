amount=int(input("enter your bill:"))
per=int(input("enter no.of persons:"))
tip=int(input("enter % of tip:"))
t=(tip/100)*amount
a=(amount/per)+t
print(f"Each per will pay {a} amount")