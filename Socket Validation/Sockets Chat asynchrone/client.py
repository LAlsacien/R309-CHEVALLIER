import socket
import threading

host = "127.0.0.1"
port = 10000
msg = ""

def envoi():
    while True:
        msg = input(f'\n{usname} > ')
        socket_client.send(msg.encode())
        if msg == "bye" or msg == "exit":
            break
            socket_client.close()


def recu():
    while True:
        data = socket_client.recv(1024).decode()
        print(f"\n{usnameserver} > {data}")
        if msg == "bye" or msg == "exit":
            break
            socket_client.close()


if __name__ == "__main__" :
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_client.connect((host, port))
    except ConnectionRefusedError:
        print("Connexion au serveur refusée.")
    else:
        try:
            print("Vous êtes connecté au serveur !")
            usname = input('Veuillez entrer votre pseudo : ')
            socket_client.send(usname.encode())
            usnameserver = socket_client.recv(1024).decode()
            
            thread_envoi = threading.Thread(target = envoi)
            thread_envoi.start()

            thread_recu = threading.Thread(target = recu)
            thread_recu.start()

        except KeyboardInterrupt:
            bye = "bye"
            socket_client.send(bye.encode())


