"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
oop and functional coded by laxz : m.me/minlaxz
All rights reserved.
"""
#REGISTER
from firebase import firebase_utils as utils
import oled.oled_device as oled
import translator as trans
import time
auth = 0

def _init():
	import conn
	if not conn:
		print("no internet")
		exit(1)
	if auth == 0:
		auth_laxz()
	else:
		pass
	__init()

def auth_laxz():
	from firebase import firebase_cred
	auth = 1

def __init():
	from pyfingerprint.pyfingerprint import PyFingerprint as pfp
	try:
		f = pfp('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
		if(f.verifyPassword() == False):
			raise ValueError("Sensor password is wrong.")
	except Exception as e:
		print("[ERROR] :Fingerprint sensor could not be initialized!")
		print("Exception Message : " + str(e))
		print("[ERROR] :Exiting ...")
		exit(1)
	_s("used templates: {0}".format(f.getTemplateCount()))
	time.sleep(1)

	#print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
	try:
		name = input("Enter Name: ")
		_s("Processing for {0}".format(name))
		roll = input("Enter Roll(eg:5ec39): ")
		_s("Roll number is :{0}".format(roll))
		if fire.check_user(roll):
			f=get_finger()
			if (f.compareCharacteristics()==0):
				_s("Finigerprints do not match! resetting ...")
				print("Don not match! try again.")
				time.sleep(2)
			else:
				f.createTemplate()
				fingerID = str(f.storeTemplate())
				_s("Enrolled Successfully")
				print("Enrolled Successfully, at Position: "+ fingerID)
				user=utils.Job(name,roll,fingerID)
				user.register_this()
				_s("Registered to firebase")
				time.sleep(1)
				try:
					trans.Job(user.roll,None).count_this()
				except Exception as e:
					print(e)
				_s("Registered to local translator.")
				time.sleep(1)
				print("Process Done!")
		else:
			print("User found is database.")
			_s("Error")

	except KeyboardInterrupt:
		#raise Exception("User stopped the program")
		print("\n user STOPPED the program")
		_s("user stopped.")
		time.sleep(1)
		exit(0)
	except Exception as e:
		print(str(e))
		exit(1)

def get_finger():
	_s("Waiting for finger image...")
	print("[INFO] :Waiting for finger ...")
	while(f.readImage()== False):
		pass
	_s("Enrolling.. Hold on.")
	print("Please hold on ...")
	time.sleep(1)
	f.convertImage(0x01)
	position = f.searchTemplate()[0]
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
		while (f.readImage()==False):
			pass
		f.convertImage(0x02)
	return f

def _s(m):
	oled.show_text_sm(m)

if __name__ =="__main__":
	while True:
		_init()
