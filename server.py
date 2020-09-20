import socket
import ssl
from threading import Thread


class SSLServer:
    def __init__(self, host, port, cafile, chunk_size=1024):
        self.host = host
        self.port = port
        self.chunk_size = chunk_size
        self._context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self._context.verify_mode = ssl.CERT_REQUIRED
        self._context.load_verify_locations(cafile)
        self._ssock = None

    def __del__(self):
        self.close()

    def connect(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
                sock.bind((self.host, self.port))
                sock.listen(5)
                with self._context.wrap_socket(sock, server_side=True) as self._ssock:
                    conn, _ = self._ssock.accept()

                    while True:
                        data = conn.recv(self.chunk_size).decode()
                        if data is None:
                            break
                        else:
                            print(data)
        finally:
            sock.close()
            self.close()

    def close(self):
        self._ssock.close()


class SSLServerThread(Thread):
    def __init__(self, server):
        super().__init__()
        self._server = server
        self.daemon = True

    def run(self):
        self._server.connect()

    def stop(self):
        self._server.close()

