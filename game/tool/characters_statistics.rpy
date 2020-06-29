init python:
    ## GirlStats
    class GirlStats():
        def __init__(self, love, lust, corruption, submission, anger, limbo, lesbo, addiction):
            self.love = love
            self.lust = lust
            self.corruption = corruption
            self.submission = submission
            self.anger = anger
            self.limbo = limbo
            self.lesbo = lesbo
            self.addiction = addiction
        def changeLove(self, amt):
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
            self.corruption += amt
            if amt > 0:
                notify(increase_corruption_notify)
            else:
                notify(decrease_corruption_notify)
            if self.corruption < 0:
                self.corruption = 0
            elif self.corruption > 100:
                self.corruption = 100
        def changeLust(self, amt):
            self.lust += amt
            if amt > 0:
                notify(increase_lust_notify)
            else:
                notify(decrease_lust_notify)
        def changeSubmission(self, amt):
            self.submission += amt
            if amt > 0:
                notify(increase_submission_notify)
            else:
                notify(decrease_submission_notify)
        def changeAnger(self, amt):
            self.anger += amt
            if amt > 0:
                notify(increase_anger_notify)
            else:
                notify(decrease_anger_notify)
            if self.anger < 0:
                self.anger = 0
            elif self.anger > 100:
                self.anger = 100
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
