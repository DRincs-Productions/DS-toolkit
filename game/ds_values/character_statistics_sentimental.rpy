init python:
    from typing import Union

    from pythonpackages.ds.character_statistics import Statistic
    from pythonpackages.renpy_utility.renpy_custom_notify import NotifyEx, notify

    against_notify = NotifyEx(
        message=__("Is against a love affair with you"),
        image="/images_tool/icon/notification/emblems-against.webp",
    )
    fear_against_notify = NotifyEx(
        message=__("Has too much fear of you for a love affair"),
        image="/images_tool/icon/notification/relations-fear.webp",
    )
    # Characteristics
    increase_energy_notify = NotifyEx(
        message=__("{color=#00ff00}{b}+{/b} Energy{/color}"),
        image="/images_tool/icon/notification/characteristics-energy.webp",
    )
    decrease_energy_notify = NotifyEx(
        message=__("{color=#f00} {b}-{/b} Energy{/color}"),
        image="/images_tool/icon/notification/characteristics-energy.webp",
    )
    increase_willpower_notify = NotifyEx(
        message=__("{color=#00ff00}{b}+{/b} Willpower{/color}"),
        image="/images_tool/icon/notification/characteristics-willpower.webp",
    )
    decrease_willpower_notify = NotifyEx(
        message=__("{color=#f00} {b}-{/b} Willpower{/color}"),
        image="/images_tool/icon/notification/characteristics-willpower.webp",
    )
    increase_inhibition_notify = NotifyEx(
        message=__("{color=#f00}{b}+{/b} Inhibition{/color}"),
        image="/images_tool/icon/notification/characteristics-inhibition.webp",
    )
    decrease_inhibition_notify = NotifyEx(
        message=__("{color=#00ff00} {b}-{/b} Inhibition{/color}"),
        image="/images_tool/icon/notification/characteristics-inhibition.webp",
    )
    increase_addiction_notify = NotifyEx(
        message=__("{color=#00ff00}{b}+{/b} Addictions{/color}"),
        image="/images_tool/icon/notification/characteristics-addiction.webp",
    )
    decrease_addiction_notify = NotifyEx(
        message=__("{color=#f00} {b}-{/b} Addictions{/color}"),
        image="/images_tool/icon/notification/characteristics-addiction.webp",
    )
    increase_lust_notify = NotifyEx(
        message=__("{color=#00ff00}{b}+{/b} Lust{/color}"),
        image="/images_tool/icon/notification/characteristics-lust.webp",
    )
    decrease_lust_notify = NotifyEx(
        message=__("{color=#f00} {b}-{/b} Lust{/color}"),
        image="/images_tool/icon/notification/characteristics-lust.webp",
    )
    # Relations
    increase_friendship_notify = NotifyEx(
        message=__("{color=#00ff00}{b}+{/b} Friendship{/color}"),
        image="/images_tool/icon/notification/relations-friendship.webp",
    )
    decrease_friendship_notify = NotifyEx(
        message=__("{color=#f00} {b}-{/b} Friendship{/color}"),
        image="/images_tool/icon/notification/relations-friendship.webp",
    )
    increase_favour_notify = NotifyEx(
        message=__("{color=#00ff00}{b}+{/b} Favour{/color}"),
        image="/images_tool/icon/notification/relations-favour.webp",
    )
    decrease_favour_notify = NotifyEx(
        message=__("{color=#f00} {b}-{/b} Favour{/color}"),
        image="/images_tool/icon/notification/relations-favour.webp",
    )
    increase_love_notify = NotifyEx(
        message=__("{color=#00ff00}{b}+{/b} Love{/color}"),
        image="/images_tool/icon/notification/relations-love.webp",
    )
    decrease_love_notify = NotifyEx(
        message=__("{color=#f00} {b}-{/b} Love{/color}"),
        image="/images_tool/icon/notification/relations-love.webp",
    )
    increase_corruption_notify = NotifyEx(
        message=__("{color=#00ff00}{b}+{/b} Corruption{/color}"),
        image="/images_tool/icon/notification/relations-corruption.webp",
    )
    decrease_corruption_notify = NotifyEx(
        message=__("{color=#f00} {b}-{/b} Corruption{/color}"),
        image="/images_tool/icon/notification/relations-corruption.webp",
    )
    increase_anger_notify = NotifyEx(
        message=__("{color=#f00}{b}+{/b} Anger{/color}"),
        image="/images_tool/icon/notification/relations-anger.webp",
    )
    decrease_anger_notify = NotifyEx(
        message=__("{color=#00ff00} {b}-{/b} Anger{/color}"),
        image="/images_tool/icon/notification/relations-anger.webp",
    )
    increase_fear_notify = NotifyEx(
        message=__("{color=#f00}{b}+{/b} Fear{/color}"),
        image="/images_tool/icon/notification/relations-fear.webp",
    )
    decrease_fear_notify = NotifyEx(
        message=__("{color=#00ff00} {b}-{/b} Fear{/color}"),
        image="/images_tool/icon/notification/relations-fear.webp",
    )

    class SentimentalStatistic(Statistic):
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic#sentimental-statistic """

        def __init__(
            self,
            friendship: int = 0,
            favour: int = 0,
            love: int = 0,
            corruption: int = 0,
            virgin: bool = True,
            bisexual: bool = False,
            against=0,
            addiction=0,
            max_values: int = 100,
        ):

            # Statistic init
            super().__init__(
                notify_increase_dict={
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
                },
                notify_decrease_dict={
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
                },
                max_values=max_values,
            )

            # SentimentalStatistic init
            self._default_show_notify = False

            # is a contradiction to a romantic relationship
            self.against = against
            # Characteristics
            self.addiction = addiction
            # Relaction
            self.friendship = friendship
            self.favour = favour
            self.love = love
            self.corruption = corruption
            # Emblems
            self.is_virgin = virgin
            self.bisexual = bisexual

            self._default_show_notify = True

        # Friendship
        @property
        def friendship(self) -> int:
            return self.get("friendship")

        @friendship.setter
        def friendship(self, value: int) -> None:
            cur_value = self.get("friendship")
            amt = value - cur_value
            if (self.anger > 0 and amt > 0):
                self.anger = self.anger - 5
                return
            self.improve("friendship", amt, max=100, min=-100)
            return

        @property
        def is_friend(self) -> bool:
            return self.friendship > 0

        # Favour
        @property
        def favour(self) -> int:
            return self.get("favour")

        @favour.setter
        def favour(self, value: int) -> None:
            cur_value = self.get("favour")
            amt = value - cur_value
            if (self.anger is int and self.anger > 0 and amt > 0):
                self.anger = self.anger - 1
                return
            if (cur_value + amt) >= 105:
                self.love = self.love + 1
            if (cur_value + amt) < 0:
                self.anger = self.anger + 10
            self.improve("favour", amt, max=100, min=0)
            return

        # Love
        @property
        def love(self) -> int:
            return self.get("love")

        @love.setter
        def love(self, value: int) -> None:
            cur_value = self.get("love")
            amt = value - cur_value
            if (self.anger is int and self.anger > 0 and amt > 0):
                self.anger = self.anger - 5
                return
            if (self.is_against and (cur_value + amt) > 20):
                self.set("love", 20)
                notify(against_notify)
                return
            if (self.fear + amt) > 40 and amt > 0:
                self.improve("love", -amt, max=100, min=0)
                notify(fear_against_notify)
                return
            if (cur_value + amt) >= 110:
                self.lust = self.lust + 1
            self.improve("love", amt, max=100, min=0)
            return

        # Corruption
        @property
        def corruption(self) -> int:
            return self.get("corruption")

        @corruption.setter
        def corruption(self, value: int) -> None:
            cur_value = self.get("corruption")
            amt = value - cur_value
            if (cur_value + amt) >= 105:
                self.willpower = self.willpower - 5
            self.improve("corruption", amt, max=100, min=0)
            return

        # Fear
        @property
        def fear(self) -> int:
            return self.get("fear")

        @fear.setter
        def fear(self, value: int) -> None:
            cur_value = self.get("fear")
            amt = value - cur_value
            self.improve("fear", amt, max=100, min=0)
            return

        # Anger
        @property
        def anger(self) -> int:
            return self.get("anger")

        @anger.setter
        def anger(self, value: int) -> None:
            cur_value = self.get("anger")
            amt = value - cur_value
            self.improve("anger", amt, max=100, min=0)
            return

        # Energy
        @property
        def energy(self) -> int:
            return self.get("energy")

        @energy.setter
        def energy(self, value: int) -> None:
            cur_value = self.get("energy")
            amt = value - cur_value
            self.improve("energy", amt, max=100, min=0)
            return

        # Willpower
        @property
        def willpower(self) -> int:
            return self.get("willpower")

        @willpower.setter
        def willpower(self, value: int) -> None:
            cur_value = self.get("willpower")
            amt = value - cur_value
            if (cur_value + amt) < 0:
                self.energy = self.energy - 15
            self.improve("willpower", amt, max=100, min=0)
            return

        # Inhibition
        @property
        def inhibition(self) -> int:
            return self.get("inhibition")

        @inhibition.setter
        def inhibition(self, value: int) -> None:
            cur_value = self.get("inhibition")
            amt = value - cur_value
            self.improve("inhibition", amt, max=100, min=0)
            return

        # Addiction
        @property
        def addiction(self) -> int:
            return self.get("addiction")

        @addiction.setter
        def addiction(self, value: int) -> None:
            cur_value = self.get("addiction")
            amt = value - cur_value
            if (cur_value + amt) >= 105:
                self.inhibition = self.inhibition - 3
            self.improve("addiction", amt, max=100, min=0)
            return

        # Lust
        @property
        def lust(self) -> int:
            return self.get("lust")

        @lust.setter
        def lust(self, value: int) -> None:
            cur_value = self.get("lust")
            amt = value - cur_value
            if (cur_value + amt) >= 120:
                self.inhibition = self.inhibition - 5
            self.improve("lust", amt, max=100, min=0)
            return

        # Against
        @property
        def against(self) -> int:
            return self.get("against")

        @against.setter
        def against(self, value: int) -> None:
            cur_value = self.get("lust")
            amt = value - cur_value
            self.improve("against", amt, max=100, min=0)
            return

        @property
        def is_against(self) -> bool:
            val = self.get("against")
            if val == None:
                return False
            return val <= 0

        @is_against.setter
        def is_against(self, value: bool):
            """Set the virginity of the character."""
            if value:
                self.against = 0
            else:
                self.against = 100

        # Other

        @property
        def is_virgin(self) -> bool:
            """Return True if the character is a virgin, False otherwise."""
            val = self.get("sex_actions")
            return val <= 0

        @is_virgin.setter
        def is_virgin(self, value: Union[bool, int]):
            """Set the virginity of the character."""
            if isinstance(value, bool):
                if value:
                    self.set("sex_actions", 0)
                else:
                    self.improve("sex_actions", 1)
            else:
                self.set("sex_actions", value)

        @property
        def is_healthy(self) -> bool:
            if (not self.is_against):
                return False
            if (self.is_slut or self.is_submissive or self.is_nymphomaniac or self.is_celebrolesis or self.is_free_use):
                return False
            return (self.energy == 100 and self.willpower == 100 and self.inhibition == 100 and self.corruption == 0 and self.addiction == 0)

        @is_healthy.setter
        def is_healthy(self, value: bool):
            if value:
                self.energy += 100
                self.willpower += 100
                self.inhibition += 100
                self.corruption -= 100
                self.addiction -= 100
                self.fear -= 50
                self.lust -= 50
                self.is_against = False
            else:
                self.energy -= 100
                self.willpower -= 100
                self.inhibition -= 100
                self.corruption += 100
                self.addiction += 100

        @property
        def is_unfaithful(self) -> bool:
            return (self.willpower > 45 and self.lust > 60 and self.anger > 50 and (self.lust + self.anger) > 130)

        @is_unfaithful.setter
        def is_unfaithful(self, value: bool):
            if value:
                self.willpower += 100
                self.lust += 100
                self.anger += 100
            else:
                self.willpower -= 100
                self.lust -= 100
                self.anger -= 100

        @property
        def is_slut(self) -> bool:
            return (self.lust > 50 and (self.corruption > 80 or self.addiction > 60) and (self.lust + self.corruption + self.addiction) > 160)

        @is_slut.setter
        def is_slut(self, value: bool):
            if value:
                self.lust += 100
                self.corruption += 100
                self.addiction += 100
            else:
                self.lust -= 100
                self.corruption -= 100
                self.addiction -= 100

        @property
        def is_nymphomaniac(self) -> bool:
            return (self.lust > 90 and self.corruption > 10 and self.inhibition < 40)

        @is_nymphomaniac.setter
        def is_nymphomaniac(self, value: bool):
            if value:
                self.corruption += 100
                self.lust += 100
                self.inhibition -= 100
            else:
                self.corruption -= 100
                self.lust -= 100
                self.inhibition += 100

        @property
        def is_submissive(self) -> bool:
            return (self.willpower < 20 and self.fear > 80 and (self.fear - self.willpower) > 80)

        @is_submissive.setter
        def is_submissive(self, value: bool):
            if value:
                self.willpower -= 100
                self.fear += 100
            else:
                self.willpower += 100
                self.fear -= 100

        @property
        def is_celebrolesis(self) -> bool:
            return (self.inhibition < 20 and (self.willpower < 80 or self.addiction > 20) and (self.addiction - self.inhibition - self.willpower > 40))

        @is_celebrolesis.setter
        def is_celebrolesis(self, value: bool):
            if value:
                self.willpower -= 100
                self.inhibition -= 100
                self.addiction += 100
            else:
                self.willpower += 100
                self.inhibition += 100
                self.addiction -= 100

        @property
        def is_free_use(self) -> bool:
            return ((self.is_slut and self.is_submissive) or (self.is_slut and self.is_celebrolesis))

        @is_free_use.setter
        def is_free_use(self, value: bool):
            if value:
                self.willpower -= 100
                self.inhibition -= 100
                self.fear += 100
                self.lust += 100
                self.corruption += 100
                self.addiction += 100
            else:
                self.willpower += 100
                self.inhibition += 100
                self.fear -= 100
                self.lust -= 100
                self.corruption -= 100
                self.addiction -= 100
