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
        session = []
        study_topic = input("Study topic (eg: Python, DSA, JavaScript) :")
        print("Adding a study session.\n")
    elif x==2:
        print("Viewing study session.\n")
    elif x==3:
        print("Showing learning summary.\n")
    elif x==4:
        print("Good Bye\n")
        break
    else:
        print("Invalid Choice, Try again.\n")

