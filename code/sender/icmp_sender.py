#Here we manually add the path of the scapy library to the python path.
import sys
sys.path.append("/usr/local/lib/python3.10/dist-packages")

from scapy.all import *

packet = Ether()/IP(dst="receiver", src="sender", ttl=1)/ICMP()
sendp(packet)
