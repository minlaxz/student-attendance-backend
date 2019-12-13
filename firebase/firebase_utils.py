from firebase_admin import db
from datetime import date,datetime
today=date.today()

dayObject = datetime.now()
day = dayObject.strftime("%d")
month = dayObject.strftime("%B")
year = dayObject.strftime("%Y")
x = dayObject.strftime("%x")
X = dayObject.strftime("%X")
noon = dayObject.strftime("%p")

class Job:
	print("00p developed by .")
	def __init__(self,name,rollNumber,fingerID,ph,check_att):
		self.name=name
		self.roll=rollNumber
		self.id=fingerID
		self.ph=ph
		self.ref=db.reference('project/student/'+rollNumber)
		self.check_att=check_att
	def register_this(self):
		print('processing...')
		try:
			self.ref.set({
			u'name':self.name,
			#u'attendance':{month : {day:'Present'}},
			u'attendance':{month : {day: {noon : "Present"}},counter:1},
			u'updated_date':year+'-'+month+'-'+day,
			u'register_date_detail':str(dayObject),
			u'register_date_short': str(x +"-"+ X),
			u'roll':self.roll,
			u'fingerID':self.id,
			u'phone':self.ph
		})
		except Exception as e:
			print(e)
		print("OK. User {} added to database.".format(self.name))
	
	def update_this(self):
		print('utils: processing to firebase...')
		try:
			#e=(db.reference('project/student/'+self.roll+'/attendance').get())+1
			e = db.reference('project/student/'+self.roll+'/attendance/'+month)
			f = db.reference('project/student/'+self.roll+'/attendance/'+month+'/'+day+'/AM')
			g = db.reference('project/student/'+self.roll+'/attendance/counter')
			g.set(g.get()+1)
			if(f.get()):
				e.update({day: {"AM":"Present",noon:"Present"}})
			else:
				e.update({day: {noon:"Present"}})
			self.ref.update({
				#u'attendance':{month : {day:'Present'}},
				u'updated_date':year+"-"+month+"-"+day
			})
			print("utils: Done")
		except Exception as e:
			print(e)
			
	def check_user(self):
		if self.ref.get()==None:
			print('Registering ...')
			return True
		else:
			print('User Exist in firebase database')
			return False

	def check_attendance(self):
		pass
