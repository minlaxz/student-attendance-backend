#THIS IS BETA
from firebase_admin import db
from datetime import date,datetime
today=date.today()
class Job:
	print("00p developed by ...")
	def __init__(self,name,rollNumber,fingerID):
		self.name=name
		self.roll=rollNumber
		self.id=fingerID
		self.ref=db.reference('project/student/'+rollNumber)

	def register_this(self):
		print('processing...')
		try:
			self.ref.set({
			u'name':self.name,
			u'attendance':1,
			u'registered_date':str(date.today()),
			u'last_update':str(date.today().day),
			u'last_update_long':str(datime.today()),
			u'roll':self.roll,
			u'fingerID':self.id
		})
		except Exception as e:
			print(e)
		print("OK. User {} added to database.".format(self.name))
	
	def update_this(self):
		print('processing...')
		try:
			e=(db.reference('project/student/'+self.roll+'/attendance').get())+1
			self.ref.update({
				u'attendance':e,
				u'last_update':date.today().day,
				u'last_update_long':str(datetime.today())
			})
		except Exception as e:
			print(e)
			
	def check_user(self):
		if self.ref.get()==None:
			print('Registering ...')
			return True
		else:
			print('User Exist')
			return False
