from socket import socket, AF_INET, SOCK_STREAM


target_host = 'google.com'
target_port = 80


# create socket object
client = socket(AF_INET, SOCK_STREAM)
# connect the client
client.connect((target_host, target_port))
# send some data
client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
# receive some data
response = client.recv(4096)

print(response.decode())
client.close()