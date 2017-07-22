import random
class dsl(object):
    def __init__(self,intent):
        self.rep = "error"
        self.website(intent)
        self.goodbye(intent)
        self.contact(intent)
        self.location(intent)
    def generate(self):
        return self.rep
    def website(self,intent):
        if intent == "website":
            self.rep = random.choice(["here is the RIT website:(www.rit.ac.in)","check this out:(www.rit.ac.in)","click here:(www.rit.ac.in)"])
    def goodbye(self,intent):
        if intent == "goodbye":
            self.rep = random.choice(["bye see you","have a nice day","good bye","take care","see you soon"])
    def contact(self,intent):
        if intent == "contact":
            self.rep = random.choice(["here is some information:(8281427437)","here you go:(8281427437)","contact:(8281427437)"])
    def location(self,intent):
        if intent == "location":
            self.rep = random.choice(["here is the address:(address)","i will navigate you:(address)","RIT is here:(address)","Look at this:(address)"])
