Introducing cryptography  with the help of proxy-server to the  Modbus communication protocol  to have communication security in the interaction 
between modbus device and the client.

Description :
This was given as an assignment to get a practical overview about how to implement encrypted interaction between Modbus Master with the client.

Requisites:
To install the simulator, it is required to have windows 10 or windows 7. You can create two virtual
machine, one to install the simulator, and the other one to write a python client using umodbus library to 
remotely access as a client to the master PLC or you can do the both in a same machine.

Installation:
  1. To install umodbus run :
        pip install umodbus
  2. To install modbus proxy server run :
        pip install modbus-proxy
  3. To Download the MOdRSSIM simulator visit
        (https://sourceforge.net/projects/modrssim/files/)
  4. To implement cryptography in the codes, make sure to install the python cryptogtaphy library by running:
        pip install cryptography.
  5. To work with the asymmetric cryptographic protocol RSA run:
        pip install rsa
To access the remote server, the IP address of the simulator server machine will be needed. Collect that.
After installation, A proxy configuration file needs to be written in YAML format (same as the attached file name: modbus-config.yml) by mentioning the ip address
and port numbers of the server and proxy server, and then run :
modbus-proxy -c ./modbus-config.yml

As asked in the homework, I have changed the modbus-proxy.py, tcp.py (client), utils.py files. The files are attached. Please make sure to replace them with
the corresponding files. (As I used anaconda, the exact files were in Anaconda3\Lib\site-packages\umodbus)

Usage: Now to run the  python script  modbus_client.py, pass the suitable IP address and port number of the simulator Host as such:
       python modbus_client.py -a 10.0.2.6:9000

Once you are connected, you are going to get a display containing the list of all the tasks of the assigned work.
Once the corresponding task is chosen, you will be seeing the required encryption mechanism for each one of the function calls.


                      

                       


