loop = True
clientusr = ['client1','client2']
clientpass = ['1234']
globalcalluser = "client"

def client():
     import socket

     handlerSocket = socket.socket()
     serverIP = "0.0.0.0"
     serverPort = 2222

     handlerSocket.connect((serverIP,serverPort))
     print 'connecting to server'

     while True:
           message = handlerSocket.recv(1024)
           print 'pesan dari server : ',message
           message = raw_input("masukkan pesan anda : ")
           handlerSocket.send(message)
           pass

while(loop):
           print 'login client'.upper()
           inputA = raw_input("Username = ")
           inputB = raw_input("Password = ")
 
           if ((inputA in clientusr) and (inputB in clientpass)):
                   globalcalluser = inputA
                   client()
           else:
                   print 'maaf username atau password yang anda masukan salah'
                   loop
