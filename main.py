import json

try:
    with open("sessions.json","r") as file:
        sessions=json.load(file)
except FileNotFoundError or :
    sessions = []

def save_sessions(sessions):
    with open("sessions.json","w") as file:
        json.dump(sessions,file,indent=4)

while True:
    print("=======================")
    print("Study Sprint Tracker")
    print("=======================")
    print("1. Add study session")
    print("2. View study sessions")
    print("3. Show learning summary")
    print("4. Exit\n")

    try:
        x = int(input("Choose an option: "))
        print("\n")
    except ValueError:
        print("Invalid Choice, Try again.\n")
        continue
    if x==1:
        while True:
            study_topic = input("Enter Study topic (eg: Python, DSA, JavaScript) :").strip()
            if not study_topic.strip():
                print("Topic name should not be empty.")
                continue
            try:
                duration = int(input("Enter duration in minutes (eg: 45) :"))
                if duration<=0:
                    print("Duration should not be negative or zero")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid Duration, Try again.\n")
                continue
        new_session = {
            "topic":study_topic,
            "minutes":duration
        }
        sessions.append(new_session)
        save_sessions(sessions)
        print("Adding a study session.\n")
    elif x==2:
        print("====== Study Sessions ======")
        if not sessions:
            print("No study sessions recorded yet.")
        for i in range(len(sessions)):
            print(f"{i+1}. Topic: {sessions[i]['topic']} | Duration: {sessions[i]['minutes']} minutes")
    elif x==3:
        print("====== Learning Summary ======")

        if len(sessions)==0:
            print("No study sessions recorded yet.\n")
        else:
            total_min=0
            topic_total={}
            for session in sessions:
                topic = session["topic"]
                minutes = session["minutes"]
                total_min+=minutes
                if topic in topic_total:
                    topic_total[topic]+=minutes
                else:
                    topic_total[topic]=minutes
            print(f"Total study time : {total_min} minutes")
            print("\nTime by topic :\n")
            for topic, minutes in topic_total.items():
                print(f"\t{topic} : {minutes} minutes")
            print("\n")
    elif x==4:
        print("Good Bye\n")
        break
    else:
        print("Invalid Choice, Try again.\n")

