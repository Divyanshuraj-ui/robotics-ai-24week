# lst = [23, 25, 22, 27, 24]


# def analyze_sensor_data(lst):
#     count = 0
#     for i in lst:
#         count += i
#     avg = count / len(lst)
#     print(
#         f"Total Readings : {len(lst)} \n Average : {avg} \n Maximum : {max(lst)} \n Minimum : {min(lst)}"
#     )


# analyze_sensor_data(lst)

# sensor_data = {"temperature": 25, "humidity": 60, "distance": 120}
# for i, y in sensor_data.items():
#     print(i, ":", y)


# class Sensor:
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value

#     def display(self):
#         print(f"Sensor : {self.name} \n Value : {self.value}")


# s1 = Sensor("temperature", 25)
# # print(f"Sensor : {s1.name} \n Value : {s1.value}")
# s1.display()
# s2 = Sensor("humidity", 60)
# s3 = Sensor("distance", 120)
# s2.display()
# s3.display()

import numpy as np

sensor_data = np.array([23, 25, 22, 27, 24])

# print(sensor_data)
# print(type(sensor_data))
# print(
#     f"Mean : {np.mean(sensor_data)} \n Max : {np.max(sensor_data)} \n Min : {np.min(sensor_data)} \n Sum : {np.sum(sensor_data)}"
# )

# print(
#     f"First value : {sensor_data[0]} \n Last value : {sensor_data[-1]} \n first three values : {sensor_data[0:3]}"
# )

print(f"{sensor_data[sensor_data > 24]}")
new_data = sensor_data * 2
print(new_data)
