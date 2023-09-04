'''
client: 01.sends local-file structure
	02.reccives files
'''

import socket, json

def get_wifi_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# print("IP Address of the connected Wi-Fi network:", get_wifi_ip_address())


# Set the server IP address and port
server_ip = '192.168.1.4'  # Replace with the server's IP address
server_port = 25200  # Replace with the server's port number
client_name = 'roy125'

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# send metadata: {JSON}
metadata = {
    "name" : client_name
}
client_socket.send(json.dumps(metadata).encode('utf-8'))

# Send data to the server
# message = "Hello, server!"
# client_socket.send(message.encode())

# # Receive a response from the server
# response = client_socket.recv(1024)
# print(f"Received response: {response.decode()}")

# Close the socket
client_socket.close()