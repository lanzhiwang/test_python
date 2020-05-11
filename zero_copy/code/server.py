import socket
import hashlib
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    print('Waiting for a connection')
    connection, client_address = sock.accept()
    size = 0
    cnt = None
    try:
        i = 0
        while True:
            data = connection.recv(65536)
            # print('Received data: "%s"' % data)  # 不要打印数据，对性能有很大影响
            i += 1
            if data:
                size += len(data)
                # cnt += data
                print('size: %s' % size)
            else:
                print('Done!')
                break
        print('i:', i)
        print('Total size: ', size)
        #print('Hash of received data :', hashlib.md5(cnt).hexdigest())
    finally:
        connection.close()
