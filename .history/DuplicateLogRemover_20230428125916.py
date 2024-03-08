import fileinput
lines_seen = set()

for line in fileinput.input(files=["C:\\Users\\srdasg\\OneDrive - SAS\\Desktop\\KnowledgeSharing\ps"], inplace=True):
    log_info = line.split("|", 3)[3].strip()
    if log_info not in lines_seen:
        lines_seen.add(log_info)
        print(line.rstrip())