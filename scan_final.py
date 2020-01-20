#! /usr/bin/python3
"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
00p & functional r cod3d buy laxz : m.me/minlaxz
All rights reserved.
SCAN FINAL++--++++-----
"""
from mod import *
with open("info.txt") as f:
    info = f.readlines()
with open("error.txt") as f:
    error = f.readlines()

def main():
    if conn.check():
        printall(info[0])
        master()
    else:
        printall(error[0])
        out(True)

def master():
    from firebase import firebase_cred
    try:
        f = pfp('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        if(f.verifyPassword() == False):
            raise ValueError(error[1])
    except Exception as e:
        printall(error[2])
        print(error[4] + str(e))
        out(True)
    print(info[1] + str(f.getTemplateCount()) +'/' + str(f.getStorageCapacity()))
    try:
        printall(info[2])
        while(f.readImage() == False):
            pass
        printall(info[3])
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber,accu = result[0],result[1]
        if(positionNumber == -1):
            printall(info[4])
            s(1)
        else:
            print(info[5] + str(positionNumber))
            roll = trans.Job(None, positionNumber).who()
            printall(roll+' '+info[6]+str(accu))
            s(2)
            timecheck = utils.timecheck()
            if (timecheck > 0 or time_lock_bypass):
                print(info[7]+'{}'.format(timecheck))
            else:
                raise Exception(reg_str)
            printall(info[8])
            utils.Job(rollNumber=roll).update_handler()
            printall(info[9])
            s(2)

    except KeyboardInterrupt:
        print(info[10])
        out(False)
    except Exception as e:
        print(error[3])
        print(error[4] + str(e))

if __name__ == "__main__":
    while True:
        main()
