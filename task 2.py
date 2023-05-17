#Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json
x= { "Mumbai":"Maharastra" ,"asam":"dispur", "Bihar":"Patna" , "gujrat":"gandhinagar", "Himachal Pradesh":"Shimla" , "Kerala":"Thiruvananthapuram","Karnataka":"Bangalore"}
json_string=json.dumps(x)
print(json_string)