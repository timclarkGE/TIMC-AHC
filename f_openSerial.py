import serial
import time

def openSerial():
    port = "COM"
    baud = 115200

    serialError = 0

    for x in range(1, 100):
         try:
             ser = serial.Serial(port+str(x), baud, timeout = 0.05)
         except Exception as e:
             serialError = serialError + 1
    if serialError >= 99:
        print("")
        time.sleep(1)
        print("===============================================")
        print("Error: No Serial Port Identified.")
        print("COM1 through COM100 were tested with no results")
        print("===============================================")
        print("Is it plugged in or turned on?")
        print("It's most likely a problem between the seat and keyboard.")
        print("")
        time.sleep(5)
        exit()
    if ser.isOpen():
        print("Serial port " + ser.name + " successfully opened.")
        return ser
