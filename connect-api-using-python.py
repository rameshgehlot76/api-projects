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

pokemon_name = input("Enter Pokemon Name: ").lower()  
get_pokemon_info(pokemon_name)           

