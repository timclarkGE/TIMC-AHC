#Run Motor Up and Stop Abruptly
def RunMotorUp(ser):
    print('s r0x37 200')
    ser.write(b's r0x37 200\r')
    data = ser.readline().decode('ascii')
    print(data)

    print('s r0x2f 503808')
    ser.write(b's r0x2f 503808\r')
    data = ser.readline().decode('ascii')
    print(data)

    print('s r0x24 11')
    ser.write(b's r0x24 11\r')
    data = ser.readline().decode('ascii')
    print(data)

    i = 500
    while i:
        ser.write(b'g r0x18\r')
        data = ser.readline().decode('ascii')
        print(data)
        i = i-1
    print('s r0x24 0')
    ser.write(b's r0x24 0\r')
    data = ser.readline().decode('ascii')
    print(data)
