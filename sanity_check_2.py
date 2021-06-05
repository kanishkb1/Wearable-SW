#importing libraries

import os
import json

with open('sensor_data.json') as json_data:
    data = json.load(json_data)
#delete file from Sensors object if value=-999
    for element in data["sensors"]:
        #del element['-999']
        element.pop('-999', None)

with open('dummy.json', 'w') as output_file:  
    json.dump(data, output_file)