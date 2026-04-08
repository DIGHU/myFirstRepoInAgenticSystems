import requests
import pandas as pd

# Step 1: Fetch data from API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

data = response.json()

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Basic Cleaning
df.rename(columns={"userId": "user_id"}, inplace=True)
df.drop(columns=["id"], inplace=True)

# Step 4: EDA - posts per user
posts_per_user = df.groupby("user_id").size().reset_index(name="post_count")

# Step 5: New column (post_length)
df["post_length"] = df["body"].apply(len)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
posts_per_user.to_csv("posts_per_user.csv", index=False)

print("Data fetched and saved successfully!")