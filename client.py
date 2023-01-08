import socket
import threading
from rich import print

IP_ADDRESS = '127.0.0.1'
PORT = 55555

server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP_ADDRESS,PORT))
print("\n[bold magenta]Enter a nickname :vampire: : [/bold magenta]",end=" ")
nickname = input()


def receive():
    while True:
        try:
            message = server.recv(1024).decode('ascii')
            if message == 'NICK':
                server.send(nickname.encode('ascii'))
            else:
                print("[bold blue]\n"+message+"[/bold blue]\n")
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