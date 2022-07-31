# Botnet_Woazo
A botnet who work only in a local network - Can do a DDoS attack

/!\ THIS IS FOR EDUCATIONAL PURPOSE ONLY /!\ 

The botnet work with a python server, with the socket module. It work with only 2 programs, the server and the client. You must change "host" variable to put your local ip address in the client script. When you have start the botnet_server.py, your victim (in your local network) must start the botnet_client.py, and then, you got a reverse shell. You can have several victims, you only need to hit the "refresh" command and wait for other bots to connect. If you have any issues, report it.

Here is the list of things you can do :

- Help : Display a help screen
- Cmd  : Send command to all your bots
- Refresh : When there are new vitcims, hit refresh to accept the connection
- Flood : Execute a DDoS attack against a victim. Once you hit that command and hit enter, you must specify the target ip, the target port and the number of packets you want to send (2500 packets = 10sec), all separated by ":". For example : 1.1.1.1:80:2500. And bam! All your bots will send packets to the victim. More you have bots, more powerful it is.
- Close : Close all connections with your bots.

Be free to change the script as you want and add more feature.

You can also use pyinstaller to make an executable of the client so the victim won't need to download python and dependencies. But before that, make sure you have changed the host to your local ip address so the client will connect to you. You can also change the port if you want but you will need to change the port also in the server script.


List of dependencies you will need :

- pip install sockets
- pip install scapy
- pip install threading
- pip install time
- pip install os


And once again, if you have any issues report it.
