import socket
class tcp_sever:

    s = socket.socket()
    s.bind(('127.0.0.1',8090))
    s.listen(1)
    conn, addr = s.accept()
    #nhan request tu Client
    data = conn.recv(1024)
    print(data.decode('utf-8'))


    conn.send(str.encode('utf-8'))
    conn.close()