# remote-control

A code that allows you to execute any system command and Python code on a target computer using an Arduino and a Bluetooth module.

## Installation
It's sufficient to ensure that this code runs every time the target computer starts.

## Usage
Install it on the target computer and run the circuit you will create with Bluetooth modules like HC-05 or HC-06. The circuit will detect and connect to the Bluetooth module if it is on. You can tell if it is connected by the LED light on the Bluetooth module. Afterwards, the code will execute commands sent over the Bluetooth connection of the circuit.

### Running Python code

If you want to run Python code, simply send the code line over the serial Bluetooth connection.

### Executing system commands

Simply place the `$` character before the command and send it over the serial Bluetooth connection.

## Warning

I do not take responsibility for the use of this code. By using this code, you accept that the responsibility lies with you. This code is written for entertainment purposes. It is not recommended to use it without the consent of the owner of the target computer.
