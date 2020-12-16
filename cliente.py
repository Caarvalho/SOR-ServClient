import conversor
import socket



HOST = 'localhost'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    
    z = str(conversor.menu())
    
    s.send(z.encode('utf-8'))
    
    x = str(conversor.menuUm())
    
    s.send(x.encode('utf-8'))
    
    if x == '1':
        y = str(conversor.menuDois())
        s.send(y.encode('utf-8'))
        data = s.recv(1024)
        res = data.decode('utf-8')
        print(res)
    
    elif x == '2':
        y = str(conversor.menuTres())
        s.send(y.encode('utf-8'))
        data = s.recv(1024)
        res = data.decode('utf-8')
        print(res)
        
    elif x == '3':
        res = s.recv(1024).decode('utf-8')
        print(res)
    
    try:
        final = input('Você quer continuar? [S/N]')
    except:
        print('Você sabe ler?')
    else:
        if final in 'Ss':
            continue
        else:
            exit()