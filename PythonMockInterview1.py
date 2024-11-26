import requests

url = "https://api.travelpayouts.com/v2/prices/month-matrix"
querystring = {"currency":"usd","show_to_affiliates":"true","origin":"NYC","destination":"LAX"}
headers = {'x-access-token': '2160a9f9ca2fa3d348f4a3a32504538e'}
response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.json())
# Get flight information for departure date 10.21.2024

flight_data=response.json()
#print(flight_data)
print(flight_data['data'][1]['destination'])

# print(flight_data)
# print(myfamily["child2"]["name"])

# for items in raw["Stages"]:
    # print({items.get("Sid")})

#try: 
    #for flight in flight_data["data"]:
        #if flight["depart_date"] == "2024-10-21":
            #print(f"Your flight to {flight['destination']} from {flight['origin']} will take {flight['duration']}mins long, but you'll have a wonderful time when you get there!")

# # for items in flight_data["data"]:
#     # ({items.get("depart_date")})
#     if items["depart_date"] == "2024-10-21":
#         print(f"Your flight to {items['destination']} from {items['origin']} will take {items['duration']}mins long, but you'll have a wonderful time when you get there!")



   
    


#for items, values in flight_data.items("data"):



