import os
import requests

# 1. Retrieve API key from environment variable
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API key not found. Please set the API_KEY environment variable.")
    exit()

# 2. API endpoint (FIXED LINE ✅)
url = "https://jsonplaceholder.typicode.com/posts/1"

# 3. Headers with Authorization Bearer format
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

try:
    # Send GET request
    response = requests.get(url, headers=headers)

    # 4. Handle status codes
    if response.status_code == 200:
        print("Success! JSON Response:")
        print(response.json())

    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")

    else:
        print("Request failed")
        print(f"Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Error occurred while making the request:")
    print(e)