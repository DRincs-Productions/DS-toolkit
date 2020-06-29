init python:
    ## PartnerStats
    class PartnerStats():
        def __init__(self, love, lust, corruption, submission):
            self.favor = 0
            self.love = love
            self.lust = lust
            self.corruption = corruption
            self.submission = submission
            self.anger = 0
        def changeFavor(self, amt):
            if (self.anger > 0 and amt > 0):
                self.changeAnger(-2)
                return
            elif (self.favor == 0 and amt < 0):
                self.changeAnger(10)
                return
            elif (self.favor == 100 and amt > 0):
                return
            self.favor += amt
            if amt > 0:
                notify(increase_favor_notify)
            else:
                notify(decrease_favor_notify)
            if self.favor < 0:
                self.favor = 0
            elif self.favor > 100:
                self.favor = 100
        def changeLove(self, amt):
            if (self.anger > 0 and amt > 0):
                self.changeAnger(-10)
                return
            elif (self.love == -50 and amt < 0):
                self.changeAnger(40)
                return
            elif (self.love < 0 and amt < 0):
                self.changeAnger(20)
            elif (self.love == 100 and amt > 0):
                return
            self.love += amt
            if amt > 0:
                notify(increase_love_notify)
            else:
                notify(decrease_love_notify)
            if self.love < -50:
                self.love = -50
            elif self.love > 100:
                self.love = 100
        def changeCorruption(self, amt):
            if (self.corruption == -50 and amt < 0):
                self.changeAnger(-5)
                return
            elif (self.corruption == 100 and amt > 0):
                return
            self.corruption += amt
            if amt > 0:
                notify(increase_corruption_notify)
            else:
                notify(decrease_corruption_notify)
            if self.corruption < -50:
                self.corruption = -50
            elif self.corruption > 100:
                self.corruption = 100
        def changeLust(self, amt):
            if (self.lust == -100 and amt < 0):
                self.changeLove(-20)
                self.changeAnger(10)
                return
            elif (self.lust == 1000 and amt > 0):
                return
            self.lust += amt
            if amt > 0:
                notify(increase_lust_notify)
            else:
                notify(decrease_lust_notify)
            if self.lust < -100:
                self.lust = -100
            elif self.lust > 1000:
                self.lust = 1000
        def changeSubmission(self, amt):
            if (self.submission == -100 and amt < 0):
                self.changeCorruption(-20)
                self.changeAnger(10)
                return
            elif (self.submission == 1000 and amt > 0):
                return
            self.submission += amt
            if amt > 0:
                notify(increase_submission_notify)
            else:
                notify(decrease_submission_notify)
            if self.submission < -100:
                self.submission = -100
            elif self.submission > 1000:
                self.submission = 1000
        def changeAnger(self, amt):
            if (self.anger == 0 and amt < 0):
                return
            elif (self.anger == 100 and amt > 0):
                return
            self.anger += amt
            if amt > 0:
                notify(increase_anger_notify)
            else:
                notify(decrease_anger_notify)
            if self.anger < 0:
                self.anger = 0
            elif self.anger > 100:
                self.anger = 100
    ## Tendencies
    class Tendencies():
        def __init__(self, lesbo, addiction):
            self.lesbo = lesbo
            self.addiction = addiction
        def changeLesbo(self, amt):
            self.lesbo += amt
            if amt > 0:
                notify(increase_lesbo_notify)
            else:
                notify(decrease_lesbo_notify)
            if self.lesbo < 0:
                self.lesbo = 0
            elif self.lesbo > 100:
                self.lesbo = 100
        def is_lesbian(self):
            return self.friendship > 80
        def changeAddiction(self, amt):
            self.addiction += amt
            if amt > 0:
                notify(increase_addiction_notify)
            else:
                notify(decrease_addiction_notify)
            if self.addiction < 0:
                self.addiction = 0
            elif self.addiction > 100:
                self.addiction = 100
        def is_addicted_alcohol(self):
            return self.addiction > 30
        def is_addicted_soft_drugs(self):
            return self.addiction > 60
        def is_addicted_hard_drugs(self):
            return self.addiction > 90
    ## FriendStats
    class FriendStats():
        def __init__(self, friendship):
            self.friendship = friendship
        def change(self, amt):
            self.friendship += amt
            if amt > 0:
                notify(increase_friendship_notify)
            else:
                notify(decrease_friendship_notify)
            if self.friendship < -100:
                self.friendship = -100
            elif self.friendship > 100:
                self.friendship = 100
        def is_friend(self):
            return self.friendship > 0
