#!/usr/bin/python                                                               

# Load the JSON module and use it to load your JSON file.  
# import json files                                      
import json
obj  = json.load(open("sensor_data.json"))

# Iterate through the objects in the JSON and pop (remove)                      
# the obj once we find it. 
# remove the redundant value if we find the error as -999 in Oxygen saturation                                                     
for i in range(len(obj)):
    if obj[i]["data"] == -999:
        obj.pop(i)
        break


# Output the updated file with pretty JSON                                      
open("sensor_data.json", "w").write(json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))
