import random
arr=["Rock","Paper","Scissor"]
print("use Rock=0, Paper=1, Scissor=2 and (use 3 for exit):")

while True:
    com=random.randint(0,2)
    user=int(input("Enter your choice:"))
    if user==3:
        print("Thank You")
        break
    elif user==com:
        print("Game Tie")
    elif ((user==0 and com==3) or
            (user==1 and com==0) or
            (user==2 and com==1)):
            print("You Win")
            print(f"You Choose:{user} and Com choose:{com}")
    else:
        print("You Loose")
        print(f"You Choose:{user} and Com choose:{com}")

