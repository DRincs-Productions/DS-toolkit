init 10 python:
    from pythonpackages.renpy_custom_notify import NotifyEx
    from pythonpackages.ds.character_statistics import Statistic

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
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic#sentimental-statistic """

        def __init__(
            self,
            gender_attracted: GENDER_TYPE,
            friendship: int = 0,
            favour: int = 0,
            love: int = 0,
            corruption: int = 0,
            virgin: bool = True,
            bisexual: bool = False,
            polyamorous: bool = False,
            against=None,
            addiction=None,
            max_values: int = 100,
        ):

            self.memory = {}
            self.max_values = max_values
            # Characteristics
            if (gender_attracted != None):
                self.improve(name="gender_attracted",
                            amt=gender_attracted, show_notify=False)
            else:
                self.setHeterosexual()
            # is a contradiction to a romantic relationship
            if (against != None):
                self.improve(name="against",  amt=against, show_notify=False)
            # Characteristics
            self.improve(name="energy",  amt=0, show_notify=False)
            self.improve(name="willpower",  amt=0, show_notify=False)
            self.improve(name="inhibition",  amt=0, show_notify=False)
            if (addiction != None):
                self.improve(name="addiction",  amt=addiction, show_notify=False)
            # Relaction
            if (friendship != None):
                self.improve(name="friendship",  amt=friendship, show_notify=False)
            if (favour != None):
                self.improve(name="favour",  amt=favour, show_notify=False)
            if (love != None):
                self.improve(name="love",  amt=love, show_notify=False)
            if (corruption != None):
                self.improve(name="corruption",  amt=corruption, show_notify=False)
            # Emblems
            if (virgin != None):
                self.improve(name="virgin",  amt=virgin, show_notify=False)
            if (bisexual != None):
                self.improve(name="bisexual",  amt=bisexual, show_notify=False)
            if (polyamorous != None):
                self.improve(name="polyamorous",
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
            self.notify_dict = {}

        def setHeterosexual(self) -> None:
            """Knowing the denere of the gender_attracted sect character hetero"""
            if self.get("gender") == "F":
                self.set("gender_attracted", "M")
            else:
                self.set("gender_attracted", "F")
            return


        # Emblems
        def isVirgin(self) -> bool:
            val = self.get("virgin")
            if val == None:
                return True
            elif val is bool:
                return val
            elif val is int:
                return val > 0
            return True

        def isBisexual(self) -> bool:
            val = self.get("bisexual")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val > 10

        def isPolyamorous(self) -> bool:
            val = self.get("polyamorous")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val > 10

        def isAgainst(self) -> bool:
            val = self.get("against")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val <= 0

        def isHealthy(self) -> bool:
            if (self.get("against") and self.get("against") != True and self.get("against") != False and self.get("against", 0) > 0):  # TODO: TO improve
                return False
            if (self.isSlut() or self.isSubmissive() or self.isNymphomaniac() or self.isCelebrolesis() or self.isFreeUse()):
                return False
            return (self.get("energy", 0) == 100 and self.get("willpower", 0) == 100 and self.get("inhibition", 0) == 100 and self.get("corruption", 0) == 0 and self.get("addiction", 0) == 0)

        def isUnfaithful(self) -> bool:
            return (self.get("willpower", 0) > 45 and self.get("lust", 0) > 60 and self.get("anger", 0) > 50 and (self.get("lust", 0) + self.get("anger", 0)) > 130)

        def isSlut(self) -> bool:
            return (self.get("lust", 0) > 50 and (self.get("corruption", 0) > 80 or self.get("addiction", 0) > 60) and (self.get("lust", 0) + self.get("corruption", 0) + self.get("addiction", 0)) > 160)

        def isNymphomaniac(self) -> bool:
            return (self.get("lust", 0) > 90 and self.get("corruption", 0) > 10 and self.get("inhibition", 0) < 40)

        def isSubmissive(self) -> bool:
            return (self.get("willpower", 0) < 20 and self.get("fear", 0) > 80 and (self.get("fear", 0) - self.get("willpower", 0)) > 80)

        def isCelebrolesis(self) -> bool:
            return (self.get("inhibition", 0) < 20 and (self.get("willpower", 0) < 80 or self.get("addiction", 0) > 20) and (self.get("addiction", 0) - self.get("inhibition", 0) - self.get("willpower", 0) > 40))

        def isFreeUse(self) -> bool:
            return ((self.isSlut() and self.isSubmissive()) or (self.isSlut() and self.isCelebrolesis()))


        # Relaction
        def isFriend(self) -> bool:
            val = self.get("friendship")
            if val == None:
                return False
            if (val == True or val == False):
                return val
            return val > 0

        def improveFriendship(self, amt) -> None:
            valAnger = self.get("anger")
            if (valAnger is int and valAnger > 0 and amt > 0):
                self.improveAnger(-5)
                return
            self.improve("friendship", amt, max=100, min=-100)
            del valAnger
            return

        def improveFavour(self, amt) -> None:
            valAnger = self.get("anger")
            if (valAnger is int and valAnger > 0 and amt > 0):
                self.improveAnger(-1)
                return
            if self.get("favour") is int and (self.get("favour") + amt) >= 105:
                self.improveLove(1)
            if self.get("favour") is int and (self.get("favour") + amt) < 0:
                self.improveAnger(10)
            self.improve("favour", amt, max=100, min=0)
            del valAnger
            return

        def improveLove(self, amt) -> None:
            valAnger = self.get("anger")
            if (valAnger is int and valAnger > 0 and amt > 0):
                self.improveAnger(-5)
                return
            if self.get("love") != None and (self.isAgainst() and (self.get("love") + amt) > 20):
                self.set("love", 20)
                notify(against_notify)
                return
            if self.get("fear") != None and ((self.get("fear") + amt) > 40 and amt > 0):
                self.improve("love", -amt, max=100, min=0)
                notify(fear_against_notify)
                return
            if self.get("love") != None and (self.get("love") + amt) >= 110:
                self.improveLust(1)
            self.improve("love", amt, max=100, min=0)
            return

        def improveCorruption(self, amt) -> None:
            if self.get("corruption") != None and (self.get("corruption") + amt) >= 105:
                self.improveWillpower(-5)
            self.improve("corruption", amt, max=100, min=0)
            return

        def improveFear(self, amt) -> None:
            self.improve("fear", amt, max=100, min=0)
            return

        def improveAnger(self, amt) -> None:
            self.improve("anger", amt, max=100, min=0)
            return


        # Characteristics
        def improveEnergy(self, amt) -> None:
            self.improve("energy", amt, max=100, min=0)
            return

        def improveWillpower(self, amt) -> None:
            if self.get("willpower") != None and (self.get("willpower") + amt) < 0:
                self.improveEnergy(-15)
            self.improve("willpower", amt, max=100, min=0)
            return

        def improveInhibition(self, amt) -> None:
            self.improve("inhibition", amt, max=100, min=0)
            return

        def improveAddiction(self, amt) -> None:
            if self.get("addiction") != None and (self.get("addiction") + amt) >= 105:
                self.improveInhibition(-3)
            self.improve("addiction", amt, max=100, min=0)
            return

        def improveLust(self, amt) -> None:
            if self.get("lust") != None and (self.get("lust") + amt) >= 120:
                self.improveInhibition(-5)
            self.improve("lust", amt, max=100, min=0)
            return
