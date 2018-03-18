import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080
f = open("host.txt","w")
f.write(str(HOST))
f.close()
s = socket.socket()
s.bind((HOST, PORT))
s.listen(10)
conn, addr = s.accept()
print 'Connected by', addr
conn.send("hi")

while True:
    print "v"
    data = conn.recv(1024)
    print "yes"
    conn.send(data)
conn.close()
