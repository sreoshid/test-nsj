import os
import re

log_directory = r'C:\Users\srdasg\OneDrive - SAS\Desktop\KnowledgeSharing\ps_wrapper'  # Path to the log directory
output_directory = r'C:\Users\srdasg\OneDrive - SAS\Desktop\KnowledgeSharing\psDuplicate'  # Path to the output directory

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Regular expression pattern to extract the date and line
pattern = r"(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2},\d{3})\s+DEBUG\s+\[.*\]\s+\(.*\) (.*)"

# Iterate over log files in the directory 
for file_name in os.listdir(log_directory):
    if file_name.endswith('.log'):  # Consider only log files
        file_path = os.path.join(log_directory, file_name)
        output_file_name = f"{os.path.splitext(file_name)[0]}_duplicate.log"
        output_file_path = os.path.join(output_directory, output_file_name)

        # Extract dates and lines from the log file
        with open(file_path, 'r') as log_file:
            log_content = log_file.read()
            matches = re.findall(pattern, log_content)

        # Create a dictionary to store lines by date
        lines_by_date = {}

        # Find duplicate lines for each date
        for match in matches:
            date, line = match
            if date in lines_by_date:
                lines_by_date[date].append(line)
            else:
                lines_by_date[date] = [line]

        # Find duplicate lines for each date
        duplicate_lines_by_date = {date: lines for date, lines in lines_by_date.items() if len(lines) > 1}

        # Save duplicate lines to the output file
        with open(output_file_path, 'w') as output_file:
            if duplicate_lines_by_date:
                output_file.write("Duplicate lines found:\n")
                for date, lines in duplicate_lines_by_date.items():
                    output_file.write("Date: " + date + "\n")
                    output_file.write("Duplicate Lines:\n")
                    for line in lines:
                        output_file.write(line + "\n")
                    output_file.write("\n")
            else:
                output_file.write("No duplicate lines found.\n")
