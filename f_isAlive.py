import time

def isAlive(ser):
    from f_isError import isError

    #Write simple command to controller, acknowledges all faults
    ser.write(b'ACKNOWLEDGEALL\n')
    data = ser.readline().decode('ascii')
    print("Data:")
    print(data)

    if "%" in data:
        print("Communication Established with Controller")
        return 1
    else:
        print("")
        time.sleep(1)
        print("===============================================")
        print("Error: No Communication with Controller.")
        print("===============================================")
        print("Is the controller turned on and plugged in?")
        print("It's most likely a problem between the seat and keyboard.")
        print("")
        time.sleep(5)
        exit()
        return 0