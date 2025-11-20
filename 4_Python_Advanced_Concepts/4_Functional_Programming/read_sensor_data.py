with open('E:\\Mentorhints\\Workspace\\course-materials\\3_Python_Intermediate_Fundamentals\\10_Functional_Programming\\sensor_data.txt', 'r') as sensor_data:
    data = sensor_data.readlines()

print("Sensor Data (Before Processing):")
print(data)

cleaned_data = list(map(int, list(map(lambda x: x.strip(), data))))
print("Sensor Data (After Processing):")
print(cleaned_data)

# Remove invalid readings (-9999999)
valid_data = list(filter(lambda x: x != -9999999, cleaned_data))
print("Sensor Data (Valid Readings):")
print(valid_data)