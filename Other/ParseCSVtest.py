import pandas as pd
import matplotlib.pyplot as plt
#plotly


# load CSV (dataframe struct)
df = pd.read_csv("images_2007384.csv")

# check column names
#print("Columns: ", df.columns.tolist())

# show first 5 rows
#print(df.head())

# get number of rows and columns
#print("Shape of Data: ", df.shape)

# basic info about dataset
#print(df.info())

# show summary stats (numerical columns
#print(df.describe())

#print(df.isnull().sum()) #count missing values per column
#print (df.duplicated().sum()) #count duplicate rows

print(df["timestamp"].dtype) # timestamp column is of 'object' dt

df["timestamp"] = pd.to_datetime(df["timestamp"]) #convert object dt timestamps to datetime dt

df["date"] = df["timestamp"].dt.date #extract date only from timestamp
df["month"] = df["timestamp"].dt.to_period("M") #extract to month

image_counts_date = df.groupby("date").size() #count images per day
image_counts_month = df.groupby("month").size() #group by month!

# plt.figure(figsize=(10, 5))
# plt.plot(image_counts_date.index, image_counts_date.values, marker="o", linestyle="-")
# plt.xlabel("Date")
# plt.ylabel("Total Images Taken")
# plt.title("Total Images Captured Over Time")
# plt.xticks(rotation=45) # rotate dates for readability
# plt.grid(True)
# plt.show()
