import info
import mathoperation
name=input("enter your name:")
std=input("enter your std:")
print(info.users(name,std))
marathi=int(input("enter your Marathi sub marks:"))
hindi=int(input("enter your Hindi sub marks:"))
eng=int(input("enter your English sub marks:"))
print(f"Your total percentage is {mathoperation.add(marathi,hindi,eng)}")
