#!/usr/bin/env python
# coding: utf-8

# In[7]:


from pymodbus.client.sync import ModbusTcpClient
import sys
client=ModbusTcpClient("10.0.2.15",port=502)
client = ModbusTcpClient(sys.argv[1], port=sys.argv[2]) 
client.connect()
def printResponse( response):
    print("Response received is:")
    attrList=['address','value','bits' , 'function_code', 'protocol_id','register' ]
    for attr in attrList:
    	try: print( attr, getattr(response, attr))
    	except: continue
print("Select the Question Number ")
print("1. Write values in Holding Registers")
print("2. Write values in coils")
print("3. Read values from Holding Registers")
print("4. Read values from coils")
print("5. Display function codes of reading and writing from the coils")
print("6. Display function code whenever its an error ")
print("7. Disabling  the write option for the coils in the simulator and then proceeding")
print("8. exit")
print("="*50)

choice=int(input())
if choice==1:
    rr=client.write_registers(142,[10,20,30,40,60])
    printResponse(rr)
elif choice==2:
    client.write_coil(115,True)
    result=client.read_coils(115,1)
    print(result.bits[0])
    client.write_coil(16,True)
    result=client.read_coils(16,1)
    print(result.bits[0])
    client.write_coil(34,True)
    result=client.read_coils(34,1)
    print(result.bits[0])
    client.write_coil(18,True)
    result=client.read_coils(18,1)
    print(result.bits[0])
    client.write_coil(25,True)
    result=client.read_coils(25,1)
    print(result.bits[0])
    client.write_coil(9,True)
    result=client.read_coils(9,1)
    print(result.bits[0])
elif choice==3:
    rr=client.read_holding_registers(140,10)
    printResponse(rr)
elif choice==4:
    rr=client.read_coils(30,15)
    printResponse(rr)
elif choice==5:
    rr=client.read_coils(30,15)
    print(rr.function_code)
    rr=client.write_coil(115,True)
    print(rr.function_code)
elif choice==6:
    rr=client.write_registers(30000,a)
    print(rr.function_code)
elif choice==7:
    rr=client.write_registers(142,[10,20,30,40,60])
    printResponse(rr)
else:
    print("wrong chice!")






# In[ ]:





# In[ ]:





# In[ ]:




