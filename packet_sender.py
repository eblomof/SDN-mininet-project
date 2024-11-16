
from scapy.all import *

def send_packets():
    print("Sending ICMP packets from h1 to h2...")
    packet = IP(src="10.0.0.1", dst="10.0.0.2") / ICMP()
    send(packet, count=10)
    
    print("Sending ICMP packets from h2 to h3...")
    packet = IP(src="10.0.0.2", dst="10.0.0.3") / ICMP()
    send(packet, count=10)

if __name__ == "__main__":
    send_packets()
