import fileinput
import glob
import os

# Get a list of all files in the directory
files = glob.glob("C:\\Users\\srdasg\\OneDrive - SAS\\Desktop\\KnowledgeSharing\\ps\\*")

for file in files:
    file_name = os.path.splitext(os.path.basename(file))[0]
    output_file_name = f"{file_name}Duplicate.txt"
    
    lines_seen = set()
    duplicate_lines = set()
    duplicate_log_info = []
    
    for line in fileinput.input(files=file, inplace=False):
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
                duplicate_log_info.append(log_info)
        else:
            lines_seen.add(log_info)
    
    with open(output_file_name, "w") as f:
        for log_info in duplicate_log_info:
            f.write(log_info + "\n")
