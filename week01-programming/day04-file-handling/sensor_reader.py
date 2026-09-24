try:
    with open("sensor_log.txt", "r") as file:
        for line in file:
            if not line.strip():
                continue

            parts = line.split(":")

            sensor = parts[0].strip()
            value = int(parts[1].strip())

            print("Sensor :", sensor, "| Value :", value)

except FileNotFoundError:
    print("File not found")

except ValueError:
    print("Invalid value")

finally:
    print("Sensor reading completed")
