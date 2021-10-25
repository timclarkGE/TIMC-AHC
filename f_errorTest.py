def errorTest(ser):
    from f_isError import isError
    from f_acmd import acmd
    import time

    print("Error 1: <Hello>")
    acmd(ser,"Hello")

    print("Error 2: <MOVEABS Drive_Axis_A 100 F 100\\n>")
    acmd(ser, "MOVEABS Drive_Axis_A 100 F 100")

    #NOTE: One can send the DISABLE command multiple times without getting # error
    print("Enable A, WAIT MODE = NOWAIT, Move Inc, Abort, WAIT MOVEDONE")
    acmd(ser,"ENABLE Drive_Axis_A")
    acmd(ser,"WAIT MODE NOWAIT")
    acmd(ser, "MOVEINC Drive_Axis_A 1000 F 100")
    time.sleep(1)
    acmd(ser, "ABORT Drive_Axis_A")
    acmd(ser, "WAIT MOVEDONE Drive_Axis_A")
    print(str(acmd(ser, "PFBK(Drive_Axis_A)"))) #Returns % character for successful command and then returns a number

    #After 10 seconds if no \n character controller times out
    #print("Error 3:")
    #ser.write(b'MOVEABS Drive_Axis_A 100 F 100')
    #time.sleep(11)
    #data = ser.readline().decode('ascii')
    #isError(data)

    print("Disable Drive A")
    ser.write(b'DISABLE Drive_Axis_A\n')
    data = ser.readline().decode('ascii')
    isError(data)

    print("Disable Drive B")
    ser.write(b'DISABLE Drive_Axis_B\n')
    data = ser.readline().decode('ascii')
    isError(data)
