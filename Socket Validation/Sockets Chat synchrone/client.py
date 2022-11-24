import socket

host = "127.0.0.1"
port = 10000
msg = ""

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
            while msg!="exit" and msg!= "bye":
                msg = input(f'\n{usname} > ')
                socket_client.send(msg.encode())
                data = socket_client.recv(1024).decode()
                print(f"\n{usnameserver} > {data}")
            socket_client.close()
        except KeyboardInterrupt:
            bye = "bye"
            socket_client.send(bye.encode())