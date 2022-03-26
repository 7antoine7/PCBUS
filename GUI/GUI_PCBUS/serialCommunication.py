# This Python file uses the following encoding: utf-8
from ast import Try
from logging import exception
import serial
import serial.tools.list_ports
import time


class serialCommunication:
    def __init__(self):
        self.ser = serial.Serial(timeout = 0)
        self.ser.baudrate = 115200
        self.ser.port = None
        self.line = []
        pass

    def connect(self):
        try:
            self.ser.open()
            print("conection")
            self.send("\r\n\r")
            time.sleep(2)
            self.ser.flushInput()
            return 0
        except Exception as e:
            print(str(e))
            return -1

    def disconnect(self):
        try:
            self.ser.close()
            return 0
        except:
            return -1

    def send(self, message):
        try:
            message += '\n'
            self.ser.write(message.encode('ascii'))
            print("send")
            return 0
        except Exception as e:
            print(str(e))
            return -1

    def setPort(self, port):
        self.ser.port = port

    def update(self):
        try:
            byteSize = self.ser.in_waiting
            newlines = []
            if byteSize > 0:
                for c in self.ser.read(byteSize):
                    self.line.append(chr(c))
                    if chr(c) == '\r':
                        print("Line: " + ''.join(self.line))
                        newlines.append(''.join(self.line).strip())
                        self.line = []
                return newlines
        except Exception as e:
            print(str(e))

    def listPort(self):
        info = serial.tools.list_ports.comports()
        ports = [str(ports.device) for ports in info]
        return ports


if __name__ == "__main__":
    test = serialCommunication()
    print(test.listPort())
