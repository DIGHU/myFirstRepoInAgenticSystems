import requests

# API URL
url = "https://api.github.com/search/repositories"

# Query parameters
params = {
    "q": "python",          # search keyword
    "sort": "stars",       # sort by stars
    "order": "desc",       # descending order
    "per_page": 5          # limit to 5 results
}

# Send GET request
response = requests.get(url, params=params)

# Convert response to JSON
data = response.json()

# Print results
print("Top 5 Python Repositories:\n")

for repo in data["items"]:
    print(f"Name: {repo['name']}")
    print(f"Stars: {repo['stargazers_count']}")
    print("-" * 30)