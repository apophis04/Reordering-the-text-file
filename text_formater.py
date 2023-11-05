# Read the input text file
with open('data.txt', 'r') as file:
    lines = file.readlines()

# Initialize variables
rearranged_data = {}
current_serial = None

# Define the order you want
order = ["First name", "Telephone number", "Middle name", "Last name"]

# Process the lines and rearrange the data
for line in lines:
    line = line.strip()
    if line.isnumeric():
        current_serial = int(line)
        rearranged_data[current_serial] = {key: "" for key in order}
    else:
        parts = line.split(': ', 1)
        if len(parts) == 2:
            key, value = parts
            if key in order and current_serial is not None:
                rearranged_data[current_serial][key] = value

# Save the rearranged data to a new text file
with open('converted.txt', 'w') as outfile:
    for serial, data in sorted(rearranged_data.items()):
        outfile.write(str(serial) + '\n')
        for key in order:
            outfile.write(key + ": " + data[key] + '\n')
        outfile.write('\n')
