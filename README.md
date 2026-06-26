# 🌐 API Projects — Python & FastAPI Learning Journey

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP%20Library-orange?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> A hands-on collection of Python programs demonstrating how to **consume REST APIs**, **work with real-world data**, and **build APIs using FastAPI** — from beginner to practical level.

---

## 📁 Project Structure 
```
api-projects/
│
├── real-time-currency-converter.py   # Live forex rates using ExchangeRate API
├── connect-api-using-python.py       # Pokémon data via PokéAPI
├── making-api-call.py                # Intro to GET requests with JSONPlaceholder
└── fastapi.py                        # Building REST APIs using FastAPI
```

---

## 🚀 Projects Overview 

### 💱 1. Real-Time Currency Converter
**File:** `real-time-currency-converter.py`

Converts currency amounts in real time using live exchange rates from the ExchangeRate API.

- Fetches live rates via HTTP GET request
- Supports USD, EUR, GBP, JPY, INR
- Calculates cross-currency conversion using rate ratio formula

```bash
python real-time-currency-converter.py
# Enter amount: 1000
# From: INR  →  To: USD
# Output: 1000 INR = 11.97 USD
```

**API Used:** `https://api.exchangerate-api.com/v4/latest/USD`

---

### 🎮 2. Pokémon Info Fetcher
**File:** `connect-api-using-python.py`

Fetches real-time Pokémon data (ID, height, weight, abilities) from the public PokéAPI.

- Makes a GET request to a dynamic URL with user input
- Handles HTTP status codes (200 vs errors)
- Parses nested JSON response

```bash
python connect-api-using-python.py
# Enter Pokemon name: pikachu
# Name: Pikachu | ID: 25 | Height: 4 | Weight: 60
# Abilities: static, lightning-rod
```

**API Used:** `https://pokeapi.co/api/v2/pokemon/{name}`

---

### 📬 3. Making an API Call (Beginner)
**File:** `making-api-call.py`

Introductory example showing the complete anatomy of an API call — request, response, status check, and JSON parsing.

- Uses JSONPlaceholder (free fake REST API for testing)
- Demonstrates `response.status_code` and `response.json()`
- Clean error handling with else block

**API Used:** `https://jsonplaceholder.typicode.com/posts/1`

---

### ⚡ 4. FastAPI — Build Your Own API
**File:** `fastapi.py`

Demonstrates how to **build** a REST API from scratch using FastAPI — the modern, high-performance Python framework.

```python
# Endpoint 1: Hello World
GET /  →  {"Hello": "World"}

# Endpoint 2: Items List
GET /items/  →  [{"name": "Ramesh"}, {"name": "Suresh"}]
```

**Run the server:**
```bash
uvicorn fastapi:app --reload
```
Then open: `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| `requests` | Consuming external REST APIs (HTTP GET) |
| `FastAPI` | Building REST API endpoints |
| `uvicorn` | ASGI server to run FastAPI |
| ExchangeRate API | Live forex/currency rates |
| PokéAPI | Pokémon data (public, no auth needed) |
| JSONPlaceholder | Fake REST API for testing & learning |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10 or above
- pip

### Clone the repo
```bash
git clone https://github.com/rameshgehlot76/api-projects.git
cd api-projects
```

### Install dependencies
```bash
pip install requests fastapi uvicorn
```

### Run any script
```bash
python real-time-currency-converter.py
python connect-api-using-python.py
python making-api-call.py
```

### Run FastAPI server
```bash
uvicorn fastapi:app --reload
```

---

## 💡 Key Concepts Learned

- What an API is and how HTTP requests (GET) work
- Parsing and navigating JSON responses in Python
- Handling API errors using `status_code` checks
- Making dynamic API calls with user input
- Building REST API endpoints using FastAPI
- Understanding API endpoints, routes, and responses
- How `requests.get()`, `response.json()`, and status codes work together

---

## 📈 What's Next

- [ ] Add POST request examples
- [ ] Add API key authentication examples
- [ ] Build a weather app using OpenWeatherMap API
- [ ] Add FastAPI with Pydantic models and request body
- [ ] Deploy a FastAPI project on Render or Railway

---

## 👨‍💻 Author

**Ramesh Gehlot**

[![GitHub](https://img.shields.io/badge/GitHub-rameshgehlot76-181717?style=flat&logo=github)](https://github.com/rameshgehlot76)  

---

Built with dedication 🚀

> ⭐ If this helped you understand APIs better, consider giving this repo a star!

