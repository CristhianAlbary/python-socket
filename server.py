import socket
# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Escutar a porta 9000
server = sock.bind(('localhost', 8000))
# Definir o limite de 1 conexao paralela
sock.listen(1)

def sendMessage(msg):
    connection.sendall(msg.encode())

while True:
    # Aguardar uma conexao
    print("Aguardando conexao")
    connection, address_client = sock.accept()    
    
    received_data = ''
    while True:
        received_data = connection.recv(1024).decode()
        if(received_data != "see ya"):
            print("Cliente diz:")
            print(received_data)
            print("Digite uma mensagem:")
            msg = input()
            sendMessage(msg)
        else:
            msg = 'see ya'
            sendMessage(msg)
            break
    print(received_data)
    connection.close()