from collections import defaultdict

log_file = '''
<log entries>
'''

logs_by_date = defaultdict(list)

# Split log file into individual lines
lines = log_file.strip().split('\n')

# Process each log entry
for line in lines:
    # Extract the date from the log entry
    date = line.split('|')[2].strip().split()[0]
    # Append the log entry to the corresponding date list
    logs_by_date[date].append(line)

# Print only one instance of duplicate entries
for date, entries in logs_by_date.items():
    if len(entries) > 1:
        print(f"Duplicate entries for date {date}:")
        print(entries[0])  # Print the first instance
        print()
