from firebase_admin import db
from datetime import datetime

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
		print('utils[register]: processing to firebase...')
		try:
			self.ref.set({
			u'name':self.name,
			u'attendance':{month : {day: {noon : dayObject.strftime("%d/%b/%Y,%X")}},counter:1},
			u'updated_date':dayObject.strftime("%c"),
			u'register_date_detail':dayObject.strftime("%c"),
			u'roll':self.roll,
			u'fingerID':self.id,
			u'phone':self.ph
		})
		except Exception as e:
			print(e)
		print("utils[register]: OK. User {} added to database.".format(self.name))
	
	def update_this(self):
		print('utils[update]: processing to firebase...')
		try:
			e = db.reference('project/student/'+self.roll+'/attendance/'+month)
			f = db.reference('project/student/'+self.roll+'/attendance/'+month+'/'+day+'/AM')
			g = db.reference('project/student/'+self.roll+'/attendance/counter')
			g.set(g.get()+1)
			if(f.get()):
				e.update({day: {"AM":f.get(), noon:dayObject.strftime("%d/%b/%Y,%X")}})
			else:
				e.update({day: {noon:dayObject.strftime("%d/%b/%Y,%X")}})
			self.ref.update({
				u'updated_date':dayObject.strftime("%c")
			})
			print("utils: Done")
		except Exception as e:
			print(e)
		print('utils[update]: OK. User {} updated to database'.format(self.name))
			
	def check_user(self):
		if self.ref.get()==None:
			print('Registering ...')
			return True
		else:
			print('User Exist in firebase database')
			return False

	def check_attendance(self):
		pass
