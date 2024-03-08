import fileinput
import glob

# Get a list of all files in the directory
files = glob.glob("C:\\Users\\srdasg\\OneDrive - SAS\\Desktop\\KnowledgeSharing\\ps\\*")

lines_seen = set()

for line in fileinput.input(files=files, inplace=True):
    if "|" in line:
        # Split the line based on pipes if present
        log_info = line.split("|", 3)[3].strip()
    else:
        # Split the line based on spaces if no pipes are present
        log_info = line.split(" ")
        if len(fields) >= 4:
            log_info = fields[3].strip()

    if log_info not in lines_seen:
        lines_seen.add(log_info)
        print(line.rstrip())
