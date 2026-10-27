import json

sessions = [
    {"topic":"Python","miniutes":60},
    {"topic":"Django","minutes":45},
    {"topic":"DSA","minutes":30}
]

with open("sessions.json","w") as file:
    json.dump(sessions, file, indent=4)