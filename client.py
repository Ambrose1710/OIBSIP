import socket
import threading

host = socket.gethostname()
port = 5002

Client_server = socket.socket()

Client_server.connect((host, port))

def send():
    while True:
        data = input()
        Client_server.send(data.encode())
    
def recieve():
    while True:
        data = Client_server.recv(513).decode()
        print("-> ", data)
        
thread_1 = threading.Thread(target = send)
thread_2 = threading.Thread(target = recieve)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

