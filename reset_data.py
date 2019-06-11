#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
'''laxz'''
"""

from pyfingerprint.pyfingerprint import PyFingerprint
import time
from sys import exit

## Deletes a finger from sensor

def init_sensor():

    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    used = f.getTemplateCount() #0,1,2,3 = 4
    print('Currently used templates: ' + str(used) +'/'+ str(f.getStorageCapacity()))

    if(used > 0):
        del_me()
    else:
        print("Nothing to be deleted !")
        print("Exit.")

def del_me():

    user = input("Delete from module? y/n:")
    if (user == 'y'):

        try:
            print("Fingerprints deleting in... 5s ")
            for i in range(1,6):
                print(str(i)+ " sec.")
                time.sleep(1)

            for i in range(used):
                if(f.deleteTemplate(i) == True):
                    print("Template deleted from position {0}".format(i))
                else:
                    print("Internal Error")

        except KeyboardInterrupt:
            print("-fingerprint delete- operation cancled")
            exit(0)

        except Exception as e:
            print(str(e))
            print('Operation failed!')
            exit(1)
    else:
        print('Adios Amigos!')
        exit(0)

    userlog = input("Override user.log file? y/n:")

    if(userlog == 'y'):

        userLogOverwrite()

    else:
        print("You may get error with module, manaully overwrite user.log file")
        exit(0)

    print("All done TODO delete firebase database childs.")
def userLogOverwrite():
    users = '[]\n'
    with open('user.log','w') as f:
        f.write(users)



if __name__=='__main__':

    init_sensor()
