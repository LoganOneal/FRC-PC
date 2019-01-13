import socket
import pickle

HOST = 'roborio-3966-frc.local'

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 5800))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = 'null'
    while True:
        data = conn.recv(4096)
        if not data: break
        print(pickle.loads(data))
    conn.close()
    print('client disconnected')