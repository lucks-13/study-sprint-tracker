print("=======================")
print("Study Sprint Tracker")
print("=======================")
print("1. Add study session")
print("2. View study sessions")
print("3. Show learning summary")
print("4. Exit\n")

while (True):
    x=int(input("Choose an option:"))
    print("\n")
    if x<=4 and x>=1:
        break

if x==1:
    print("Adding a study session")
