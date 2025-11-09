print()
print()
data = input("Enter some data to write to file: ")
mode = input("Do you want to append (a) or write (w) to the file?")

append_options = ['a', 'append', 'app']
write_options = ['w', 'write', 'wr']

if mode.lower() in append_options:
    file_mode = 'a'
elif mode.lower() in write_options:
    file_mode = 'w'
else:
    print("Invalid mode selected.")
    exit()

file1 = open("E:\\Mentorhints\\Workspace\\course-materials\\4_Python_Advanced_Concepts\\2_File_Handling\\file1.txt", file_mode)
file1.write(data + "\n")
file1.close() 

print("Data written to file successfully.")