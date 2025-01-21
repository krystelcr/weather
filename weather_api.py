import requests
import json
import pandas as pd 

#path to save the json data
jsondirectory = "data/json/data.json"
#path to save the csv file
csvdirectory = "data/csv/data.csv"

#url for the json data
URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"

#gets the json data from the api
page = requests.get(URL)
data = page.json()

#saves the json data to file
with open(jsondirectory, "w") as file:
    json.dump(data, file, indent = 4)

#convert json data into a pandas dataframe
df = pd.DataFrame(data)

#extract hourly data from the json
hourly_data = data["hourly"]
#dictionary with the hourly requested data fields
dicct = {
    "time": hourly_data ["time"],
    "temperature_2m": hourly_data ["temperature_2m"],
    "relative_humidity_2m": hourly_data ["relative_humidity_2m"],
    "precipitation": hourly_data ["precipitation"],
    "surface_pressure": hourly_data ["surface_pressure"]

}
#dictionary converted into a pandas dataframe
df= pd.DataFrame(dicct)

#save the dataframe to a csv file
df = df.to_csv(csvdirectory)