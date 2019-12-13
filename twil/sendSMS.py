class Job:
    def __init__(self,ph,name,roll):
        self.ph = ph
        self.name = name
        self.roll = roll

    def send(self):
        from twilio.rest import Client
        account_sid = "ACad597acdc047697847ac3d71c3bd558f"
        auth_token = "d1475cd82a1e0ae7f5d795669ec3fef4"
        client = Client(account_sid, auth_token)  #auth
        message = client.messages.create(
            to="+95"+str(self.ph[1:len(self.ph)]),
            from_="+12055516681",
            body="Student: " + str(self.name)+ "," +str(self.roll) + " is under 75% attendance in this month."
        )  #msg end
        return message.sid
