init 9 python:
    from typing import Optional

    class Statistic(object):
        """Manages the relationship of possible patners. Using the dictionaries has in memory only the variables to use, I recommend changing the slo values with set(), change(), get()I suggest to customize this function."""

        def __init__(
            self,
            values: Optional[dict[str, int]] = None,
            notify_increase_dict: Optional[dict[str]] = None,
            notify_decrease_dict: Optional[dict[str]] = None,
            notify_dict: Optional[dict[str, NotifyEx]] = None,
        ):

            self.memory = {}
            self.memory.update(values if values else {})
            self.notify_increase_dict = notify_increase_dict if notify_increase_dict else {}
            self.notify_decrease_dict = notify_decrease_dict if notify_decrease_dict else {}
            self.notify_dict = notify_dict if notify_dict else {}

        def set(self, name: str, value: int):
            """Function to set or add a new value"""
            if (name != None and name != ""):
                self.memory[name] = value
            else:
                self.remove(name)

        def remove(self, name: str):
            """Delete the name value"""
            del self.memory[name]

        def change(self, name: str, amt: int, max: int = 100, min: int = 0, show_notify: bool = True):
            """Changes a value, if it does not exist adds it"""
            if (self.get(name) != None):
                if (amt > 0 and self.memory[name] >= max):
                    return
                elif (amt < 0 and self.memory[name] <= min):
                    return
                self.memory[name] += amt
                if self.memory[name] < min:
                    self.memory[name] = min
                elif self.memory[name] > max:
                    self.memory[name] = max
            else:
                if (amt is int and amt >= max):
                    self.set(name, max)
                    return
                elif (amt is int and amt <= min):
                    self.set(name, min)
                    return
                self.set(name, amt)
            if show_notify:
                self.notify(name, amt)
            return

        def get(self, name):
            """Returns the value "name", in case it does not exist returns None"""
            if name in self.memory:
                return self.memory[name]
            else:
                return None

        def improve(self, name: str, amt: int = 1):
            self.change(name, amt, max=10, min=0)

        def notify(self, name: str, amt: int):
            if amt < 0 and name in self.notify_decrease_dict:
                notify(self.notify_decrease_dict[name])
            elif amt > 0 and name in self.notify_increase_dict:
                notify(self.notify_increase_dict[name])
            elif name in self.notify_dict:
                notify(self.notify_dict[name])
            return


init 10 python:
    against_notify = NotifyEx(msg=__("Is against a love affair with you"),
                            img="/images_tool/icon/notification/emblems-against.webp")
    fear_against_notify = NotifyEx(msg=__("Has too much fear of you for a love affair"),
                                img="/images_tool/icon/notification/relations-fear.webp")
    # Characteristics
    increase_energy_notify = NotifyEx(msg=__(
        "{color=#00ff00}{b}+{/b} Energy{/color}"), img="/images_tool/icon/notification/characteristics-energy.webp")
    decrease_energy_notify = NotifyEx(msg=__(
        "{color=#f00} {b}-{/b} Energy{/color}"), img="/images_tool/icon/notification/characteristics-energy.webp")
    increase_willpower_notify = NotifyEx(msg=__(
        "{color=#00ff00}{b}+{/b} Willpower{/color}"), img="/images_tool/icon/notification/characteristics-willpower.webp")
    decrease_willpower_notify = NotifyEx(msg=__(
        "{color=#f00} {b}-{/b} Willpower{/color}"), img="/images_tool/icon/notification/characteristics-willpower.webp")
    increase_inhibition_notify = NotifyEx(msg=__(
        "{color=#f00}{b}+{/b} Inhibition{/color}"), img="/images_tool/icon/notification/characteristics-inhibition.webp")
    decrease_inhibition_notify = NotifyEx(msg=__(
        "{color=#00ff00} {b}-{/b} Inhibition{/color}"), img="/images_tool/icon/notification/characteristics-inhibition.webp")
    increase_addiction_notify = NotifyEx(msg=__(
        "{color=#00ff00}{b}+{/b} Addictions{/color}"), img="/images_tool/icon/notification/characteristics-addiction.webp")
    decrease_addiction_notify = NotifyEx(msg=__(
        "{color=#f00} {b}-{/b} Addictions{/color}"), img="/images_tool/icon/notification/characteristics-addiction.webp")
    increase_lust_notify = NotifyEx(msg=__(
        "{color=#00ff00}{b}+{/b} Lust{/color}"), img="/images_tool/icon/notification/characteristics-lust.webp")
    decrease_lust_notify = NotifyEx(msg=__(
        "{color=#f00} {b}-{/b} Lust{/color}"), img="/images_tool/icon/notification/characteristics-lust.webp")
    # Relations
    increase_friendship_notify = NotifyEx(msg=__(
        "{color=#00ff00}{b}+{/b} Friendship{/color}"), img="/images_tool/icon/notification/relations-friendship.webp")
    decrease_friendship_notify = NotifyEx(msg=__(
        "{color=#f00} {b}-{/b} Friendship{/color}"), img="/images_tool/icon/notification/relations-friendship.webp")
    increase_favour_notify = NotifyEx(msg=__(
        "{color=#00ff00}{b}+{/b} Favour{/color}"), img="/images_tool/icon/notification/relations-favour.webp")
    decrease_favour_notify = NotifyEx(msg=__(
        "{color=#f00} {b}-{/b} Favour{/color}"), img="/images_tool/icon/notification/relations-favour.webp")
    increase_love_notify = NotifyEx(msg=__(
        "{color=#00ff00}{b}+{/b} Love{/color}"), img="/images_tool/icon/notification/relations-love.webp")
    decrease_love_notify = NotifyEx(msg=__(
        "{color=#f00} {b}-{/b} Love{/color}"), img="/images_tool/icon/notification/relations-love.webp")
    increase_corruption_notify = NotifyEx(msg=__(
        "{color=#00ff00}{b}+{/b} Corruption{/color}"), img="/images_tool/icon/notification/relations-corruption.webp")
    decrease_corruption_notify = NotifyEx(msg=__(
        "{color=#f00} {b}-{/b} Corruption{/color}"), img="/images_tool/icon/notification/relations-corruption.webp")
    increase_anger_notify = NotifyEx(msg=__(
        "{color=#f00}{b}+{/b} Anger{/color}"), img="/images_tool/icon/notification/relations-anger.webp")
    decrease_anger_notify = NotifyEx(msg=__(
        "{color=#00ff00} {b}-{/b} Anger{/color}"), img="/images_tool/icon/notification/relations-anger.webp")
    increase_fear_notify = NotifyEx(msg=__(
        "{color=#f00}{b}+{/b} Fear{/color}"), img="/images_tool/icon/notification/relations-fear.webp")
    decrease_fear_notify = NotifyEx(msg=__(
        "{color=#00ff00} {b}-{/b} Fear{/color}"), img="/images_tool/icon/notification/relations-fear.webp")


    class SentimentalStatistic(Statistic):
        """Manages the relationship of possible patners. Using the dictionaries has in memory only the variables to use, I recommend changing the slo values with set(), change(), get()I suggest to customize this function."""

        def __init__(
            self,
            gender_attracted: str,  # ["F", "M"],
            friendship: int = 0,
            favour: int = 0,
            love: int = 0,
            corruption: int = 0,
            virgin: bool = True,
            bisexual: bool = False,
            polyamorous: bool = False,
            against=None,
            addiction=None
        ):

            self.memory = {}
            # Characteristics
            if (gender_attracted != None):
                self.change(name="gender_attracted",
                            amt=gender_attracted, show_notify=False)
            else:
                self.setHeterosexual()
            # is a contradiction to a romantic relationship
            if (against != None):
                self.change(name="against",  amt=against, show_notify=False)
            # Characteristics
            self.change(name="energy",  amt=0, show_notify=False)
            self.change(name="willpower",  amt=0, show_notify=False)
            self.change(name="inhibition",  amt=0, show_notify=False)
            if (addiction != None):
                self.change(name="addiction",  amt=addiction, show_notify=False)
            # Relaction
            if (friendship != None):
                self.change(name="friendship",  amt=friendship, show_notify=False)
            if (favour != None):
                self.change(name="favour",  amt=favour, show_notify=False)
            if (love != None):
                self.change(name="love",  amt=love, show_notify=False)
            if (corruption != None):
                self.change(name="corruption",  amt=corruption, show_notify=False)
            # Emblems
            if (virgin != None):
                self.change(name="virgin",  amt=virgin, show_notify=False)
            if (bisexual != None):
                self.change(name="bisexual",  amt=bisexual, show_notify=False)
            if (polyamorous != None):
                self.change(name="polyamorous",
                            amt=polyamorous, show_notify=False)

            self.notify_increase_dict = {
                "energy": increase_energy_notify,
                "willpower": increase_willpower_notify,
                "inhibition": increase_inhibition_notify,
                "addiction": increase_addiction_notify,
                "lust": increase_lust_notify,
                "friendship": increase_friendship_notify,
                "favour": increase_favour_notify,
                "love": increase_love_notify,
                "corruption": increase_corruption_notify,
                "anger": increase_anger_notify,
                "fear": increase_fear_notify,
            }
            self.notify_decrease_dict = {
                "energy": decrease_energy_notify,
                "willpower": decrease_willpower_notify,
                "inhibition": decrease_inhibition_notify,
                "addiction": decrease_addiction_notify,
                "lust": decrease_lust_notify,
                "friendship": decrease_friendship_notify,
                "favour": decrease_favour_notify,
                "love": decrease_love_notify,
                "corruption": decrease_corruption_notify,
                "anger": decrease_anger_notify,
                "fear": decrease_fear_notify,
            }
            self.notify = {}

        def setHeterosexual(self):
            """Knowing the denere of the gender_attracted sect character hetero"""
            if self.get("gender") == "F":
                self.set("gender_attracted", "M")
            else:
                self.set("gender_attracted", "F")

        # Emblems

        def isVirgin(self):
            val = self.get("virgin")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val > 0

        def isBisexual(self):
            val = self.get("bisexual")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val > 10

        def isPolyamorous(self):
            val = self.get("polyamorous")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val > 10

        def isAgainst(self):
            val = self.get("against")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val <= 0

        def isHealthy(self):
            if (self.get("against") != True and self.get("against") != False and self.get("against") > 0):  # TODO: TO CHANGE
                return False
            if (self.isSlut() or self.isSubmissive() or self.isNymphomaniac() or self.isCelebrolesis() or self.isFreeUse()):
                return False
            return (self.get("energy") == 100 and self.get("willpower") == 100 and self.get("inhibition") == 100 and self.get("corruption") == 0 and self.get("addiction") == 0)

        def isUnfaithful(self):
            return (self.get("willpower") > 45 and self.get("lust") > 60 and self.get("anger") > 50 and (self.get("lust") + self.get("anger")) > 130)

        def isSlut(self):
            return (self.get("lust") > 50 and (self.get("corruption") > 80 or self.get("addiction") > 60) and (self.get("lust") + self.get("corruption") + self.get("addiction")) > 160)

        def isNymphomaniac(self):
            return (self.get("lust") > 90 and self.get("corruption") > 10 and self.get("inhibition") < 40)

        def isSubmissive(self):
            return (self.get("willpower") < 20 and self.get("fear") > 80 and (self.get("fear") - self.get("willpower")) > 80)

        def isCelebrolesis(self):
            return (self.get("inhibition") < 20 and (self.get("willpower") < 80 or self.get("addiction") > 20) and (self.get("addiction") - self.get("inhibition") - self.get("willpower") > 40))

        def isFreeUse(self):
            return ((self.isSlut() and self.isSubmissive()) or (self.isSlut() and self.isCelebrolesis()))
        # Relaction

        def isFriend(self):
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
            if self.get("love") != None and (self.isAgainst() and (self.get("love") + amt) > 20):
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
