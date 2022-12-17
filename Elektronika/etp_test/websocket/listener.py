import serial,subprocess

subprocess.run(['sudo','chmod','a+wr','/dev/ttyACM0'])

ser=serial.Serial('/dev/ttyACM0',timeout=2)

# while True:
#     content=ser.readline()
#     print(content)

string='0'
# while True:
#     if string == '1': string='0'
#     else: string='1'
#     print('sent',string)
#     ser.write(string.encode())
#     content=ser.readline()
#     print(content)
ser.write(string.encode())
content=ser.readline()
print(content)