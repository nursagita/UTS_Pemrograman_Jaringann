loop = True
adminusr = ['server']
adminpass = ['1234']
globalcalluser = "server"

def server():
    import socket

    listenerSocket = socket.socket()
    serverIP = "0.0.0.0"
    serverPort = 2222
    listenerSocket.bind((serverIP,serverPort))
    listenerSocket.listen(0)
    print 'server siap menerima client'
    while True:
          handlerSocket, addr = listenerSocket.accept()
          print 'sebuah client baru terkoneksi dengan alamat = ',addr
          while True:
                message = raw_input("masukan pesan anda : ")
                handlerSocket.send(message)
                message = handlerSocket.recv(1024)
                print 'pesan dari client ; ',message
                 pass
         pass

while(loop):
    print 'login server'.upper()
    input1 = raw_input("Username = ")
    input2 = raw_input("Password = ")
    if ((input1 in adminusr) and (input2 in adminpass)):
                globalcalluser = input1
                server()
    else:
                print 'maaf username atau password yang anda masukan salah'
                loop
