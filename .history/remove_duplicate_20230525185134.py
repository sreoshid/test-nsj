import os
import glob

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

        # Keep track of log bodies that have already been written
        written_bodies = set()

        # Read through the original log file and copy unique log bodies to the duplicate
        with open(log_path, 'r') as log_file:
            for line in log_file:
                if '|' in line:
                    # Log line separated by |
                    parts = line.split('|')
                    log_body = '|'.join(parts[3:])
                else:
                    # Log line separated by spaces
                    parts = line.split()
                    print(parts)
                    start_index = line.find(parts[])
                    log_body = line[start_index:].strip()

                if log_body not in written_bodies:
                    with open(dup_path, 'a') as dup_file:
                        dup_file.write(line)
                    written_bodies.add(log_body)