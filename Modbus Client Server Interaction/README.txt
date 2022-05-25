Installing ModRSSim simulator as a master PLC and using Modbus interface doing interaction as a client.

Description :
This was given as an assignment to understand  and get a practical overview about how the architecture
and interaction  between Modbus Master  with the slave  occurs.

Requisites:
To install the simulator it is required to have windows 10 or windows 7.  Have to create two virtual
machine  , one to install the simulator , other  to write a python client using pymodbus library to 
remotely access as a client to the master PLC. 

Installation:
  1. To install pymodbus run  on ubuntu machine  run:
        sudo apt-get install python-pymodbus
     To install it on windows machine run:
        pip install  -U pymodbus
  2. To  Download the MOdRSSIM simulator visit
        (https://sourceforge.net/projects/modrssim/files/)
To access the remote server, the IP address of the simulator server machine will be needed.Collect that.

Usage: To run the  python script  client.py pass the  suitable IP address and port number of the simulator Host.
      ./client.py 10.0.2.15  502
Once you are connected  , you are going to get a display containing all the list of task of the assigned work.
Choose the corresponding inputs and get the result.But before opting for choice 7, just make sure to disable
write options for coil and holding register in the simulator.


                      

                       


