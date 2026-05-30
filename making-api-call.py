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
 


