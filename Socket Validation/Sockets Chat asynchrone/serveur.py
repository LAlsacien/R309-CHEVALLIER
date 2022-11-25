import socket
import threading

host = "127.0.0.1"
port = 10000
usnameserver = "Serveur"
data = ""
msg = ""

def envoi():
    while True:
        msg = input(f'\n{usnameserver} > ')
        conn.send(msg.encode())
        if msg == "bye" or msg == "exit":
            break
            b = "Le serveur a fermé la connexion."
            conn.send(b.encode())
            conn.close()

def recu():
    while True:
        data = conn.recv(1024).decode()
        print(f"\n{usname} > {data}")
        if msg == "bye" or msg == "exit":
            break
            conn.close()

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((host, port))
socket_server.listen(1)

while True:
    conn, address = socket_server.accept()
    usname = conn.recv(1024).decode()
    conn.send(usnameserver.encode())
    
    thread_envoi = threading.Thread(target = envoi)
    thread_envoi.start()

    thread_recu = threading.Thread(target = recu)
    thread_recu.start()

    rep = input("Continuer ? (y/n)")
    if rep == "n":
        break
socket_server.close()


