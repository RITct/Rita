import random
class dsl(object):
    def __init__(self,intent):
        self.rep = {}

        self.website(intent)
        self.goodbye(intent)
        self.contact(intent)
        self.location(intent)
        self.greetings(intent)
    def generate(self):
        return self.rep
    def website(self,intent):
        if intent == "website":
            self.rep["text"] = random.choice(["here is the RIT website:(www.rit.ac.in)","check this out:(www.rit.ac.in)","click here:(www.rit.ac.in)"])
            self.rep["title"] = "college website"
            self.rep["url"] = "www.rit.ac.in"
    def goodbye(self,intent):
        if intent == "goodbye":
            self.rep["text"] = random.choice(["bye see you","have a nice day","good bye","take care","see you soon"])
    def contact(self,intent):
        if intent == "contact":
            self.rep["text"] = random.choice(["here is some information:(8281427437)","here you go:(8281427437)","contact:(8281427437)"])
            self.rep["post_back"] = True
            self.rep["post_content"] = "8281427437"
    def location(self,intent):
        if intent == "location":
            self.rep["text"] = random.choice(["here is the address:(address)","i will navigate you:(address)","RIT is here:(address)","Look at this:(address)"])
    def greetings(self,intent):
        if intent == "greeting":
            self.rep["text"] = random.choice(["hello there","Hi","hi there","its good to see you","hello"])
