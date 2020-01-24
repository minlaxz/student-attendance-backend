from firebase_admin import db
from datetime import datetime

time_lock_bypass = False

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

    def __init__(self, name=None, rollNumber=None, fingerID=None, phone=None):
        self.name = name
        self.roll = rollNumber
        self.id = fingerID
        self.ph = phone
        self.ref = db.reference('project/student/'+rollNumber+'/')

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
        if(time_lock_bypass):
            timesession = 9
            print('utils[register]: time result (sos)', timesession)
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
            if(timesession > 1):
                for i in range(1, timesession-1, 1):
                    self.ref.update({
                        u'attendance': {
                            month: {
                                day: {
                                    i: 'N/A.'
                                }
                            }
                        }
                    })

            elif(timesession < 1):
                print('[utils] > Time Error.')
                raise Exception

        except Exception as e:
            print(e)
        print("utils[register]: user added to database.")

    def update_handler(self):
        print('utils[update]: processing to firebase...')
        timesession = self.timecheck()
        print('utils[update]: time session is', timesession)
        if(time_lock_bypass):
            timesession = 9
            print('utils[register]: time result (sos)', timesession)
        try:
            f = self.ref.child('attendance/counter')
            f.set(f.get()+1)
            print('utils[update]: major counter updated.')

            # https://raspberrypi75955.firebaseio.com/project/student/meec1/attendance/January/09/1

            if(self.ref.child('attendance/'+month+'/'+day+'/').get() == None):
                print('utils[update]: This is first scan of your, for today.')
                for i in range(1, 7, 1):
                    print('For timesession > {0}'.format(str(i)))
                    self.ref.child('attendance/'+month+'/'+day+'/').update({
                        i: 'No Record.'
                    })
            else:
                print('utils[update]: This user is Non-empty for today.')
                self.ref.child('attendance/'+month+'/'+day+'/').update({
                    timesession: dayObject.strftime("%d/%b/%Y,  %X")
                })
                print('utils[update]: update done.')

            self.ref.update({
                u'updated_date': dayObject.strftime("%c")
            })
            print("utils[update]: All Done")

        except Exception as e:
            print(e)
        print('utils[update]: OK. User {} updated to database'.format(self.name))


def timecheck():
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
# DEPRICATED
    # def register_this(self):
    #     print('utils[register]: processing to firebase...')
    #     try:
    #         self.ref.set({
    #             u'name': self.name,
    #             u'attendance': {month: {day: {noon: dayObject.strftime("%d/%b/%Y,%X")}}, 'counter': 1},
    #             u'updated_date': dayObject.strftime("%c"),
    #             u'register_date_detail': dayObject.strftime("%c"),
    #             u'roll': self.roll,
    #             u'fingerID': self.id,
    #             u'phone': self.ph
    #         })
    #     except Exception as e:
    #         print(e)
    #     print("utils[register]: OK. User {} added to database.".format(self.name))

    # def update_this(self):
    #     print('utils[update]: processing to firebase...')
    #     try:
    #         e = db.reference('project/student/'+self.roll+'/attendance/'+month)
    #         f = db.reference('project/student/'+self.roll +
    #                          '/attendance/'+month+'/'+day+'/AM')
    #         g = db.reference('project/student/'+self.roll +
    #                          '/attendance/counter')
    #         g.set(g.get()+1)
    #         if(f.get()):
    #             e.update(
    #                 {day: {"AM": f.get(), noon: dayObject.strftime("%d/%b/%Y,%X")}})
    #         else:
    #             e.update({day: {noon: dayObject.strftime("%d/%b/%Y,%X")}})
    #         self.ref.update({
    #             u'updated_date': dayObject.strftime("%c")
    #         })
    #         print("utils: Done")
    #     except Exception as e:
    #         print(e)
    #     print('utils[update]: OK. User {} updated to database'.format(self.name))
