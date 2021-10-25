def disableDrive(ser, axisNameArray):
    from f_isError import isError
    import time
    i = 0
    while i < len(axisNameArray):
        ser.write(b'DISABLE ' + axisNameArray[i].encode('ascii') + b' \n' )
        data = ser.readline().decode('ascii')
        isError(data, ser)
        ser.write(b'ABORT ' + axisNameArray[i].encode('ascii') + b' \n' )
        data = ser.readline().decode('ascii')
        isError(data, ser)
        i += 1
