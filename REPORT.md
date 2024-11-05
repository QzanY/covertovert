Ozan Yanık - 2581163 \
Fatih Emre Güneş - 2580603 \
Group ID: 28 \ 
GitHub link: https://github.com/QzanY/covertovert 

# Description:
This documentation is created for CENG435 Programming Assignment 1. \
The project is a simple implementation of an ICMP environment. \
The project is written in Python. To be able to send and receive ICMP packets, the project uses the **scapy** library. \
There are 2 main parts of the project: The sender and the receiver. 
## Sender:
The sender sends ICMP packets to the receiver. It uses the **Ether**,**IP** and **ICMP** functions of the **scapy** library.\
The TTL value of the packets is 1.
The packets are sent by the send function of the **scapy** library. \
The sender sends 1 packet to the receiver. 
## Receiver:
The receiver receives the ICMP packets from the sender. \
It uses the **sniff** function of the **scapy** library to receive the packets. \
In the **sniff** function, the **filter** argument is set to capture only ICMP Response packets. Also, In the **check_and_show** function, the packet is checked for having its TTL value as 1. If the TTL value of the packet is 1, the packet is printed with **show** function of the **scapy** library. Otherwise, nothing is shown.
# Additional Note:
In some setups, the **$PATH** environment variable does not include the directory of Python packages. This was the case for us too. In order to guarantee that the **$PATH** varible meets our needs, we manually add the directory of Python packages to the **$PATH** by the **path.append** function of the **sys** library in the codes of both receiver and sender.