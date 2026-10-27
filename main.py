import json
import os

def get_data_file():
    app_data = os.environ.get("LOCALAPPDATA")
    if not app_data:
        raise RuntimeError("Windows application data directory not found.")
    data_dir = os.path.join(app_data,"study-sprint-tracker")
    os.makedirs(data_dir,exist_ok=True)
    return os.path.join(data_dir,"sessions.json")
    
def load_sessions():
    try:
        with open("sessions.json","r") as file:
            sessions=json.load(file)
    except FileNotFoundError:
        sessions = []
    except json.JSONDecodeError:
        print("session.json contains invalid Json, Please check the file before continuing")
        raise SystemExit(1)
    if not isinstance(sessions,list):
        print("sessions.json must contain a json list.")
        raise SystemExit(1)
    return sessions

def save_sessions(sessions):
    with open("sessions.json","w") as file:
        json.dump(sessions,file,indent=4)

def add_session(sessions):
    while True:
        study_topic = input("Enter Study topic (eg: Python, DSA, JavaScript) :").strip()
        if not study_topic:
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
    return sessions

def view_sessions(sessions):
    print("====== Study Sessions ======")
    if not sessions:
        print("No study sessions recorded yet.")
    for i in range(len(sessions)):
        print(f"{i+1}. Topic: {sessions[i]['topic']} | Duration: {sessions[i]['minutes']} minutes")

def show_summary(sessions):
    print("====== Learning Summary ======")
    if len(sessions)==0:
        print("No study sessions recorded yet.\n")
        return
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

def main():
    sessions = load_sessions()
    try:
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
                sessions=add_session(sessions)
            elif x==2:
                view_sessions(sessions)
            elif x==3:
                show_summary(sessions)
            elif x==4:
                print("Good Bye\n")
                break
            else:
                print("Invalid Choice, Try again.\n")
    except KeyboardInterrupt:
        print("\n Program interrupted. Good Bye")

if __name__ == "__main__":
    main()
