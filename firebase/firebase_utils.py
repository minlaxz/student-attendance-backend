from firebase_admin import db
from datetime import datetime

dayObject = datetime.now()
day = dayObject.strftime("%d")
month = dayObject.strftime("%B")
year = dayObject.strftime("%Y")
x = dayObject.strftime("%x")
X = dayObject.strftime("%X")
noon = dayObject.strftime("%p")
hm = int(dayObject.strftime('%H%M'))


class Job:
    print("utils[Job Class]: 00p developed by .")

    def __init__(self, name, rollNumber, fingerID, phone):
        self.name = name
        self.roll = rollNumber
        self.id = fingerID
        self.ph = phone
        self.ref = db.reference('project/student/'+rollNumber)

    def timecheck(self):
        if (hm > 900 and hm < 950):
            return 1
        elif (hm > 955 and hm < 1045):
            return 2
        elif (hm > 1050 and hm < 1140):
            return 3
        elif (hm > 1230 and hm < 1320):
            return 4
        elif (hm > 1325 and hm < 1415):
            return 5
        elif (hm > 1420 and hm < 1510):
            return 6
        else:
            return -1

    def register_this(self):
        print('utils[register]: processing to firebase...')
        try:
            self.ref.set({
                u'name': self.name,
                u'attendance': {month: {day: {noon: dayObject.strftime("%d/%b/%Y,%X")}}, 'counter': 1},
                u'updated_date': dayObject.strftime("%c"),
                u'register_date_detail': dayObject.strftime("%c"),
                u'roll': self.roll,
                u'fingerID': self.id,
                u'phone': self.ph
            })
        except Exception as e:
            print(e)
        print("utils[register]: OK. User {} added to database.".format(self.name))

    def update_this(self):
        print('utils[update]: processing to firebase...')
        try:
            e = db.reference('project/student/'+self.roll+'/attendance/'+month)
            f = db.reference('project/student/'+self.roll +
                             '/attendance/'+month+'/'+day+'/AM')
            g = db.reference('project/student/'+self.roll +
                             '/attendance/counter')
            g.set(g.get()+1)
            if(f.get()):
                e.update(
                    {day: {"AM": f.get(), noon: dayObject.strftime("%d/%b/%Y,%X")}})
            else:
                e.update({day: {noon: dayObject.strftime("%d/%b/%Y,%X")}})
            self.ref.update({
                u'updated_date': dayObject.strftime("%c")
            })
            print("utils: Done")
        except Exception as e:
            print(e)
        print('utils[update]: OK. User {} updated to database'.format(self.name))

    def check_user(self):
        if self.ref.get() == None:
            print('Registering ...')
            return True
        else:
            print('User Exist in firebase database')
            return False

    def register_handler(self):
        print('utils[register]: processing to firebase...')
        timesession = self.timecheck()
        print('utils[register]: time result ', timesession)
        try:
            self.ref.set({
                u'name': self.name,
                u'attendance': {
                    month: {
                        day: {
                            timesession: dayObject.strftime("%d/%b/%Y,  %X")
                        }
                    },
                    'counter': 1},
                u'updated_date': dayObject.strftime("%c"),
                u'register_date_detail': dayObject.strftime("%c"),
                u'roll': self.roll,
                u'fingerID': self.id,
                u'phone': self.ph
            })
        except Exception as e:
            print(e)
        print("utils[register]: OK. User {} added to database.".format(self.name))

    def update_handler(self):
        print('utils[update]: processing to firebase...')
        timesession = self.timecheck()
        try:
            g = db.reference('project/student/'+self.roll + '/attendance/counter')
            g.set(g.get()+1)

            e = db.reference('project/student/'+self.roll+'/attendance/'+month)

            f = db.reference('project/student/'+self.roll +'/attendance/'+month+'/'+day+'/'+timesession)
			# https://raspberrypi75955.firebaseio.com/project/student/meec1/attendance/January/09/1
            if (not f.get()):
                e.update(
					{
						day: {
							timesession: dayObject.strftime("%d/%b/%Y,  %X")
							}
					}
				)
            else:
	            pass

            self.ref.update({
                u'updated_date': dayObject.strftime("%c")
            })
            print("utils: Done")

        except Exception as e:
            print(e)
        print('utils[update]: OK. User {} updated to database'.format(self.name))
