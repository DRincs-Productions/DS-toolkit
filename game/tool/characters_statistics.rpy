init python:
    ## PartnerStats
    class PartnerStats():
        def __init__(self, friendship, love, virgin, bisexual, polyamorous, against, addiction):
            self.friendship = friendship
            self.virgin = virgin
            self.bisexual = bisexual
            self.polyamorous = polyamorous
            # is a contradiction to a romantic relationship
            self.against = against
            self.energy = 100
            self.willpower = 100
            self.inhibition = 100
            self.favour = 0
            self.love = love
            self.lust = 0
            self.anger = 0
            self.fear = 0
            self.corruption = 0
            self.addiction = 0
        # Emblems
        def is_virgin(self):
            if (self.virgin == True or self.virgin == False):
                return self.virgin
            return self.virgin > 0
        def is_bisexual(self):
            if (self.bisexual == True or self.bisexual == False):
                return self.bisexual
            return self.bisexual > 10
        def is_polyamorous(self):
            if (self.polyamorous == True or self.polyamorous == False):
                return self.polyamorous
            return self.polyamorous > 10
        def is_against(self):
            if (self.against == True or self.against == False):
                return self.against
            return self.against <= 0
        def is_healthy(self):
            if (self.against != True and self.against != False and self.against > 0):
                return False
            if (self.is_slut() or self.is_submissive() or self.is_nymphomaniac() or self.is_celebrolesis() or self.is_free_use()):
                return False
            return (self.energy == 100 and self.willpower == 100 and self.inhibition == 100 and self.corruption == 0 and self.addiction == 0)
        def is_unfaithful(self):
            return (self.willpower > 45 and self.lust > 60 and self.anger > 50 and (self.lust + self.anger) > 130)
        def is_slut(self):
            return (self.lust > 50 and (self.corruption > 80 or self.addiction > 60) and (self.lust + self.corruption + self.addiction) > 160)
        def is_nymphomaniac(self):
            return (self.lust > 90 and self.corruption > 10 and self.inhibition < 40)
        def is_submissive(self):
            return (self.willpower < 20 and self.fear > 80 and (self.fear - self.willpower) > 80)
        def is_celebrolesis(self):
            return (self.inhibition < 20 and (self.willpower < 80 or self.addiction > 20) and (self.addiction - self.inhibition - self.willpower > 40))
        def is_free_use(self):
            return ((self.is_slut() and self.is_submissive()) or (self.is_slut() and self.is_celebrolesis()))
        # Relaction
        def is_friend(self):
            if (self.friendship == True or self.friendship == False):
                return self.friendship
            return self.friendship > 0
        def changeFriendship(self, amt):
            if (self.anger > 0 and amt > 0):
                self.changeAnger(-5)
                return
            self.friendship += amt
            if (amt > 0 and self.friendship <= 100):
                notify(increase_friendship_notify)
            elif (amt < 0 and self.friendship >= -100):
                notify(decrease_friendship_notify)
            if self.friendship < -100:
                self.friendship = -100
            elif self.friendship > 100:
                self.friendship = 100
        def changeFavour(self, amt):
            if (self.anger > 0 and amt > 0):
                self.changeAnger(-1)
                return
            self.favour += amt
            if (amt > 0 and self.favour <= 100):
                notify(increase_favour_notify)
            elif (amt < 0 and self.favour >= 0):
                notify(decrease_favour_notify)
            if self.favour >= 105:
                self.changeLove(1)
            if self.favour < 0:
                self.changeAnger(10)
                self.favour = 0
            elif self.favour > 100:
                self.favour = 100
        def changeLove(self, amt):
            if (self.anger > 0 and amt > 0):
                self.changeAnger(-5)
                return
            self.love += amt
            if (self.is_against() and self.love > 20):
                self.love = 20
                notify(against_notify)
                return
            if (self.fear > 40 and amt > 0):
                self.love -= amt
                notify(fear_against_notify)
                return
            if (amt > 0 and self.love <= 100):
                notify(increase_love_notify)
            elif (amt < 0 and self.love >= 0):
                notify(decrease_love_notify)
            if self.love >= 110:
                self.changeLust(1)
            if self.love < 0:
                self.changeAnger(10)
                self.love = 0
            elif self.love > 100:
                self.love = 100
        def changeCorruption(self, amt):
            self.corruption += amt
            if (amt > 0 and self.corruption <= 100):
                notify(increase_corruption_notify)
            elif (amt < 0 and self.corruption >= 0):
                notify(decrease_corruption_notify)
            if self.corruption >= 105:
                self.changeWillpower(-5)
            if self.corruption < 0:
                self.corruption = 0
            elif self.corruption > 100:
                self.corruption = 100
        def changeFear(self, amt):
            self.fear += amt
            if (amt > 0 and self.fear <= 100):
                notify(increase_fear_notify)
            elif (amt < 0 and self.fear >= 0):
                notify(decrease_fear_notify)
            if self.fear < 0:
                self.fear = 0
            elif self.fear > 100:
                self.fear = 100
        def changeAnger(self, amt):
            self.anger += amt
            if (amt > 0 and self.anger <= 100):
                notify(increase_anger_notify)
            elif (amt < 0 and self.anger >= 0):
                notify(decrease_anger_notify)
            if self.anger < 0:
                self.anger = 0
            elif self.anger > 100:
                self.anger = 100
        # Characteristics
        def changeEnergy(self, amt):
            self.energy += amt
            if (amt > 0 and self.energy <= 100):
                notify(increase_energy_notify)
            elif (amt < 0 and self.energy >= 0):
                notify(decrease_energy_notify)
            if self.energy < 0:
                self.energy = 0
            elif self.energy > 100:
                self.energy = 100
        def changeWillpower(self, amt):
            self.willpower += amt
            if (amt > 0 and self.willpower <= 100):
                notify(increase_willpower_notify)
            elif (amt < 0 and self.willpower >= 0):
                notify(decrease_willpower_notify)
            if self.willpower < 0:
                self.changeEnergy(-15)
                self.willpower = 0
            elif self.willpower > 100:
                self.willpower = 100
        def changeInhibition(self, amt):
            self.inhibition += amt
            if (amt > 0 and self.inhibition <= 100):
                notify(increase_inhibition_notify)
            elif (amt < 0 and self.inhibition >= 0):
                notify(decrease_inhibition_notify)
            if self.inhibition < 0:
                self.inhibition = 0
            elif self.inhibition > 100:
                self.inhibition = 100
        def changeAddiction(self, amt):
            self.addiction += amt
            if (amt > 0 and self.addiction <= 100):
                notify(increase_addiction_notify)
            elif (amt < 0 and self.addiction >= 0):
                notify(decrease_addiction_notify)
            if self.addiction >= 105:
                self.changeInhibition(-3)
            if self.addiction < 0:
                self.addiction = 0
            elif self.addiction > 100:
                self.addiction = 100
        def changeLust(self, amt):
            self.lust += amt
            if (amt > 0 and self.lust <= 100):
                notify(increase_lust_notify)
            elif (amt < 0 and self.lust >= 0):
                notify(decrease_lust_notify)
            if self.lust >= 120:
                self.changeInhibition(-5)
            if self.lust < 0:
                self.lust = 0
            elif self.lust > 100:
                self.lust = 100
