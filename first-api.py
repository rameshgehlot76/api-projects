# 1st API Example in Python  
# Real-Time Currency Converter (With API)  
import requests 

API_URL = "https://api.exchangerate-api.com/v4/latest/USD" 

amount = float(input("Enter amount: ")) 
from_currency = input("From (USD/EUR/GBP/JPY/INR): ").upper()
to_currency = input("To (USD/EUR/GBP/JPY/INR): ").upper() 

# Make the GET request  
response = requests.get(API_URL) 
data = response.json()
rates = data["rates"] 

if from_currency in rates and to_currency in rates:
    result = amount * rates[to_currency] / rates[from_currency]
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}") 
else:
    print("Invalid currency code")



# 2nd API Example 
# How to connect to an API using Python 
import requests 

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name): 
    url = f"{base_url}/pokemon/{name}" 
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        print(f"Name: {pokemon_data['name'].capitalize()}") 
        print(f"ID: {pokemon_data['id']}") 
        print(f"Height: {pokemon_data['height']}")
        print(f"Weight: {pokemon_data['weight']}") 
        print("Abilities:")
        for ability in pokemon_data['abilities']:
            print(f" - {ability['ability']['name']}") 
    else:
        print(f"Failed to retrieve data for {name}. Status code: {response.status_code}") 


pokemon_name = input("Enter Pokemon name: ").lower()  
get_pokemon_info(pokemon_name)            




# 3rd API Example 
# How to make an API call? 
# Python example using the requests library:

import requests 
# The API endpoint URL 
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Make the GET request
response = requests.get(url) 

# Check if the request was succesful 
if response.status_code == 200:
    # Parse the JSON response  
    data = response.json() 
    print(data) 
else:
    print(f"Error: Unable to fetch data. Status code {response.status_code}") 
 



# FastAPI Example 
'''
python 3.6+
pip install fastapi uvicorn
''' 
from fastapi import FastAPI

app = FastAPI() 
@app.get('/')
def hello_world():
    return {'Hello':'World'} 
# To run the server: uvicorn filename:app --reload 


# 2nd
from fastapi import FastAPI 
app = FastAPI() 
@app.get("/items/") 
def read_word():
    return [{"name": "Ramesh"}, {"name": "Suresh"}]

# To run the server: uvicorn filename:app  --reload 



