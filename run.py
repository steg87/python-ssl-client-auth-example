import client, server
from os import path
from time import sleep

server_host = "127.0.0.1"
server_port = 35689
server_sni_hostname = "www.company-b.com"
client_cert = path.join(path.dirname(__file__), "client.crt")
client_key = path.join(path.dirname(__file__), "client.key")
server_cert = path.join(path.dirname(__file__), "server.crt")
server_key = path.join(path.dirname(__file__), "server.key")

s = server.SSLServer(server_host, server_port, server_cert, server_key, client_cert)
s_thread = server.SSLServerThread(s)
s_thread.start()
sleep(2)
c = client.SSLClient(
    server_host, server_port, server_sni_hostname, client_cert, client_key
)
c.connect()

c.send("This is a test message!")

c.close()
