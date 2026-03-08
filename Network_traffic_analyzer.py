# Import the sniff function from Scapy to capture network packets
from scapy.all import sniff

# Import IP, TCP, and UDP protocol layers
from scapy.layers.inet import IP, TCP, UDP


# Function to analyze each captured packet
def analyze_packet(packet):

    # Check if the packet contains an IP layer
    if packet.haslayer(IP):

        # Extract Source IP Address
        src_ip = packet[IP].src

        # Extract Destination IP Address
        dst_ip = packet[IP].dst

        # Extract Protocol Number (6 = TCP, 17 = UDP)
        protocol = packet[IP].proto

        # Print packet details
        print("=================================")
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")
        print(f"Protocol       : {protocol}")

        # Check if packet uses TCP protocol
        if packet.haslayer(TCP):
            print("Protocol Type  : TCP")

        # Check if packet uses UDP protocol
        elif packet.haslayer(UDP):
            print("Protocol Type  : UDP")

        # Print the total packet size in bytes
        print("Packet Length  :", len(packet))
        print("=================================")


# Display message when packet capture starts
print("Starting Packet Capture...")

# Start sniffing network packets
# prn = function to process each packet
# store=False = do not store packets in memory (saves RAM)
sniff(prn=analyze_packet, store=True)

#ctrl+c to stop the packet capture