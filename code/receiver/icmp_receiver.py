#Here we manually add the path of the scapy library to the python path since the program could not find the scapy library otherwise.
import sys
sys.path.append("/usr/local/lib/python3.10/dist-packages")

from scapy.all import sniff

#Here we sniff the packets that are ICMP echo requests

def check_and_show(x):
    if x.ttl ==1:
        x.show()
 
sniff(filter="icmp  and icmp[icmptype] == icmp-echo", prn=check_and_show)
