import serial

ser = serial.Serial('/dev/cu.usbmodem142201', 9600, serial.EIGHTBITS)

while True:
    with open('datos.txt', 'a') as file:
        line = ser.readline().decode('utf_8')
        print(line)
        file.write(line)


