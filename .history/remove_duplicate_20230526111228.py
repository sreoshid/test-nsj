import os

log_dir = r'C:\Users\srdasg\OneDrive - SAS\Desktop\KnowledgeSharing\ps_wrapper'
dup_dir = r'C:\Users\srdasg\OneDrive - SAS\Desktop\KnowledgeSharing\psDuplicate'

# Create the duplicate directory if it doesn't exist
if not os.path.exists(dup_dir):
    os.makedirs(dup_dir)

# Loop through each file in the log directory
for filename in os.listdir(log_dir):
    if filename.endswith('.log'):  # Only process log files
        log_path = os.path.join(log_dir, filename)
        dup_path = os.path.join(dup_dir, filename)

        # Create or truncate the duplicate log file
        with open(dup_path, 'w') as dup_file:
            pass

        # Dictionary to store log lines grouped by date
        log_lines_by_date = {}

        # Read through the original log file and group log lines by date
        with open(log_path, 'r') as log_file:
            for line in log_file:
                date_time = line.split(' ', 3)[2].strip()  # Extract the date and time from the line

                # Extract the date part from the date_time string
                date = date_time.split()[0]

                # Add the log line to the corresponding date entry in the dictionary
                log_lines_by_date.setdefault(date, []).append(line)

        # Write the first instance of each duplicate entry for each date to the duplicate log file
        with open(dup_path, 'a') as dup_file:
            for date, log_lines in log_lines_by_date.items():
                duplicates = set()
                for line in log_lines:
                    if line in duplicates:
                        continue
                    dup_file.write(line)
                    duplicates.add(line)
