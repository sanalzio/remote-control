import serial
import serial.tools.list_ports
import keyboard
ports=serial.tools.list_ports.comports()
bports=[]
p=None
print('Searching for serial port communication...')
while len(bports)==0:
    for(port,desc,hwid)in sorted(ports):
        if'Bluetooth'in desc:bports.append(port);print(f"Detected {desc}")
for port in bports:
    for dp in bports:
        if int(port[len(port)-1:])>int(dp[len(dp)-1:]):p=int(port[len(port)-1:])
while True:
    try:
        with serial.Serial('COM'+str(p),9600,timeout=1)as ser:
            while True:
                line=ser.readline();con=str(line)[2:len(str(line))-5]
                if len(str(line))!=3:
                    if con=='1':keyboard.send('alt+tab')
                    elif con=='2':keyboard.send('win+d')
                    elif con=='3':keyboard.send('alt+f4')
                    elif con=='4':keyboard.send('space')
                    print(con)
    except:
        continue