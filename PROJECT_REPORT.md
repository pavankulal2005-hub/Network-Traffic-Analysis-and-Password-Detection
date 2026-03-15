# Project Report: Network traffic analysis and password detection
### Team Member name :
* **Pavan**
* **Mahesh**
* **Karthik**
* **Manjunath**

### 1. Project Objective :
The main objective of this project is to analyze network traffic and detect sensitive information such as usernames and passwords transmitted through insecure protocols.

### 2. Implementation Details :
The project was implemented using network monitoring tools and Python scripting.
#### Python with Scapy:
Scapy is a powerful Python library used for packet sniffing and manipulation. It is used in this project to capture network packets programmatically and analyze them to detect login credentials or sensitive information.

#### Packet Sniffing:
The system captures packets from the network interface and inspects them for HTTP requests that may contain login data.

#### Wireshark:
Wireshark is used to capture and analyze network packets in real time. It helps visualize network protocols, packet structure, and communication between devices on the network.

#### Credential Detection:
The program scans captured packets to detect common login fields such as:
* (http://testaspnet.vulnweb.com/login.aspx)

* *username*
* *password*
* *login*

#### Protocol Analysis:
The tool also identifies network protocols such as TCP, UDP, and HTTP while displaying the source and destination IP addresses.

### 3 Tools and Technologies Used :

* *Python*
* *Scapy*
* *Wireshark*
* *Nmap*
* *Kali Linux*

### 4 What I Learned :

Through this project, I gained practical knowledge in several cybersecurity areas:

Understanding how network packets travel across a network

Learning how to capture and analyze packets using Wireshark

Using Scapy for packet sniffing and network analysis

Understanding the difference between HTTP and HTTPS communication

Learning how sensitive data can be exposed in unencrypted network traffic

Gaining experience in Python scripting for cybersecurity applications
