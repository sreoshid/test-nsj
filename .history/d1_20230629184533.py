import os
import re
from collections import Counter

log_directory = r'C:\Users\srdasg\OneDrive - SAS\Desktop\KnowledgeSharing\ps_wrapper'  # Path to the log directory
output_directory = r'C:\Users\srdasg\OneDrive - SAS\Desktop\KnowledgeSharing\psDuplicate'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Regular expression pattern to extract the date and line
# pattern = r"(\d{4}/\d{2}/\d{2})\s+(\d{2}:\d{2}:\d{2})\s+\|\s+(.*)"
pattern_error = r"pattern = r"(\d{4}/\d{2}/\d{2})\s+(\d{2}:\d{2}:\d{2})\s+\|\s+(?!.*\d{2}:\d{2}:\d{2},\d{3}\s+.*)"
)"

# Iterate over log files in the directory
for file_name in os.listdir(log_directory):
    if file_name.endswith('.log'):  # Consider only log files
        file_path = os.path.join(log_directory, file_name)
        output_file_name = f"{os.path.splitext(file_name)[0]}_duplicate.log"
        output_file_path = os.path.join(output_directory, output_file_name)

        # Extract dates and lines from the log file
        with open(file_path, 'r') as log_file:
            log_content = log_file.read()
            matches = re.findall(pattern + "|" + pattern_error, log_content)
            print(matches)


        # Create a list of lines with date and time
        lines_with_datetime = []
        for match in matches:
            date, time, line = match
            datetime = date + ' ' + time
            lines_with_datetime.append((datetime, line))

        # Count occurrences of duplicate lines
        line_counter = Counter(lines_with_datetime)

        # Save duplicate lines to the output file
        with open(output_file_path, 'w') as output_file:
            if line_counter:
                output_file.write("Duplicate lines found:\n")
                for line, count in line_counter.items():
                    if count > 1:
                        datetime, line_text = line
                        output_file.write("Line: " + line_text + ", Count: " + str(count) + "\n")
                output_file.write("\n")
            else:
                output_file.write("No duplicate lines found.\n")
