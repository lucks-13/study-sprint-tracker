sessions = []
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
        study_topic = input("Enter Study topic (eg: Python, DSA, JavaScript) :")
        duration = int(input("Enter duration in minutes (eg: 45) :"))
        new_session = {
            "topic":study_topic,
            "minutes":duration
        }
        sessions.append(new_session)
        print("Adding a study session.\n")
        print(sessions)
    elif x==2:
        print("====== Study Sessions ======")
        if len(sessions)==0:
            print("No study sessions recorded yet.")
        for i in range(len(sessions)):
            print(f"{i+1}. Topic: {sessions[i]['topic']} | Duration: {sessions[i]['minutes']}")
    elif x==3:
        print("====== Learning Summary ======")
        print(f"Total study time : {} minutes")
        
    elif x==4:
        print("Good Bye\n")
        break
    else:
        print("Invalid Choice, Try again.\n")

