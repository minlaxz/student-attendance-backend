import firebase.firebase_cred
from firebase_admin import db

def main():
	roll = input("Roll No?: ")
	g = db.reference('project/student/'+roll+'/attendance/counter')
	if(g.get() != None):
		print("roll no."+roll+" is valid.")
		mode = input("update or delete?(u/d): ")
		if (mode=='u' or mode=='U'):
			print("update mode...")
			update_this(g)
		elif(mode=='d' or mode=='D'):
			print("delete mode...")
			print("deleting in 5 sec from NOW!'Press ctrl+c to cancle this process'")
			time.sleep(5)
			delete_this(g)
		else:
			print("invalid. exit with error 0")

	else:
		print("roll no."+roll+" is invalid 'not exist in database'.")

def update_this(g):
	mode = input("phone,roll_count,name?(p,r,n): ")
	if(mode=='p' or mode=='P'):
		cphone = g.parent.parent.child('phone').get()
		print("database's current phone: "+ cphone)
		phone = input("enter phone no: ")
		g.parent.parent.update({u'phone':phone})
		if(g.parent.parent.child('phone').get()==phone):
			print("Done.")
			print(cphone + " :changed to: " + phone)
		else:
			print("Failed.")
	elif(mode=='r' or mode=='R'):
		croll = str(g.get())
		print("database's current roll_count: " + croll)
		adder = input("How many do you want to add?: ")
		f=g.get()
		g.set(int(adder)+f)
		if(g.get()==int(adder)+f):
			print("Done.")
			print(croll + " :changed to:" + str(g.get()))
		else:
			print("Failed.")
	elif(mode=='n' or mode=='N'):
		cname = g.parent.parent.child('name').get()
		print("database's current name: "+ cname)
		name = input("enter name: ")
		g.parent.parent.update({u'name':name})
		if(g.parent.parent.child('name').get()==name):
			print("Done.")
			print(cname + " :changed to: " + name)
		else:
			print("Failed.")


def delete_this(g):
	g.parent.parent.parent.child(roll).delete()


if __name__ == "__main__":
	main()