import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("typing_data.csv", header=None, names=["Username", "Timestamp", "WPM", "Time"])
df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

# Convert "Time" to MM:SS format
df["Time"] = pd.to_datetime(df["Time"], unit="s").dt.strftime("%M:%S")

# Streamlit UI
st.title("Typing Speed Test Analysis")

# Select user
usernames = df["Username"].unique()
selected_user = st.selectbox("Select User:", usernames)

# Filter data
user_data = df[df["Username"] == selected_user]

# Display data
st.write(user_data)

# Plot Performance Trend
st.subheader("Typing Speed Over Time")
fig, ax = plt.subplots()
ax.plot(user_data["Timestamp"], user_data["WPM"], marker="o", linestyle="-", color="b", label="WPM")
ax.set_xlabel("Timestamp")
ax.set_ylabel("Words Per Minute")
ax.set_title(f"Performance Trend of {selected_user}")
ax.grid()
ax.legend()
plt.xticks(rotation=45)  
st.pyplot(fig)
