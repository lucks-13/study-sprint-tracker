import json

sessions = [
    {"topic":"Python","miniutes":60},
    {"topic":"Django","minutes":45},
    {"topic":"DSA","minutes":30}
]

with open("sessions.json","w") as file:
    json.dump(sessions, file, indent=4)

with open("sessions.json","r") as file:
    loaded_sessions = json.load(file)

print(loaded_sessions[0]["topic"])