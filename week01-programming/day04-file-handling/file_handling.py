# file = open("sensor_log.txt", "w")

# file.write("Temperature: 25\n")
# file.write("Humidity: 60\n")
# file.write("Distance: 120\n")
# file.write("Pressure: 45\n")
# file.close()

# file = open("sensor_log.txt", "r")
# for line in file:
# print(line.strip())
# content = file.read()

# print(content)

# file.close()

# file = open("sensor_log.txt", "a")
# file.write("GAS : 70\n")
# file.close()

# file = open("sensor_log.txt", "r")
# for line in file:
#     print(line.strip())

# with open("sensor_log.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# try:
#     with open("abc.txt", "r"):
#         for line in file:
#             print(line.strip())
# except FileNotFoundError:
#     print("Sensor file not found")


# try:
#     with open("sensor_log.txt", "r") as file:
#         line = file.readline()

#         parts = line.split(":")
#         value = int(parts[1].strip())
#         print("Sensor value: ", value)
# except FileNotFoundError:
#     print("File not found")

# except ValueError:
#     print("Invalid sensor value")

# finally:
#     print("Program finished")

