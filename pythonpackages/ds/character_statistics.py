from typing import Optional

from pythonpackages.renpy_custom_notify import NotifyEx, notify


class Statistic(object):
    """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic """

    def __init__(
        self,
        values: Optional[dict[str, int]] = None,
        notify_increase_dict: Optional[dict[str, NotifyEx]] = None,
        notify_decrease_dict: Optional[dict[str, NotifyEx]] = None,
        notify_dict: Optional[dict[str, NotifyEx]] = None,
        max_values: int = 100,
    ):
        self._memory = {}
        self.memory = values
        self._default_show_notify = False
        self.notify_increase_dict = notify_increase_dict
        self.notify_decrease_dict = notify_decrease_dict
        self.notify_dict = notify_dict
        self.max_values = max_values
        self._default_show_notify = True

    # Memory

    @property
    def memory(self) -> dict[str, int]:
        """Dictionary of all stats. Why a dictionary? Because it's easier to add new stats without editing the class code."""
        return self._memory if self._memory else {}

    @memory.setter
    def memory(self, value: Optional[dict[str, int]]) -> None:
        self._memory.update(value if value else {})

    def set(self, name: str, value: int) -> None:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic#set """
        # if (value != 0):
        self._memory[name] = value
        # else:
        #     self.remove(name)
        return

    def remove(self, name: str) -> None:
        """Delete the name value"""
        del self._memory[name]
        return

    def improve(self, name: str, amt: int = 1, max: Optional[int] = None, min: int = 0, show_notify: Optional[int] = None) -> None:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic#improvment """
        if show_notify == None:
            show_notify = self._default_show_notify
        if amt == 0:
            return
        if max == None:
            max = self.max_values
        cur_value = self.get(name)
        value = 0
        if isinstance(cur_value, int) and cur_value != 0:
            if amt > 0 and cur_value > max:
                return
            elif amt < 0 and cur_value < min:
                return
            else:
                value = cur_value + amt
        else:
            value = amt

        if (value >= max):
            self.set(name, max)
        elif (value <= min):
            self.set(name, min)
        else:
            self.set(name, value)

        if show_notify:
            self.notify(name=name, amt=amt)
        return

    def get(self, name: str, default_return: int = 0) -> int:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic#get """
        if name in self._memory:
            return self._memory[name]
        else:
            return default_return

    @property
    def max_values(self) -> int:
        """Default max value for all stats"""
        return self._max_values

    @max_values.setter
    def max_values(self, value: int) -> None:
        self._max_values = value

    @property
    def notify_increase_dict(self) -> dict[str, NotifyEx]:
        """Dictionary of notifications for when a stat increases"""
        return self._notify_increase_dict if self._notify_increase_dict else {}

    @notify_increase_dict.setter
    def notify_increase_dict(self, value: Optional[dict[str, NotifyEx]]) -> None:
        self._notify_increase_dict = value

    @property
    def notify_decrease_dict(self) -> dict[str, NotifyEx]:
        """Dictionary of notifications for when a stat decreases"""
        return self._notify_decrease_dict if self._notify_decrease_dict else {}

    @notify_decrease_dict.setter
    def notify_decrease_dict(self, value: Optional[dict[str, NotifyEx]]) -> None:
        self._notify_decrease_dict = value

    @property
    def notify_dict(self) -> dict[str, NotifyEx]:
        """Dictionary of notifications for when a stat changes"""
        return self._notify_dict if self._notify_dict else {}

    @notify_dict.setter
    def notify_dict(self, value: Optional[dict[str, NotifyEx]]) -> None:
        self._notify_dict = value

    def notify(self, name: str, amt: int) -> None:
        if amt < 0 and name in self.notify_decrease_dict:
            notify(self.notify_decrease_dict[name])
        elif amt > 0 and name in self.notify_increase_dict:
            notify(self.notify_increase_dict[name])
        elif name in self.notify_dict:
            notify(self.notify_dict[name])
        return

    def getAll(self):
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic#getAll """
        return self.memory

    def getDefaultMaxValue(self):
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic#getDefaultMaxValue """
        return self.max_values
