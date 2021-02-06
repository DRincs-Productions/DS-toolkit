init python:
    class Statistics():
        """Manages the relationship of possible patners. Using the dictionaries has in memory only the variables to use, I recommend changing the slo values with set(), change(), get()I suggest to customize this function."""
        def __init__(self,
            gender = "F",
            gender_attracted = None,
            friendship = None,
            favour = None,
            love = None,
            corruption = None,
            virgin = None,
            bisexual = None,
            polyamorous = None,
            against = None,
            addiction = None,
            other_values = {}):

            self.memory = {}
            self.memory.update(other_values)
            # Characteristics
            if (gender != None):
                self.memory["gender"] = gender
            if (gender_attracted != None):
                self.memory["gender_attracted"] = gender_attracted
            else:
                self.setHeterosexual()
            # is a contradiction to a romantic relationship
            if (against != None):
                self.memory["against"] = against
            # Characteristics
            self.memory["energy"] = 100
            self.memory["willpower"] = 100
            self.memory["inhibition"] = 100
            if (addiction != None):
                self.memory["addiction"] = addiction
            # Relaction
            if (friendship != None):
                self.memory["friendship"] = friendship
            if (favour != None):
                self.memory["favour"] = favour
            if (love != None):
                self.memory["love"] = love
            if (corruption != None):
                self.memory["corruption"] = corruption
            # Emblems
            if (virgin != None):
                self.memory["virgin"] = virgin
            if (bisexual != None):
                self.memory["bisexual"] = bisexual
            if (polyamorous != None):
                self.memory["polyamorous"] = polyamorous

        def setHeterosexual(self):
            """Knowing the denere of the gender_attracted sect character hetero"""
            if self.get("gender") == "F":
                self.set("gender_attracted", "M")
            else:
                self.set("gender_attracted", "F")
        def set(self, text, value):
            """Function to set or add a new value"""
            if (text != None and text != ""):
                self.memory[text] = value
            else:
                remove(text)
        def remove(self, text):
            """Delete the text value"""
            del memory[text]
        def change(self, text, amt, max=100, min=0):
            """Changes a value, if it does not exist adds it"""
            if (self.get(text) != None):
                if (amt > 0 and self.memory[text] >= max):
                    return
                elif (amt < 0 and self.memory[text] <= min):
                    return
                self.memory[text] += amt
                if self.memory[text] < min:
                    self.memory[text] = min
                elif self.memory[text] > max:
                    self.memory[text] = max
            else:
                if (amt >= max):
                    self.set(text, max)
                    return
                elif (amt <= min):
                    self.set(text, min)
                    return
                self.set(text, amt)
            self.notify(text, amt)
        def get(self, text):
            """Returns the value "text", in case it does not exist returns None"""
            if text in self.memory:
                return self.memory[text]
            else:
                return None
        def notify(self, text, amt):
            """To customize"""
            if (text == "energy"):
                if (amt > 0):
                    notify(increase_energy_notify)
                elif (amt < 0):
                    notify(decrease_energy_notify)
            elif (text == "willpower"):
                if (amt > 0):
                    notify(increase_willpower_notify)
                elif (amt < 0):
                    notify(decrease_willpower_notify)
            elif (text == "inhibition"):
                if (amt > 0):
                    notify(increase_inhibition_notify)
                elif (amt < 0):
                    notify(decrease_inhibition_notify)
            elif (text == "addiction"):
                if (amt > 0):
                    notify(increase_addiction_notify)
                elif (amt < 0):
                    notify(decrease_addiction_notify)
            elif (text == "lust"):
                if (amt > 0):
                    notify(increase_lust_notify)
                elif (amt < 0):
                    notify(decrease_lust_notify)
            elif (text == "friendship"):
                if (amt > 0):
                    notify(increase_friendship_notify)
                elif (amt < 0):
                    notify(decrease_friendship_notify)
            elif (text == "favour"):
                if (amt > 0):
                    notify(increase_favour_notify)
                elif (amt < 0):
                    notify(decrease_favour_notify)
            elif (text == "love"):
                if (amt > 0):
                    notify(increase_love_notify)
                elif (amt < 0):
                    notify(decrease_love_notify)
            elif (text == "corruption"):
                if (amt > 0):
                    notify(increase_corruption_notify)
                elif (amt < 0):
                    notify(decrease_corruption_notify)
            elif (text == "anger"):
                if (amt > 0):
                    notify(increase_anger_notify)
                elif (amt < 0):
                    notify(decrease_anger_notify)
            elif (text == "fear"):
                if (amt > 0):
                    notify(increase_fear_notify)
                elif (amt < 0):
                    notify(decrease_fear_notify)
        # Additional functions:
        def improve_ability(self, text, amt=1):
            self.change(text, amt, max=10, min=0)
        # Emblems
        def is_virgin(self):
            val = self.get("virgin")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val > 0
        def is_bisexual(self):
            val = self.get("bisexual")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val > 10
        def is_polyamorous(self):
            val = self.get("polyamorous")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val > 10
        def is_against(self):
            val = self.get("against")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val <= 0
        def is_healthy(self):
            if (self.get("against") != True and self.get("against") != False and self.get("against") > 0): # TODO: TO CHANGE
                return False
            if (self.is_slut() or self.is_submissive() or self.is_nymphomaniac() or self.is_celebrolesis() or self.is_free_use()):
                return False
            return (self.get("energy") == 100 and self.get("willpower") == 100 and self.get("inhibition") == 100 and self.get("corruption") == 0 and self.get("addiction") == 0)
        def is_unfaithful(self):
            return (self.get("willpower") > 45 and self.get("lust") > 60 and self.get("anger") > 50 and (self.get("lust") + self.get("anger")) > 130)
        def is_slut(self):
            return (self.get("lust") > 50 and (self.get("corruption") > 80 or self.get("addiction") > 60) and (self.get("lust") + self.get("corruption") + self.get("addiction")) > 160)
        def is_nymphomaniac(self):
            return (self.get("lust") > 90 and self.get("corruption") > 10 and self.get("inhibition") < 40)
        def is_submissive(self):
            return (self.get("willpower") < 20 and self.get("fear") > 80 and (self.get("fear") - self.get("willpower")) > 80)
        def is_celebrolesis(self):
            return (self.get("inhibition") < 20 and (self.get("willpower") < 80 or self.get("addiction") > 20) and (self.get("addiction") - self.get("inhibition") - self.get("willpower") > 40))
        def is_free_use(self):
            return ((self.is_slut() and self.is_submissive()) or (self.is_slut() and self.is_celebrolesis()))
        # Relaction
        def is_friend(self):
            val = self.get("friendship")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val > 0
        def changeFriendship(self, amt):
            if (self.get("anger") > 0 and amt > 0):
                self.changeAnger(-5)
                return
            self.change("friendship", amt, max=100, min=-100)
        def changeFavour(self, amt):
            if (self.get("anger") > 0 and amt > 0):
                self.changeAnger(-1)
                return
            if self.get("favour") != None and (self.get("favour") + amt) >= 105:
                self.changeLove(1)
            if self.get("favour") != None and (self.get("favour") + amt) < 0:
                self.changeAnger(10)
            self.change("favour", amt, max=100, min=0)
        def changeLove(self, amt):
            if (self.get("anger") > 0 and amt > 0):
                self.changeAnger(-5)
                return
            if self.get("love") != None and (self.is_against() and (self.get("love") + amt) > 20):
                self.set("love", 20)
                notify(against_notify)
                return
            if self.get("fear") != None and ((self.get("fear") + amt) > 40 and amt > 0):
                self.change("love", -amt, max=100, min=0)
                notify(fear_against_notify)
                return
            if self.get("love") != None and (self.get("love") + amt) >= 110:
                self.changeLust(1)
            self.change("love", amt, max=100, min=0)
        def changeCorruption(self, amt):
            if self.get("corruption") != None and (self.get("corruption") + amt) >= 105:
                self.changeWillpower(-5)
            self.change("corruption", amt, max=100, min=0)
        def changeFear(self, amt):
            self.change("fear", amt, max=100, min=0)
        def changeAnger(self, amt):
            self.change("anger", amt, max=100, min=0)
        # Characteristics
        def changeEnergy(self, amt):
            self.change("energy", amt, max=100, min=0)
        def changeWillpower(self, amt):
            if self.get("willpower") != None and (self.get("willpower") + amt) < 0:
                self.changeEnergy(-15)
            self.change("willpower", amt, max=100, min=0)
        def changeInhibition(self, amt):
            self.change("inhibition", amt, max=100, min=0)
        def changeAddiction(self, amt):
            if self.get("addiction") != None and (self.get("addiction") + amt) >= 105:
                self.changeInhibition(-3)
            self.change("addiction", amt, max=100, min=0)
        def changeLust(self, amt):
            if self.get("lust") != None and (self.get("lust") + amt) >= 120:
                self.changeInhibition(-5)
            self.change("lust", amt, max=100, min=0)
