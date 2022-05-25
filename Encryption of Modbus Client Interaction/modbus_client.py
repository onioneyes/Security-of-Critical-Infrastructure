from argparse import ArgumentParser
from socket import create_connection
import rsa
from umodbus.client import tcp
from cryptography.fernet import Fernet

#Parse the argument of address.
parser = ArgumentParser()
parser.add_argument("-a", "--address")
args = parser.parse_args()
host, port = args.address.rsplit(":", 1)
port = int(port)

values = [1, 2, 3, 4]

#Open a socket to the Modbus proxy server.
sock = create_connection((host, port))
print("Connected to modbus Server at " + str(host) + " : " + str(port))

proxyPubKey = rsa.PublicKey.load_pkcs1(sock.recv(1024))
encKey = Fernet.generate_key()
fernet= Fernet(encKey)
sock.sendall(rsa.encrypt(encKey,proxyPubKey))
print(" Public key  recieved from the proxy-server : " + str(proxyPubKey))
print("Client generated encryption key : " + str(encKey))
print(" Encryption key encrypted with Public Key of  thhe proxy server is :" + str(rsa.encrypt(encKey, proxyPubKey)))


while True:
    print("Enter the Question number")
    print("1. To write value in holding registers")
    print("2. To read value from holding registers")
    print("3. To write boolean in coil")
    print("4. To read boolean from coil")
    print("5. To quit the program")
	
    choice = int(input())
    if choice==1:
        message = tcp.write_multiple_registers(
		    slave_id=1, starting_address=60, values=[10,20,30,40,60]
		)
        response = tcp.send_message(message, sock, fernet)
        assert response == 5
    elif choice==2:
        message = tcp.read_holding_registers(
            slave_id=1, starting_address=60, quantity=6
		)
        response = tcp.send_message(message, sock, fernet)
        assert response == [10,20,30,40,60,0]
        print("==> Values of the respective Holding registers  are :", response)
    
    elif choice==3:
        message = tcp.write_multiple_coils(
			slave_id=1, starting_address=80, values = [True,True,False,True,True,False, True]
		)
        response = tcp.send_message(message, sock, fernet)
        assert response == 7
	
    elif choice== 4: 
        message = tcp.read_coils(
			slave_id=1, starting_address=80, quantity= 7
		)
        response = tcp.send_message(message, sock, fernet)
        assert response ==[True,True, False, True,True,False, True]
        print(" values of the respective coils  are:", response)
    elif choice == 5: 
        print("Exit")
        exit()
    else:
        print(" Please Enter correct choice")
	
sock.close()