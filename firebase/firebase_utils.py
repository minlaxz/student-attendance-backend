#THIS IS BETA
from firebase_admin import db
from datetime import date,datetime
today=date.today()

dayObject = datetime.now()
day = dayObject.strftime("%W")
month = dayObject.strftime("%B")
year = dayObject.strftime("%Y")

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
			u'attendance':{month : {day:'Present'}},
			u'registered_date':year+'-'+month+'-'+day,
			u'register_date_detail':str(dayObject),
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
			print('User Exist in firebase database')
			return False
