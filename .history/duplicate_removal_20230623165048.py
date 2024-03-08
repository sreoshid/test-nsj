from collections import defaultdict

log_file_path = r"C:\Users\srdasg\OneDrive - SAS\Desktop\KnowledgeSharing\psDuplicate\wrapper.txt"
output_file_path = r"C:\Users\srdasg\OneDrive - SAS\Desktop\KnowledgeSharing\psDuplicate\duplicate_entries.txt"
logs_by_date = defaultdict(list)

def process_log_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            # Split log file into individual lines
            lines = input_file.read().strip().split('\n')

            # Process each log entry
            for line in lines:
                # Extract the date from the log entry
                date = line.split('|')[2].strip().split()[0]
                # Append the log entry to the corresponding date list
                logs_by_date[date].append(line)

        with open(output_file_path, 'w') as output_file:
            # Print only one instance of duplicate entries to the output file
            for date, entries in logs_by_date.items():
                if len(entries) > 1:
                    output_file.write(f"Duplicate entries for date {date}:\n")
                    output_file.write(entries[0] + '\n')  # Write the first instance
                    output_file.write('\n')

        print(f"Duplicate entries have been written to {output_file_path}")

    except FileNotFoundError:
        print("Log file not found.")

process_log_file(log_file_path, output_file_path)
