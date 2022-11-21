import socket

host = "127.0.0.1"
port = 10000

if __name__ == "__main__" :
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_client.connect((host, port))
    except ConnectionRefusedError:
        print("Connexion au serveur refusée.")
    else:
        print("Vous êtes connecté au serveur !")
        usname = input('Veuillez entrer votre pseudo : ')
        socket_client.send(usname.encode())
        while True:
            msg = input(f'\n{usname} > ')
            socket_client.send(msg.encode())


