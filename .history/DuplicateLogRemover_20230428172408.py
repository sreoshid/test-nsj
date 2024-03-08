import fileinput
import glob

# Get a list of all files in the directory
files = glob.glob("C:\\Users\\srdasg\\OneDrive - SAS\\Desktop\\KnowledgeSharing\\ps\\*")



lines_seen = set()
duplicate_lines = set()

for line in fileinput.input(files=files, inplace=True):
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
        if log_info not in duplicate_lines:
            duplicate_lines.add(log_info)
            print(line.rstrip())
    else:
        lines_seen.add(log_info)

