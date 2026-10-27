import json

sessions = [
    {"topic":"python","miniutes":45},
    {"topic":"dsa","minutes":30}
]

with open("sessions.json","w") as file:
    json.dump(sessions, file, indent=4)