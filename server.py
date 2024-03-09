# real-time chat application
import socket
import threading

host = socket.gethostname()
port = 5002

server = socket.socket()

server.bind((host, port)) #binding our socket to the port
server.listen(2)#listening for 2 clients

conn_1, addr_1 = server.accept()
conn_2, addr_2 = server.accept()


def send(from_conn, to_conn):
    while True:
        data = from_conn.recv(513).decode()
        info = to_conn.send(data.encode())
    
thread_1 = threading.Thread(target= send, args= (conn_1, conn_2))
thread_2 = threading.Thread(target= send, args= (conn_2, conn_1))
    
thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

conn_1.close()
conn_2.close() 


