import socket
import threading

IP_ADDRESS = '127.0.0.1'
PORT = 55555

server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP_ADDRESS,PORT))
nickname = input("Enter your nickname : ")


def receive():
    while True:
        try:
            message = server.recv(1024).decode('ascii')
            if message == 'NICK':
                server.send(nickname.encode('ascii'))
            else:
                print("\n"+message+"\n")
        except:
            print("Aww Damn, an error!")
            server.close()
            break

def write():
    while True:
        message = f"{nickname} : {input()}"
        server.send(message.encode('ascii'))

receiving = threading.Thread(target=receive)
writing = threading.Thread(target=write)
receiving.start()
writing.start()