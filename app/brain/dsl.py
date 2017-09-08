import random
class dsl(object):
    def __init__(self,intent,messege):
        self.rep = {}
        self.rep["text"]="none"
        self.toss(intent,messege)
        self.open(intent,messege)
        self.contact(intent,messege)
        self.location(intent,messege)
        self.who_or_what(intent,messege)

    def generate(self):
        return self.rep["text"]
    def open(self,intent,messege):
        open_key = [('RIT','www.rit.ac.in'),('creative team','www.ritcreativeteam.ml'),('tinkerhub-RIT','www.ritcreativeteam.ml')]
        if intent == "open":
            for key in open_key:
                if key[0] in messege:
                    self.rep["text"] = random.choice(["check this out:","here you go:","I found this:"])+key[1]
    def who_or_what(self, intent,messege):
             who_key = [('principal','i dont know her name but she is cool'),('tinkerhub','A community for learning 21st century techs'),('rit creative team','check out this website: www.ritcreativeteam.ml'),('RIT','Rajiv Gandhi Institute of tech, best engineering college in kerala !')]
             if intent == "who_or_what":
                 for key in who_key:
                     if key[0] in messege:
                         self.rep["text"]= key[1]
    def toss(self, intent, messege):
        toss_key = [('coin','co'),('die','di'),('dice','di')]
        if intent == "toss":
            for key in toss_key:
                if key[0] in messege:
                    if key[1] == "co":
                        self.rep["text"] = random.choice(['head','tails'])
                    elif key[1] == "di":
                        self.rep["text"] = str(random.choice([1,2,3,4,5,6]))

    def contact(self,intent,messege):
        contact_key = [('principal','principal_number'),('authorities','office_number'),('office','office_number')]
        if intent == "contact":
            for key in contact_key:
                if key[0] in messege:
                    self.rep["text"] = key[1]
    def location(self,intent,messege):
        location_key = [('principal','princi_loc'),('RIT','college_loc'),('CS department','cs_loc')]
        if intent == "location":
            for key in location_key:
                if key[0] in messege:
                    self.rep["text"] = key[1]
