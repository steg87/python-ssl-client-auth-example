import client, server
from os import path
from time import sleep

server_host = "localhost"
server_port = 14566
client_cert = path.join(path.dirname(__file__), "client.crt")
client_key = path.join(path.dirname(__file__), "client.key")

s = server.SSLServer(server_host, server_port, client_cert)
s_thread = server.SSLServerThread(s)
s_thread.start()
sleep(2)
c = client.SSLClient(server_host, server_port, client_cert, client_key)
c.connect()

c.send("This is a test message!")

c.close()
s.close()
