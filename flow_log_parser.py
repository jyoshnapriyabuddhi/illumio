import csv
from collections import defaultdict

def load_lookup_table(file_path):
    lookup_table = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        # print("Headers found:", reader.fieldnames)  # Debug print
        for row in reader:
            # print("Row data:", row)  # Debug print
            key = (row['dstport'].strip(), row['protocol'].strip().lower())
            tag = row['tag'].strip()
            lookup_table[key] = tag
    return lookup_table

def parse_flow_logs(file_path, lookup_table):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    
    # Map protocol numbers to string names
    protocol_map = {
        '6': 'tcp',
        '17': 'udp',
        '1': 'icmp'
    }
    
    with open(file_path, mode='r') as file:
        for line in file:
            parts = line.split()
            if len(parts) < 12:  # Ensure there are enough parts
                continue
            
            dstport = parts[5]  # Destination Port
            protocol_number = parts[7]  # Protocol as number
            protocol = protocol_map.get(protocol_number, 'unknown')  # Convert to string
            
            key = (dstport, protocol)
            tag = lookup_table.get(key, "Untagged")
            
            tag_counts[tag] += 1
            port_protocol_counts[key] += 1
            
    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_file):
    with open(output_file, mode='w') as file:
        # Write Tag Counts
        # file.write("Tag Counts:\n")
        file.write("Tag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")
        
        # Write Port/Protocol Combination Counts
        file.write("\nPort/Protocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")

def main(flow_log_file, lookup_file, output_file):
    lookup_table = load_lookup_table(lookup_file)
    tag_counts, port_protocol_counts = parse_flow_logs(flow_log_file, lookup_table)
    write_output(tag_counts, port_protocol_counts, output_file)

if __name__ == "__main__":
    flow_log_file = 'flow_logs.txt'  
    lookup_file = 'lookup_table.csv' 
    output_file = 'output_counts.csv' 
    main(flow_log_file, lookup_file, output_file)
