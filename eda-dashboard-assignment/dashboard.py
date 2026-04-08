import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("EDA Dashboard")

# Load data
df = pd.read_csv("cleaned_data.csv")
posts_per_user = pd.read_csv("posts_per_user.csv")

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Bar chart: Posts per user
st.subheader("Posts per User")
st.bar_chart(posts_per_user.set_index("user_id"))

# Histogram: Post Length
st.subheader("Post Length Distribution")

fig, ax = plt.subplots()
ax.hist(df["post_length"], bins=20)
st.pyplot(fig)