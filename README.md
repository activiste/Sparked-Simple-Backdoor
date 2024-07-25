# SPARKED BACKDOOR

## About

SPARKED BACKDOOR is a project designed to help developers and enthusiasts understand how backdoors work in computer networks. This project is composed of a client-server architecture, allowing to simulate a connection between an attacker machine (server) and a victim machine (client).

**Important:** This project is for educational purposes only. Using SPARKED BACKDOOR or any other form of malware for malicious purposes without explicit consent is illegal and unethical. By using or contributing to this project, you agree to do so in a responsible and ethical manner.

## Features

- **Remote connection:** Allows the user (server) to establish a remote connection to a compromised client.
- **Command execution:** After the connection is established, it is possible to execute commands on the compromised client.
- **Simplicity:** Designed to be simple to understand and use, allowing security beginners to find their way around.

### Prerequisites

- Python installed on both client and server machines. | unless build as executable

### Installation steps

1. **Clone the repository:**
```sh
git clone https://github.com/activiste/Sparked-Simple-Backdoor.git
```

2. **Server configuration:**

- Go to the project folder and navigate to the server subfolder.
- Run the server script on your machine.
```sh
python server.py
```

3. **Client Setup:**

- Go to the project folder and navigate to the client subfolder.
- Run the client script from your target machine.
```sh
python client.py
```

## Usage

After running the server on your machine and the client on the target machine, you establish a connection between the two. You can start sending commands from the server to the client to be executed.

## Security and Disclaimer

This project is provided **as is** for educational purposes. It is important to understand that using backdoors without permission is illegal and immoral. We do not encourage or support the use of this tool in malicious activities.

## Contribution

Contributions are welcome! If you want to improve SPARKED BACKDOOR or suggest new features, feel free to create a pull request or open an issue.

## License

This project is licensed under the [MIT](https://opensource.org/licenses/MIT) license. This license allows for great freedom of use and modification, but it provides no warranty.
