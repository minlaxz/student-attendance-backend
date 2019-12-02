from firebase_admin import db as d
from datetime import date
u = [' ', ' ']
today = date.today()

def get_data(r):
	#u.clear()
	e = d.reference('project/student/' + r)
	print('Processing ...')
	r = g(e)
	if r is not None:
		for k , v in r.items():
			if(k == 'name'):
				#print("Name : {}".format(v))
				u[0] = v
			if(k == 'attendance'):
				#print("ID : {}".format(v))
				u[1] = v
		return u
	else:
		print('No user .')

def update_this(r):
	ref = d.reference('project/student/' + r)
	e = d.reference('project/student/' + r +'/attendance')
	f = e.get() + 1
	ref.update({
		u'attendance':f,
		u'last_update':today.day
	})

def register_this(n,r,f):
	ref = d.reference('project/student/'+r)
	print("Processing ....")
	try:
		ref.set({
			u'name':n,
			u'attendance':1,
			u'registered_date':today,
			u'last_update':today.day,
			u'roll':r,
			u'fingerID':f
		})
	except Exception as e:
		print(e)
	print("OK. User {} added to database.".format(n))


def check_user(r):
	ref = d.reference('project/student/' + r)
	if g(ref) == None:
		print("Registering ...")
		return True
		#register_this(n,r,f,ref)
	else:
		return False

def check_attendance(r):
	ref = d.reference('project/student/' + r +'/attendance/counter')
	if (ref.get()/40) < 0.75:
		return True
	else:
		return False

