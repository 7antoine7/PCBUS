# This Python file uses the following encoding: utf-8
from ast import Try
from logging import exception
import serial
import serial.tools.list_ports


class serialCommunication:
    def __init__(self):
        self.ser = serial.Serial()
        self.baudrate = 115200
        self.port = None
        pass

    def connect(self):
        try:
            self.ser.open()
            return 0
        except:
            return -1

    def disconnect(self):
        try:
            self.ser.close()
            return 0
        except:
            return -1

    def send(self, message):
        try:
            self.ser.write(message)
            return 0
        except:
            return -1

    def setPort(self, port):
        self.ser.port = port

    def update(self):
        try:
            byteSize = self.ser.in_waiting()
            if byteSize > 0:
                return str(self.ser.read(1)) + str(self.ser.read(byteSize))
            else:
                return None
        except:
            return -1

    def listPort(self):
        info = serial.tools.list_ports.comports()
        ports = [str(ports.device) for ports in info]
        return ports


if __name__ == "__main__":
    test = serialCommunication()
    print(test.listPort())
