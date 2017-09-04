import socket

class PrivyIO:
    def __init__(self, isServer, port, ip):
        self.s = self.setup_socket()

        if isServer:
            self.s = self.config_server_socket(port)
        else:
            self.config_client_socket(ip, port)

        self.s.setblocking(0)

    def send(self, msg):
        try:
            self.s.send(msg.encode())
        except:
            return

    def receive(self):
        try:
            data = self.s.recv(1024)
        except:
            return
        if not data:
            return

        return data.decode()

    def close_socket(self):
        self.s.close()

    def setup_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return s

    def config_client_socket(self, ip, port):
        self.s.connect((ip, port))

    def config_server_socket(self, port):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(('127.0.0.1', port))
        self.s.listen(1)
        self.s, ip = self.s.accept()
        return self.s