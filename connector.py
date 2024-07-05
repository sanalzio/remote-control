#○--- Imports ---○#

# import module for serial communication
import serial

# import module for listing serial ports
import serial.tools.list_ports

# import module for controlling mouse and keyboard
from pyautogui import *

# import module for system command calls
from os import system as call

#○--- Imports ---○#




#○--- Main ---○#


#○--- Detecting Bluetooth port ---○#

# asign serial ports to variable
ports = serial.tools.list_ports.comports()
# create list for bluetooth ports
bluetooth_ports = []
# create variable for serial port
port = None

# print info
print('Searching for serial port communication...')

# while loop to detect bluetooth
while len(bluetooth_ports) == 0:

    # for loop to list serial ports
    for (port, desc, hwid) in sorted(ports):

        # if statement to detect bluetooth
        if ('Bluetooth' in desc):

            # add bluetooth port to list
            bluetooth_ports.append(port)
            # print info
            print(f"Detected {desc}")

# for loop to list bluetooth ports
for this_port in bluetooth_ports:

    # for loop to list bluetooth ports
    for detected_port in bluetooth_ports:

        # if statement to compare bluetooth ports
        if int( this_port[ len(this_port) - 1 : ] ) > int( detected_port[ len(detected_port) - 1 : ] ):
            # set port to bluetooth port
            port = int(this_port[ len(this_port) - 1 : ])


#○--- Detecting Bluetooth port ---○#



# print info
print(f"Using {port}")



#○--- Listening Bluetooth port for commands ---○#

# create infinite loop
while True:

    # try except block
    try:

        # start serial communication
        with serial.Serial('COM' + str(port), 9600, timeout = 1) as ser:

            # while loop to read data
            while True:

                # read data and convert to string
                line = ser.readline()
                content = str(line)[ 2 : len(str(line)) - 5 ]

                # if statement to check if data is not empty
                if len(str(line)) != 3:

                    # if statement to check if data starts with $
                    if content.startswith("$"):

                        # execute system command
                        call(content[1:])
                        # print info
                        print(" $ " + content[1:])

                    else:

                        # execute python code
                        exec(content)
                        # print info
                        print(content)

    except Exception as e:
        print(e)


#○--- Listening Bluetooth port for commands ---○#


#○--- Main ---○#
