import socket
import time
# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectar ao servidor com ip e porta
sock.connect(('localhost', 8000))

def getMessage():
    print("Digite uma mensagem")
    msg = input()
    return msg

def sendMessage(msg):
    sock.sendall(msg.encode())

received_data = ''
while received_data != "see ya":
    received_data = ''
    msg = getMessage()
    sendMessage(msg)
    received_data = sock.recv(1024).decode()
    print("Server diz:")
    print(received_data)
print("Terminou")
sock.close()