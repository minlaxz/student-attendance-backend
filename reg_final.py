"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>

oop and functional coded by <laxz> :github.com/minlaxz
All rights reserved.
"""

#REGISTER
from firebase import firebase_utils as utils
from firebase import fire_laxz as fire
import oled.oled_device as oled
import translator as trans
import time
import sys
auth = 0

reg_str = '''
#######################################################
#           Registration time is INCORRECT            #
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

def p_init():
	import conn
	if not conn:
		print("no internet")
		exit(1)
	if auth == 0:
		auth_laxz()
	else:
		pass
	p__init()

def auth_laxz():
	from firebase import firebase_cred
	auth = 1

def p__init():
	from pyfingerprint.pyfingerprint import PyFingerprint as pfp
	try:
		global fp
		fp = pfp('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
		if(fp.verifyPassword() == False):
			raise ValueError("Sensor password is wrong.")
	except Exception as e:
		print("[ERROR] :Fingerprint sensor could not be initialized!")
		print("Exception Message : " + str(e))
		print("[ERROR] :Exiting ...")
		exit(1)
	_s("used templates: {0}".format(fp.getTemplateCount()))
	time.sleep(1)

	#print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity())) ##CHECK 
	try:
		name = input("Enter Name: ")
		_s("Processing for {0}".format(name))
		roll = input("Enter Roll(eg:meec1): ")
		_s("Roll number is :{0}".format(roll))
		ph = input("Enter Phone Number: ")
		_s("Phone Number is:{0}".format(ph))
		print("Name:{0} , Roll:{1} , Phone:{2}".format(name,roll,ph))
		confirm = input("Correct ? y/n:")
		if(confirm == 'y'):
			user = utils.Job(name,roll,None,ph,None)
		else:
			exit(0)
		if user.check_user():
			timecheck = user.timecheck()
			if (timecheck > 0):
				print('Register Pipeline is initiated for session {}'.format(timecheck))
				f = get_finger()
			else:
				raise Exception (reg_str)

			if (f.compareCharacteristics()==0):
				_s("Finigerprints do not match! resetting ...")
				print("Don not match! try again.")
				time.sleep(2)
			else:
				f.createTemplate()
				fingerID = str(f.storeTemplate())
				_s("Enrolled Successfully to fingerprint module")
				print("Enrolled Successfully to fingerprint module, at Position: "+ fingerID)
				user = utils.Job(name,roll,fingerID,ph,None)

				try:
					user.register_this()
					_s("Registered to Firebase")
					print("Registered to Firebase")

					time.sleep(1)

					trans.Job(user.roll,None).count_this()

					_s("Registered to local translator.")
					print("Registered to local translator.")

					time.sleep(1)

					#TODO to ensure that everything is update after that store in module.

				except Exception as e:
					print(str(e))

				print("Process Done!")
		else:
			print("User is found in database.")
			_s("User found : Error")

	except KeyboardInterrupt:
		#raise Exception("User stopped the program")
		print("\n user STOPPED the program")
		_s("user stopped.")
		#del user
		time.sleep(1)
		exit(0)
	except Exception as e:
		#print(str(e))
		#exit(1)
		print(e)

def get_finger(): #TODO compare characteristics here and return filtered data
	_s("Waiting for finger image...")
	print("[INFO] :Waiting for finger ...")
	while(fp.readImage()== False):
		pass
	_s("Enrolling.. Hold on.")
	print("Please hold on ...")
	time.sleep(1)
	fp.convertImage(0x01)
	position = fp.searchTemplate()[0]
	result = fp.searchTemplate()[1]
	if(position >= 0):
		_s("This user fingerprint already exists.")
		print("Already exists at :{0} and accurancy:{1}".format(position,result[1]))
		time.sleep(3)
	else:
		_s("Remove Finger.")
		print("Remove finger")
		time.sleep(1)
		_s("Waiting for same finger again.")
		print('Waiting for same finger again...')
		while (fp.readImage()==False):
			pass
		fp.convertImage(0x02)
	return fp

def _s(m):
	oled.show_text_sm(m)

if __name__ =="__main__":
	while True:
		p_init()
