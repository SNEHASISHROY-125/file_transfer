'''
Server: accepts clients
        adds to log-file

'''

import socket, threading, os, build_path as build ,yaml ,json

def get_wifi_ip_address() -> str:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def server_init() ->socket.socket:
    try:
        s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global port
        port = 25200
        s_socket.bind((get_wifi_ip_address(),port))
        s_socket.listen(5)

    except: ...
    finally: return s_socket

def isclose() -> bool:
    _ = str(input('want to close?:  '))
    if _ == 'y': return True

def accept_client():
    print('server listening at:',get_wifi_ip_address(),':',port)
    client , addr = server.accept()
    metadata  =  json.loads(client.recv(1024).decode('utf-8'))
    print('meta:',metadata)
    clients[metadata['name']] = client
    # clients.append(client)
    with open('config.yaml', 'r') as DBR:
        data = yaml.safe_load(DBR)
        with open('config.yaml','w') as DBW:
            data['clients'] [metadata['name']] = addr
            yaml.safe_dump(data,DBW)
    [_.close() for _ in (DBW,DBR)]

def respond_client(): ...

print(type(server:=server_init()))
clients = {}

while True:
    # look for server closure insstructions
    if isclose() : break
    # accept clients
    accept_client()
    #



server.close()
