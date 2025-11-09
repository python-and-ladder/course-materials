data_file = open('E:\\Mentorhints\\Workspace\\course-materials\\4_Python_Advanced_Concepts\\2_File_Handling\\data.txt', 'r')
data = data_file.read(20)
data_file.close()

print(f"File name: {data_file.name}")
print(f"File mode: {data_file.mode}")
print(f"Is closed: {data_file.closed}")

print("File data:")
print(data)