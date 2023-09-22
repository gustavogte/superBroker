import csv
import os

# File paths
input_file = 'data.csv'
output_file = 'data_modified.csv'

# Open the input file for reading and the output file for writing
with open(input_file, 'r') as csvfile, open(output_file, 'w', newline='') as modified_csvfile:
    
    # Create a DictReader
    reader = csv.DictReader(csvfile)
    
    # Create a DictWriter with the same fieldnames
    writer = csv.DictWriter(modified_csvfile, fieldnames=reader.fieldnames)
    
    # Write the headers to the new file
    writer.writeheader()
    
    # Iterate over each row in the input CSV
    for row in reader:
        # Check if the name is "Bob"
        if row['name'] == 'Bob':
            # Increment the age
            row['age'] = str(int(row['age']) + 1)
        
        # Write the modified (or unmodified) row to the new CSV
        writer.writerow(row)

# Remove the original file
os.remove(input_file)

# Rename the modified file to the original file name
os.rename(output_file, input_file)
