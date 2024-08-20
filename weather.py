import requests

# Define the API endpoint
api_endpoint = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc&station=ALL"

# Send a request to the API
response = requests.get(api_endpoint)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful.")
    
    # Parse the response as JSON
    data = response.json()

    # Extract relative humidity
    max_humidity = data['weatherForecast'][1]['forecastMaxrh']['value']
    min_humidity = data['weatherForecast'][1]['forecastMinrh']['value']
    print(f"Relative Humidity for the day after tomorrow is: {min_humidity}-{max_humidity}%")
else:
    print(f"Request failed with status code: {response.status_code}")