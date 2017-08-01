import random
class dsl(object):
    def __init__(self,intent):
        self.rep = {}
        self.die(intent)
        self.website(intent)
        self.tinkerhub(intent)
        self.contact(intent)
        self.location(intent)
        self.principal(intent)
        self.coin(intent)
    def generate(self):
        return self.rep
    def website(self,intent):
        if intent == "website":
            self.rep["text"] = random.choice(["here is the RIT website:(www.rit.ac.in)","check this out:(www.rit.ac.in)","click here:(www.rit.ac.in)"])
            self.rep["title"] = "college website"
            self.rep["url"] = "www.rit.ac.in"
    def tinkerhub(self,intent):
        if intent == "tinkerhub":
            self.rep["text"] = random.choice(["a group of awesome poeple in RIT","check this out:(www.ritcreativeteam.ml)","a club under tinkerhub foundation"])
            self.rep["title"] = "tinkerhub website"
            self.rep["url"] = "www.ritcreativeteam.ml"
    def contact(self,intent):
        if intent == "contact":
            self.rep["text"] = random.choice(["here is some information:(8281427437)","here you go:(8281427437)","contact:(8281427437)"])
            self.rep["post_back"] = True
            self.rep["post_content"] = "8281427437"
    def location(self,intent):
        if intent == "location":
            self.rep["text"] = random.choice(["here is the address:(address)","i will navigate you:(address)","RIT is here:(address)","Look at this:(address)"])
    def principal(self,intent):
        if intent == "principal":
            self.rep["text"] = random.choice(["check out RIT website","check this out:(www.rit.ac.in)"])
            self.rep["title"] = "college website"
            self.rep["url"] = "www.rit.ac.in"
    def die(self,intent):
        if intent == 'die':
            self.rep["text"] = str(random.choice([1,2,3,4,5,6]))
    def coin(self,intent):
        if intent == 'coin':
            self.rep["text"] = random.choice(["head","tail"])