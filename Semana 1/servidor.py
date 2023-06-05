import socket

HOST = "127.0.0.1"
PORT = 9000
print("INICIANDO O SOCKET")
s = socket.socket()
s.bind((HOST, PORT))
print("ESCUTANDO")
s.listen()
conexao, endereco = s.accept()
with conexao:
    print(f"Nova conexão {endereco}")
    while True:
        dados = conexao.recv(1024)
        if not dados:
            break
        texto = dados.decode('utf-8')
        numero1, numero2 = texto.split("x")
        numero1 = int(numero1)
        numero2 = int(numero2)
        resultado = numero1 * numero2
        resultado = str(resultado)
        conexao.sendall(resultado.encode("utf-8"))
s.close()