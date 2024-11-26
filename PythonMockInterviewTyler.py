import requests

url = "https://api.travelpayouts.com/v2/prices/month-matrix"
querystring = {"currency":"usd","show_to_affiliates":"true","origin":"NYC","destination":"LAX"}
headers = {'x-access-token': '2160a9f9ca2fa3d348f4a3a32504538e'}
response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.json())
# Get flight information for departure date 10.21.2024

flight_data=response.json()
# print(flight_data['data'])

for trip in flight_data['data']:
    if trip['depart_date'] == '2024-10-21':
        print(trip)
