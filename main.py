print("=======================")
print("Study Sprint Tracker")
print("=======================")
print("1. Add study session")
print("2. View study sessions")
print("3. Show learning summary")
print("4. Exit\n")

while (True):
    x=int(input("Choose an option:"))
    if x<=4 and x>=1:
        break
    print("Invalid Choice, Try again.")

if x==1:
    print("Adding a study session.")
elif x==2:
    print("Viewing study session.")
elif x==3:
    print("Showing learning summary.")
elif x==4:
    print("Good Bye")
