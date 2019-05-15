class Job:
	def __init__(self,roll,posi):
		self.roll=roll
		self.posi=posi
		
	def count_this(self):
		import yaml
		with open('user.log','r') as f:
			users=f.read()
		users=yaml.load(users)
		users.append(self.roll)
		with open('user.log','w') as f:
			f.write(str(users))

	def who(self):
		import yaml
		with open('user.log','r') as f:
			users = f.read()
		users = yaml.load(users)
		print(users[self.posi])
		return(users[self.posi])