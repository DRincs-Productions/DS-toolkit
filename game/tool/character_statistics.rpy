init 9 python:
    from typing import Optional

    class Statistic(object):
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic """

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

        def set(self, name: str, value: int) -> None:
            """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic#set """
            if (name != None and name != ""):
                self.memory[name] = value
            else:
                self.remove(name)
            return

        def remove(self, name: str) -> None:
            """Delete the name value"""
            del self.memory[name]
            return

        def improve(self, name: str, amt: int = 1, max=100, min=0, show_notify= True) -> None:
            """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic#improvment """
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
                self.notify(name = name,amt= amt)
            return

        def get(self, name):
            """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Statistic#get """
            if name in self.memory:
                return self.memory[name]
            else:
                return None

        def notify(self, name: str, amt: int) -> None:
            if amt < 0 and name in self.notify_decrease_dict:
                notify(self.notify_decrease_dict[name])
            elif amt > 0 and name in self.notify_increase_dict:
                notify(self.notify_increase_dict[name])
            elif name in self.notify_dict:
                notify(self.notify_dict[name])
            return
