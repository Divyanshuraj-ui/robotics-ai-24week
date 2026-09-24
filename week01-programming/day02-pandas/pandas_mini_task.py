import pandas as pd

sensor_data = {
    "sensor": ["temperature", "humidity", "distance", "pressure", "light", "gas"],
    "value": [28, 65, 110, 42, 85, None],
}

df = pd.DataFrame(sensor_data)
print(df)
print(df.isnull().sum())
avg = df["value"].mean()
df["value"] = df["value"].fillna(avg)
print(df)

df["status"] = "normal"
df.loc[df["value"] > 70, "status"] = "high"
df.loc[df["value"] < 30, "status"] = "low"
print(df)

sorted_df = df.sort_values(by="value", ascending=False)

print(sorted_df[["sensor", "value"]].head(3))

print(df["status"].value_counts())

mean_df = df.groupby("status")["value"].mean()
print(mean_df)

print(df["value"].describe())
df.to_csv("processed_sensor_data.csv", index=False)

print(sorted_df[["sensor", "value"]].head(1))
