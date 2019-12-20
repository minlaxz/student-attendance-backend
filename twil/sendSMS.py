class Job:
    def __init__(self,ph,name,roll):
        self.ph = ph
        self.name = name
        self.roll = roll

    def send(self):
        from twilio.rest import Client
        account_sid = "AC8e7bc4b73556d29d34b061238467bc66"
        auth_token = "58f42bc8cb3b852aff386b924d2d7aa0"
        client = Client(account_sid, auth_token)  #auth
        message = client.messages.create(
            to="+95"+str(self.ph[1:len(self.ph)]),
            from_="+19727464285",
            body="Student: " + str(self.name)+ "," +str(self.roll) + " is under 75% attendance in this month."
        )  #msg end
        return message.sid
