import fileinput
import glob
import os

# Define the directory where the log files are stored
log_directory = "C:\\Users\\srdasg\\OneDrive - SAS\\Desktop\\KnowledgeSharing\\ps"

# Define the directory where the new duplicate log files will be stored
duplicate_log_directory = "C:\\Users\\srdasg\\OneDrive - SAS\\Desktop\\KnowledgeSharing\\psDuplicate"

# Get a list of all log files in the directory
log_files = glob.glob(os.path.join(log_directory, "*"))

for log_file in log_files:
    # Get the base filename without the path or extension
    base_filename = os.path.splitext(os.path.basename(log_file))[0]

    # Define the name of the new duplicate log file
    duplicate_log_file = os.path.join(duplicate_log_directory, base_filename + "Duplicate.log")

    # Create a set to track the unique log entries
    lines_seen = set()

    # Open the log file for reading and the duplicate log file for writing
    with open(log_file, "r") as f_read, open(duplicate_log_file, "w") as f_write:
        for line in f_read:
            if "|" in line:
                # Split the line based on pipes if present
                log_info = line.split("|", 3)[3].strip()
            elif " " in line:
                words = line.split()
                msg = ""
                for i in range(1, len(words)):
                    msg += " " + words[i]
                log_info = msg

            if log_info in lines_seen:
                # Write the duplicate line to the duplicate log file
                f_write.write(line.rstrip() + "\n")
            else:
                lines_seen.add(log_info)
