import pandas as pd

data = {
"Name":["Alice","Bob","Charlie","David","Eva"],
"Age":[22,21,23,20,24],
"Score":[85,70,92,60,88],
"Label":[1,0,1,0,1]
}

df = pd.DataFrame(data)

df.to_csv("dataset.csv", index=False)

print("dataset.csv created successfully")
