#! /usr/bin/python3
from twil import sendSMS
from firebase_admin import db
from twilio.rest import Client
from mod import *
import yaml
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

def check_attendance(r):
	if (db.reference('project/student/' + r +'/attendance/counter').get()/30) < 0.75:
		return True
	else:
		return False

def master():
    from firebase import firebase_cred
    with open('user.log','r') as f:
        users=f.read()
    users=yaml.load(users)

    for i in users:
        if check_attendance(i):
            print('Under Attendance. Sending SMS ...')
            ph = db.reference('project/student/'+i+'/phone').get()
            name = db.reference('project/student/'+i+'/name').get()
            roll = db.reference('project/student/'+i+'/roll').get()
            print(name, roll)
            usr = sendSMS.Job(ph,name,roll)
            sid = usr.send()
            if(sid):
                print("Success")
            else:
                print("MSG Error")
        else:
            pass


if __name__ =="__main__":
	main()