import socket

host = "127.0.0.1"
port = 10000
data = ""
usnameserver = "Serveur"

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((host, port))
socket_server.listen(1)

while True:
    conn, address = socket_server.accept()
    usname = conn.recv(1024).decode()
    while data!="exit" and data!="bye":
        try:
            hello = ""
            socket_server.send(hello.encode())
        except (ConnectionResetError, ConnectionAbortedError):
            print("Le client a fermé abruptement la connexion.")
        else:
            print("OK")


