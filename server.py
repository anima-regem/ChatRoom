import socket
import threading

IP_ADDRESS = '127.0.0.1'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP_ADDRESS, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client : socket):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames.pop(index)
            broadcast(f"{nickname} just left the server!".encode('ascii'))
            print(f"{client} disconnected!")
            client.close()
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected to {address}")

        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"{address} now has the nickname {nickname}")
        broadcast(f"{nickname} just hopped onto the server!".encode('ascii'))
        client.send(f"Connected to server!".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__=='__main__':
    receive()
