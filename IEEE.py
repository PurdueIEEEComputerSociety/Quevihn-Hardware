import serial

s = serial.Serial("/dev/tty.wchusbserial1420", 9600)
while(True):
    b = s.readline().decode("utf-8")
    c,f = b.split(";")
    print("celcius: " + c)
    print("fahrenheit: " + f)
    
