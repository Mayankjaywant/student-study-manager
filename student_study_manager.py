print("===== Student Study Manager =====")

name = input("Enter your name: ")
course = input("Enter your course: ")

subjects = []

while True:
    print("\n===== MENU =====")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Calculate Study Hours")
    print("4. Check Progress")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subject = input("Enter subject name: ")
        subjects.append(subject)
        print("Subject added successfully!")

    elif choice == "2":
        print("\nYour Subjects:")

        if len(subjects) == 0:
            print("No subjects added yet.")
        else:
            subjects.sort()

            for i in range(len(subjects)):
                print(i + 1, subjects[i])

    elif choice == "3":
        days = int(input("Enter study days: "))
        hours = float(input("Enter study hours per day: "))

        weekly_hours = days * hours
        monthly_hours = weekly_hours * 4

        print("Weekly study hours:", weekly_hours)
        print("Monthly study hours:", monthly_hours)

    elif choice == "4":
        study_hours = float(input("Enter your study hours: "))

        if study_hours >= 5:
            print("Progress: Excellent")
        elif study_hours >= 3:
            print("Progress: Good")
        elif study_hours >= 1:
            print("Progress: Need Improvement")
        else:
            print("Progress: Study More")

    elif choice == "5":
        print("Thank you", name)
        print("Keep learning Python!")
        break

    else:
        print("Invalid choice. Please try again.")
