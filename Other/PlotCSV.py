import pandas as pd
import plotly.express as px

# === INPUT FILE ===
csv = 'images_2007384.csv' 

# Load cleaned CSV
df = pd.read_csv(csv)

# convert timestamp column
df["timestamp"] = pd.to_datetime(df["timestamp"])

# group by date and count
df["date"] = df["timestamp"].dt.date
daily_counts = df.groupby("date").size().reset_index(name="image_count")

# create interactive line chart
fig = px.line(daily_counts, x="date", y="image_count", title="Total Images Captured Over Time")

# open in browser
fig.show()
