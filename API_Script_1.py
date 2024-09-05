# Alright, so I incorporated 2(!!!) API calls in this script in order to 1) turn the users city input into latitude and longitude coordinates
# And 2) to input those coordinates as the parameters for our weather API
# First, we import the module necessary to make API requests, the "requests" api
import requests

# We establish two While loops below - one overarching loop to ask the User if they'd like to request the weather for another city
# And another to error check if the city entered for coordinate translation is an actual city
while True:
    while True:
        address=input("Hello! To get the weather forcast for a city, please input one: ")  # This prompts the User for the City they want to see the weather for and stores that input in the "address" variable

        url = "https://address-from-to-latitude-longitude.p.rapidapi.com/geolocationapi"   # This is the url for the coordinate translation for our first API call

        querystring = {"address":address}  # Here, we use the city stored in the address variable as the parameter for the coordinate translation API

        headers = {  # Here is our authentication token and host URL for API access
            "x-rapidapi-key": "ceb3ef7572msh279a78c07ebbdcep18ba20jsn93715b70267d",
            "x-rapidapi-host": "address-from-to-latitude-longitude.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        if len(response.json()["Results"]) > 0:     #len here allows us to measure the amount of items in the "response.json()" array - if there are no items in the array, then we know the location stored in the address variable is not valid
            break
        elif print("That is not an actual city, silly! Please input an actual city on this here Planet Earth."):
            continue   # continue will loop the inner while loop again, allowing the user to input a new, valid city


    lat = response.json()["Results"][0]["latitude"]   # The response.json() for our coordinates API usually gives many different cities based on relevancy to the city given by the user, so here, we store the lat and longitude data for only the FIRST [0] item in the array, as that is usually the most accurate to the requested city
    long = response.json()["Results"][0]["longitude"] # We then store the lat and long coordinates in two separate variables in order to adhere to the syntax needed for our weather API parameters


    url = "https://weatherapi-com.p.rapidapi.com/current.json"   # The beginning of our second API! This is also an example of the nifty trick with variables in Python - the latest variable stored will supersede the old one, allowing you to use the same variable name multiple times in a script

    querystring = {"q":f"{lat}, {long}"}   # Here;s the lat and long variable substitution I spoke of early. f-string allows us to easily input the variables into the querystring in the same syntax as the parameters would be if we just ran the API by itself

    headers = {
        "x-rapidapi-key": "ceb3ef7572msh279a78c07ebbdcep18ba20jsn93715b70267d",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    weather=response.json()   # we store the response.json in a single variable here, to make it easier to work with

    # Below, we create a more simplified version of the .json and store it the weather_simple dictionary. This dictionary only has the key and value pairs we will print in our final print statement
    weather_simple={
        "temp_f":weather["current"]["temp_f"],
        "location":weather["location"]["name"],
        "country":weather["location"]["country"],
        "region":weather["location"]["region"],
        "rain":weather["current"]["precip_mm"],
    }

   
    # Below, we assigin our values from the simplified dictionary to varaibles, so we can more easily cite them in our final print statement. Assigning a variable to the rain value also helps us create the final if comparison statement to print out the correct statement regarding rain in the searched location.
    for key, value in weather_simple.items():
        if key == "temp_f":
            temp = value
        if key == "location":
            city = value
        if key == "country":
            country = value
        if key == "region":
            region = value
        if key =="rain":
            rain = value

    # And here are our final print statements, with the amount of rain (in mm instead of in) determining which print statement the user gets. 
    if rain == 0.0:
        print(f"It is currently {temp} degrees Fahrenheit in {city}, {region}, {country}, and it is not raining! You can safely step outside your home.")
    elif rain <= 3.0:
        print(f"It is currently {temp} degrees Fahrenheit in {city}, {region}, {country}, and it is lightly raining outside. You should bring an umbrella.")
    elif rain >= 3.0:
        print(f"It is currently {temp} degrees Fahrenheit in {city}, {region}, {country}, and it is raining heavily outside. I'd stay home if I were you!")

    # And there goes our prompt to see if the user would like to check the weather in another city (with our old friend, casefold, to ensure any Y is allowed as an answer).
    try_again=input("Would you like to see the current weather in another city? (y/n): ").casefold()
    if try_again == "y":
        continue
    break
        
