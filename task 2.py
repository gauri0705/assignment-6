#Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json
x= {"Karnataka":"Bangalore" , "Goa":"Panji" , "Mumbai":"Maharastra" , "Bihar":"Patna" , "Andhra Pradesh":"Amaravati" , "Himachal Pradesh":"Shimla" , "Kerala":"Thiruvananthapuram"}
json_string=json.dumps(x)
print(json_string)