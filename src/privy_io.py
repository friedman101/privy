import socket

def send(s, msg):
    try:
        s.send(msg.encode())
    except:
        return

def receive(s):
    try:
        data = s.recv(1024)
    except:
        return
    if not data:
        return

    return data.decode()

def setup_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s

def config_client_socket(s, ip, TCP_PORT):
    s.connect((ip, TCP_PORT))

def config_server_socket(s, TCP_PORT):
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', TCP_PORT))
    s.listen(1)
    s, ip = s.accept()
    return s