# Flow Log Parser

## Overview
This Python program parses AWS flow log data and maps each entry to a tag based on a lookup table defined in a CSV file. It counts the occurrences of each tag and each port/protocol combination, generating a summary output.

## Requirements
- Python 3.x
- No external libraries required (uses only built-in libraries)

## Files
- `flow_logs.txt`: Contains the sample flow log data.
- `lookup_table.csv`: Contains the mapping of dstport and protocol to tags.
- `flow_log_parser.py`: The main script for parsing the logs.
- `output_counts.csv`: The output file containing the counts.
- `flow_log_parser_rev2.py`: The revised version of main script which has capability to create `lookup_table_rev2.csv` that have upto 10000 mappings and `flow_logs_rev2.txt` of 10MB. This script is used for testing the program on  large input data

## Assumptions
- The program only supports the default log format (version 2).
- Input files are plain text (ASCII) and formatted as specified.
- Matches for dstport and protocol are case insensitive.
- The flow log file can be up to 10 MB, and the lookup file can have up to 10,000 mappings.

## How to Run
1. Ensure Python 3.x is installed on your machine.
2. Place `flow_logs.txt` and `lookup_table.csv` in the same directory as `flow_log_parser.py`.
3. Open a terminal and navigate to the directory.
4. Run the script using the following command: 
    - `python flow_log_parser.py`
5. The output will be written to `output_counts.csv`.

## Testing
The script has been tested with sample data provided in `flow_logs.txt` and `lookup_table.csv`. The output format has been verified against expected counts.
The revision2 script (flow_log_parser_v2.py) has been used to generate large data and test on large data.