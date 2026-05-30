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
    
    
    