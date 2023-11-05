# Read the input text file
with open('data.txt', 'r') as file:
    lines = file.readlines()

# Initialize variables
rearranged_data = []
current_entry = {}

# Define the order you want
order = ["First name", "Telephone number", "Middle name", "Last name"]

# Helper function to reset the current entry
def reset_current_entry():
    current_entry.clear()
    for key in order:
        current_entry[key] = ""

# Process the lines and rearrange the data
for line in lines:
    if line.strip().isnumeric():
        reset_current_entry()
    else:
        parts = line.strip().split(': ', 1)
        if len(parts) == 2:
            key, value = parts
            if key in order:
                current_entry[key] = value

    if all(current_entry.values()):
        rearranged_data.append(current_entry.copy())
        reset_current_entry()

# Save the rearranged data to a new text file
with open('output.txt', 'w') as outfile:
    for entry in rearranged_data:
        for key in order:
            outfile.write(key + ": " + entry[key] + '\n')
        outfile.write('\n')
