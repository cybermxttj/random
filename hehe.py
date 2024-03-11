import os

# Specify the custom path to your desktop
custom_desktop_path = "/home/mattj/Desktop"

# Create the full path for the hello.txt file
file_path = os.path.join(custom_desktop_path, "hello.txt")

# Write the desired text into the file
with open(file_path, "w") as file:
    file.write("gottcha")

print(f"File 'hello.txt' created successfully on your custom desktop path!")

