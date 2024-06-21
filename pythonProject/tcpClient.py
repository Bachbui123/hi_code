import socket
class tcp_client:
    s= socket.socket()
    s.connect(('127.0.0.1', 8090))

    a = input("a: ")
    b = input("b: ")
    t = (a,b)

    s.send(str(t).encode('utf-8'))
    data = s.recv(1024)
    print(data.decode('utf-8'))
    s.close()
