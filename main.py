while True:
    print("=======================")
    print("Study Sprint Tracker")
    print("=======================")
    print("1. Add study session")
    print("2. View study sessions")
    print("3. Show learning summary")
    print("4. Exit\n")

    x = int(input("Choose an option: "))
    print("\n")

    if x==1:
        print("Adding a study session.")
    elif x==2:
        print("Viewing study session.")
    elif x==3:
        print("Showing learning summary.")
    elif x==4:
        print("Good Bye")
        break
    else:
        print("Invalid Choice, Try again.")

