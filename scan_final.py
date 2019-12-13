#! /usr/bin/python3
"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
00p & functional r cod3d buy laxz : m.me/minlaxz
All rights reserved.
"""
#SCAN

auth = 0
import time
from firebase import firebase_utils as utils
import oled.oled_device as oled
import translator as trans
def p_init():
	import conn
	if not conn:
		print("no internet!")
		exit(1)
	if auth == 0:
		auth_laxz()
	else:
		pass
	p__init()
def auth_laxz():
	try:
		import firebase.firebase_cred
		auth=1
	except Exception as e:
		print("Exception Message: "+str(e))
def p__init():
	from pyfingerprint.pyfingerprint import PyFingerprint as pfp
	import firebase.fire_laxz as fire
	try:
		f = pfp('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
		if(f.verifyPassword() == False):
			raise ValueError("Sensor password is wrong.")
	except Exception as e:
		print("[ERROR] :Fingerprint sensor could not be initialized!")
		print("Exception Message : " + str(e))
		print("[ERROR] :Exiting ...")
		exit(1)
	print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
	try:
		print("[INFO] :Waiting for finger ...")
		_s("Waiting for finger ..")
		while(f.readImage()== False):
			pass
		time.sleep(0.5)
		print("Remove your finger ...")
		_s("Remove your finger.")
		f.convertImage(0x01)
		result = f.searchTemplate()
		positionNumber = result[0]
		accu = result[1]
		if(positionNumber == -1):
			print("[INFO] :No match found!")
			_s("No match found!")
			time.sleep(1)
			#exit(0)
		else:
			print("[RESULT] :Found template at position : " + str(positionNumber))
			print("[RESULT] :The accurancy score is: "+ str(accu))
			user=trans.Job(None,positionNumber).who()
			_s(user+"                  Accurancy Score: "+str(accu))
			time.sleep(2)
			_s("Updating in database ... " + user)
			utils.Job(None,user,None,None,None).update_this()
			print("Developed by Thazin Phyu")
			_s("Developed by Thazin Phyu")
			time.sleep(2)
	except KeyboardInterrupt:
		print("[INFO] :ABRODED by user .")
		exit(0)
	except Exception as e:
		print("[ERROR] :OPERATION Failed.")
		print("[ERROR] :Exception message: " + str(e))
		#exit(1)


def _s(m):
	oled.show_text_sm(m)

if __name__=="__main__":
	while True:
		p_init()
