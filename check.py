#! /usr/bin/python3
from twil import sendSMS as s
from firebase import fire_laxz as fire
import yaml
from firebase_admin import db as d
from twilio.rest import Client

auth = 0

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
    with open('user.log','r') as f:
        users=f.read()
    users=yaml.load(users)
    for i in users:
        if fire.check_attendance(i):
            print('Under Attendance. Sending SMS ...')
            ph = d.reference('project/student/'+i+'/phone').get()
            name = d.reference('project/student/'+i+'/name').get()
            roll = d.reference('project/student/'+i+'/roll').get()
            print(name, roll)
            usr = s.Job(ph,name,roll)
            sid = usr.send()
            if(sid):
                print("Success")
            else:
                print("MSG Error")
        else:
            pass


if __name__ =="__main__":
	p_init()