import pandas as pd

sensor_data = {
    "sensor": ["temperature", "humidity", "Distance"],
    "value": [25, 60, 120],
}
df = pd.DataFrame(sensor_data)
# print(df)
# print(df["value"])
# print(df["value"].mean())
# print(df["value"].max())
# print(df["value"].min())

# print(df[df["value"] > 50])
# df["status"] = "normal"
# df.to_csv("sensor_data_csv", index=False)
# df.loc[len(df)] = ["pressure", 45, "normal"]
# df.loc[len(df)] = ["light", 80, "normal"]
# df.loc[df["value"] > 50, "status"] = "high"
# # print(df)
# df.loc[df["value"] < 30, "status"] = "low"
# # print(df)
# df.to_csv("sensor_data.csv", index=False)

new_df = pd.read_csv("sensor_data.csv")

# print(new_df)
# print(len(new_df))
# print(new_df["value"].mean())
# print(new_df[new_df["status"] == "high"])
new_df.loc[2, "value"] = None
# print(new_df)
# print(new_df.isnull())
# print(new_df["value"].isnull().sum())
mean_value = new_df["value"].mean()
new_df["value"] = new_df["value"].fillna(mean_value)
# print(new_df["value"].isnull().sum())
up_avg = new_df["value"].mean()
# print(up_avg)
# print(new_df["value"].max())

# sorted_df = new_df.sort_values(by="value", ascending=False)
# print(sorted_df[["sensor", "value"]].head(2))

gruped_df = new_df.groupby("status")["value"].max()
# print(gruped_df)

print(new_df.describe())
