def acmd(ser, text):
    from f_isError import isError

    ser.write(text.encode('ascii') + b' \n')
    data = ser.readline().decode('ascii')
    returnValue = isError(data, ser)
    if(returnValue == 0):
        data = data.replace("%","")
        return data
