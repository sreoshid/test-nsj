import fileinput
import glob

# Get a list of all files in the directory
files = glob.glob("C:\\Users\\srdasg\\OneDrive - SAS\\Desktop\\KnowledgeSharing\\ps\\*")

lines_seen = set()

for line in fileinput.input(files=files, inplace=True):
    log_info = line.split("|", 3)[3].strip()
    if log_info not in lines_seen:
        lines_seen.add(log_info)
        print(line.rstrip())
