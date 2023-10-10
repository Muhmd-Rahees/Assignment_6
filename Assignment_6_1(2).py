# 👉 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json

states_and_capitals = {
    "Tamil Nadu": "Chennai",
    "Himachal Pradesh" : "Shimla",
    "Karnataka" : "Bengaluru",
    "Maharashtra": "Mumbai",
    "Delhi": "New Delhi",
    "Kerala": "Thiruvananthapuram",
    "Rajasthan": "Jaipur"
}

with open('indianStates.json', 'w') as json_file:
    json.dump(states_and_capitals, json_file)

print("Successfully added to indian_states.json.")
