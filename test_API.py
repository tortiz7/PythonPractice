import requests
import pprint

url = "https://free-api-live-football-data.p.rapidapi.com/football-league-heatmap-overall"

querystring = {"playerid":"827606","leagueid":"17","seasonid":"52186"}

headers = {
	"x-rapidapi-key": "ceb3ef7572msh279a78c07ebbdcep18ba20jsn93715b70267d",
	"x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

test = response.json()

pprint.pprint(test["response"]["count"])

# print(response.json())