data={
    "day": [],
    "exercise": [],
    "duration": [],
    "calories": []
}
user={
    "name":[],
    "age":[],
    "weight":[]
}

def userinfo():
    user["name"].append(name)
    user["age"].append(age)
    user["weight"].append(weight)

name=input("Enter Your name:")
age=input("Enter Your age:")
weight=input("Enter Your weight:")
userinfo()

def View():
    if not data:
        return "No records."
    print("\n")
    print(f"Total Workout Days:{len(data["day"])}")
    print(f"Total time you spend:{sum(data["duration"])}")
    print(f"Total calories Burned:{sum(data["calories"])}")


def main():    
    while True:
        print("\n")
        print(f"\n{name}'s Workout Tracker Menu")
        print("1. Add Workout")
        print("2. View Progress Summary")
        print("3. List All Workouts")
        print("4. User Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            day = input("Enter day: ")
            data["day"].append(day)
            exercise = input("Enter exercise name: ")
            data["exercise"].append(exercise)
            duration = int(input("Enter duration (mins): "))
            data["duration"].append(duration)
            calories = int(input("Enter calories burned: "))
            data["calories"].append(calories)

        elif choice == "2":
            print(View())
        elif choice == "3":
            print("\n")
            for key, value in data.items():
                print(f"{key}: {value}") 

        elif choice == "4":
            print(f"Name:{user["name"]}")
            print(f"Age:{user["age"]}")
            print(f"Weight:{user["weight"]}")
        elif choice=="5":
            print("Exiting... Stay fit!")
            break
        else:
            print("Invalid choice. Please try again.")
main()