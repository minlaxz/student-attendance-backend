class Job:
    def __init__(self,ph,name,roll):
        self.ph = ph
        self.name = name
        self.roll = roll

    def send(self):
        from twilio.rest import Client
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)
        message = client.message.create(
            to="+95"+str(ph[1:len(ph)]),
            from_="+12015975855",
            body="User " + str(name)+ " " +str(roll) + " is under attendace."
        )
        return message.sid