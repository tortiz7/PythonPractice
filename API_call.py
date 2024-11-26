import requests

url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

querystring = {"Category":"tennis","Timezone":"-7"}

headers = {
	"x-rapidapi-key": "ceb3ef7572msh279a78c07ebbdcep18ba20jsn93715b70267d",
	"x-rapidapi-host": "livescore6.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

raw=response.json()

print(raw)

# for items in raw["Stages"]:
    # print({items.get("Sid")})

# print(raw.items())
# print(raw.keys())
# print(raw.items())
# print(raw.values())


