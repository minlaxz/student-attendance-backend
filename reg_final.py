#! /usr/bin/python3
"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
00p & functional r cod3d buy laxz : m.me/minlaxz
All rights reserved.
REGISTER FINAL++-++----
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
        global fp
        fp = pfp('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        if(fp.verifyPassword() == False):
            raise ValueError(error[1])
    except Exception as e:
        printall(error[2])
        print(error[4] + str(e))
        out(True)

    print(info[1] + str(fp.getTemplateCount()) +'/' + str(fp.getStorageCapacity()))
    # print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity())) ##CHECK
    try:
        name = input(info[11])
        printall(info[12]+name)

        roll = input(info[13])
        printall(info[14]+roll)

        phone = input(info[15])
        printall(info[16]+phone)

        print("Name:{0} , Roll:{1} , Phone:{2}".format(name, roll, phone))

        confirm = input(info[17])
        if(confirm == 'n'):
            out(False)
        if utils.Job(rollNumber=roll).check_user():
            timecheck = utils.timecheck()
            if (timecheck > 0 or time_lock_bypass):
                print(info[7]+str(timecheck))
                f = get_finger()
            else:
                raise Exception(reg_str)

            if (f.compareCharacteristics() == 0):
                printall(info[18])
                s(1)
            else:
                f.createTemplate()
                fingerID = str(f.storeTemplate())
                printall(info[19]+fingerID)
                user = utils.Job(name = name, rollNumber = roll, fingerID = fingerID, phone=phone)
                try:
                    user.register_handler()
                    s(1)
                    trans.Job(user.roll, None).count_this()
                except Exception as e:
                    printall(error[4]+str(e))
                printall(info[20])
        else:
            printall(error[5])

    except KeyboardInterrupt:
        printall(info[10])
        out(False)
    except Exception as e:
        printall(error[4]+str(e))


def get_finger():
    printall(info[21])
    while(fp.readImage() == False):
        pass
    printall(info[22])
    s(1)
    fp.convertImage(0x01)
    posi = fp.searchTemplate()[0]
    if(posi >= 0):
        printall(error[6])
        s(3)
    else:
        printall(info[3])
        s(1)
        printall(info[23])
        while (fp.readImage() == False):
            pass
        fp.convertImage(0x02)
    return fp

if __name__ == "__main__":
    while True:
        main()
