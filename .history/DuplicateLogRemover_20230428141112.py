import fileinput
import glob

# Get a list of all files in the directory
files = glob.glob("C:\\Users\\srdasg\\OneDrive - SAS\\Desktop\\KnowledgeSharing\\ps\\*")

lines_seen = set()

for line in fileinput.input(files=files, inplace=True):
    if "|" in line:
        # Split the line based on pipes if present
        log_info = line.split("|", 3)[3].strip()
    elif " " in line:
        log_info = line.split(" ", 3)[3].strip()
        
    log_info not in lines_seen:
        lines_seen.add(log_info)
        print(line.rstrip())
