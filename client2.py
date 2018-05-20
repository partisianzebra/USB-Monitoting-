#!usr/bin/python
from socket import *
import os,string,time
from ctypes import windll
import winsound
import getpass
 
host = 'localhost' # '127.0.0.1' can also be used
port = 52000
username = getpass.getuser()
 
sock = socket()
#Connecting to socket
sock.connect((host, port)) #Connect takes tuple of host and port
def get_driveStatus():
    devices = []
    record_deviceBit = windll.kernel32.GetLogicalDrives()
    for label in string.uppercase : #The uppercase letters 'A-Z'
        if record_deviceBit & 1:
            devices.append(label)
        record_deviceBit >>= 1
    return devices

def detect_device():
        original = set(get_driveStatus())
        time.sleep(3)
        add_device =  set(get_driveStatus())- original
        subt_device = original - set(get_driveStatus())

        if (len(add_device)):
            for drive in add_device:
                    sock.send("Device Added in " + username)
                    duration = 1300  # millisecond
                    freq = 400  # Hz
                    winsound.Beep(freq, duration)                
        elif(len(subt_device)):
            print "There were %d"% (len(subt_device))
            for drive in subt_device:
                    sock.send("Device Removed in " + username)
                    duration = 1300  # millisecond
                    freq = 400  # Hz
                    winsound.Beep(freq, duration)
 
#Infinite loop to keep client running.
while True:
    data = sock.recv(1024)
    if (data == 'Hi'):
      while True:
          detect_device()
 
sock.close()