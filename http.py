import socket
import threading

ip = '127.0.0.1'
port = 3000
answer = """
HTTP/1.1 200 Ok
Content-Type: text/html
Content-Length: {size}
{body}"""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
server.listen(10)
print('IP -> : {}:{}'.format(ip, port))

def client(client_socket):
    request = client_socket.recv(4096).decode()
    client_socket.send(answer.format(size = len(request), body = request).encode())
    client_socket.close()

while True:
    client_sock, address = server.accept()
    print('received connection from: {}:{}'.format(address[0], address[1]))
    handler = threading.Thread(
        target = client,
        args = (client_sock,))
    handler.start()