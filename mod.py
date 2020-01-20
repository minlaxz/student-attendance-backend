import translator as trans
import oled.oled_device as oled
from firebase import firebase_utils as utils
from pyfingerprint.pyfingerprint import PyFingerprint as pfp
import time, conn


time_lock_bypass = False

reg_str = '''
#######################################################
#      Attendance Enrollment time is INCORRECT        #
#                                                     #
# Time is only valid for officially defined routines. #
#                                                     #
# Eg: for -                                           #
#                                                     #
#   Session 1 valid between 9:00 AM and 9:50 AM UTC   #
#   Session 2 valid between 9:55 AM and 10:45 AM UTC  #
#   Session 3 valid between 10:50 AM and 11:40 AM UTC #
#   ---break time----                                 #
#   Session 4 valid between 12:30 PM and 1:20 PM UTC  #
#   Session 5 valid between 1:25 PM and 2:15 PM UTC   #
#   Session 6 valid between 2:20 PM and 3:10 PM UTC   #
#######################################################
'''

def printall(m):
    print(m)
    oled.show_text_sm(m)

def s(t):
    time.sleep(t)

def out(flag):
    if flag:
        exit(1)
    else:
        exit(0)