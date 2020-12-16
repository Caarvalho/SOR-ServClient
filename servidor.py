import conversor
import socket
import random 
HOST = 'localhost'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print('Aguardando conexão de um cliente.')
conn, ender = s.accept()
print(f'Conectado em {ender}')
while True:
   
    data0 = conn.recv(1024)

    num = float(data0.decode('utf-8'))
    
    data1 = conn.recv(1024)
    
    x = int(data1.decode('utf-8'))
    if x != 3:
        data2 = conn.recv(1024)
        y = int(data2.decode('utf-8'))
    
    if x == 1:
        res = conversor.tempo(num, y)
        conn.send(res.encode('utf-8'))
        
    elif x == 2:
        res = conversor.velocidade(num,y)
        conn.send(res.encode('utf-8'))
    elif x == 3:
        
        print('Conversão aleatória')
        x = random.randint(1,2)
        y = random.randint(1,6)
        print('números sorteados')
        if x == 1:
            res = conversor.tempo(num, y)
            print('enviando valores.')
            conn.send(res.encode('utf-8'))
        elif x == 2:
            res = conversor.velocidade(num, y)
            print('enviando valores.')
            conn.send(res.encode('utf-8'))

        






