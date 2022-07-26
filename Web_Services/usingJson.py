## This python script demonstrates the use of JSON by importing its library and extracting information from a JSON string

import json
data = '''
  [
    { "id" : "001",
      "age" : "27",
     "name" : "Mkurugenzi"
    } ,
    { "id" : "009",
      "age" : "75",
      "name" : "Deborah"
    }
  ]
'''

# The data is then processed by python to obtain required data
info = json.loads(data)
print("Content Number: ", len(info))
for item in info:
    print("Name: ", item['name'])
    print("Age: ", item['age'])
    print("Id: ", item['id'])