import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../day02-pandas/processed_sensor_data.csv")

plt.bar(df["sensor"], df["value"])

plt.xlabel("Sensors")
plt.ylabel("Values")
plt.title("Processed Sensor Data")

plt.xticks(rotation=30)
plt.grid(axis="y")

plt.show()

status_count = df["status"].value_counts()

print(status_count)
plt.bar(status_count.index, status_count.values)

plt.xlabel("Status")
plt.ylabel("Number of Sensors")
plt.title("Sensor Status Distribution")
plt.grid(axis="y")
plt.savefig("sensor_status_distribution.png")
plt.show()
print(status_count.idxmax())
