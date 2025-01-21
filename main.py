import csv

# Function to convert .txt to .csv
def txt_to_csv(input_file, output_file):
    # Open the .txt file for reading
    with open(input_file, mode="r") as file:
        # Read the content from the file
        data = file.read()

    # Split the data by lines
    lines = data.strip().split("\n")

    # Open the .csv file for writing
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        
        # Write header (column names)
        header = lines[0].split(",")
        writer.writerow(header)
        
        # Write the data rows
        for line in lines[1:]:
            row = line.split(",")
            writer.writerow(row)

    print(f"CSV file '{output_file}' has been created successfully!")

# Specify input .txt file and output .csv file
input_txt = "file.txt"  # Replace with your .txt file name
output_csv = "output.csv"  # Replace with your desired .csv file name

# Call the function to convert
txt_to_csv(input_txt, output_csv)
