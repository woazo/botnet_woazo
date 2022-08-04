# Botnet_Woazo
A botnet - Can do a DDoS attack (and know how to cook an egg)

/!\ THIS IS FOR EDUCATIONAL PURPOSE ONLY /!\ 

The botnet work with a python server, with the socket module. It work with only 2 programs, the server and the client. The client is fully undetectable. You can change "host" variable to put your local ip address in the client script (or just leave it like it is, i think it should work too). When you have start the botnet_server.py, your victim must start the botnet_client.py, and then, you got a reverse shell. You can have several victims, you only need to hit the "refresh" command and wait for other bots to connect. You can get a reverse shell over the internet by using port-forwarding. In this case, you must change the port of connection in both scripts. If you have any issues, report it.

Here is the list of things you can do :

- Help : Display a help screen
- Cmd  : Send command to all your bots
- Refresh : When there are new vitcims, hit refresh to accept the connection
- Flood : Execute a DDoS attack against a victim. Once you hit that command and hit enter, you must specify the target ip, the target port and the number of packets you want to send (2500 packets = 10sec), all separated by ":". For example : 1.1.1.1:80:2500. And bam! All your bots will send packets to the victim. More you have bots, more powerful it is.
- How to cook an egg : Teach you how to cook an egg
- Close : Close all connections with your bots.

Feel free to change the script as you want and add more feature.

**Persistent and BTC miner coming soon**

You can also use pyinstaller to make an executable of the client so the victim won't need to download python and dependencies.You can also change the port if you want but you will need to change the port also in the server script.


List of dependencies you will need :

- pip install sockets
- pip install scapy
- pip install threading
- pip install time
- pip install os


And once again, if you have any issues report it.
