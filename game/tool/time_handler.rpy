init python:
    hour_names = ( (2, _("Night")),
                   (8, _("Morning")),
                   (14, _("Afternoon")),
                   (20, _("Evening")),
                 )
    weekday_names = ( _("{#weekday}Monday"),
                      _("{#weekday}Tuesday"),
                      _("{#weekday}Wednesday"),
                      _("{#weekday}Thursday"),
                      _("{#weekday}Friday"),
                      _("{#weekday}Saturday"),
                      _("{#weekday}Sunday")
                    )
    # month_names = ( ( _("November"), range(1,31)),
    #                 ( _("December"), range(1,32))
    #               )

    class TimeHandler(object):
        def __init__(self):
            self.hour_new_day = 8
            self.weekend_day = 6    # Saturday
            self.hour = self.hour_new_day
            self.day = 0

        def get_hour(self):
            hour = self.get_hour(hour)
            ret = "[hour]:00"
            return ret

        def get_hour_name(self):
            hour = self.hour
            for hour_name in hour_names:
                if hour < hour_name[0]:
                    break
                ret = hour_name[1]
            return ret

        def get_day_number(self):
            return self.day

        def get_weekday_number(self):
            return self.day % 7

        def get_weekday_name(self):
            return weekday_names[ self.get_weekday_number() ]

        # def get_day_of_month(self, hour=None):
        #     hour = self.get_hour(hour)
        #     day = self.get_day_number(hour) + 1
        #     for month in month_names:
        #         if day <= len(month[1]):
        #             break
        #         day -= len(month[1])
        #     return day

        # def get_month_name(self, hour=None):
        #     hour = self.get_hour(hour)
        #     return month_names[ self.get_month_number(hour) ][0]

        # def get_month_number(self, hour=None):
        #     hour = self.get_hour(hour)
        #     day = self.get_day_number(hour)
        #     # remember days start
        #     month_number = 0
        #     for month in month_names:
        #         if day < len(month[1]):
        #             break
        #         month_number += 1
        #         day -= len(month[1])
        #     return month_number

        def new_hour(self, amt):
            if (self.hour < hour_names[1][0]):
                return False
            self.hour += amt
            if (self.hour > 24):
                self.hour -= 24
            return True

        def new_day(self):
            self.hour = self.hour_new_day
            self.day += 1

        # def skip_weekend(self):

default time_handler = TimeHandler()
define event_duration = 6
default sky_time = 0
image sky = "check:images_tool/sky-[sky_time].webp"

label new_hour:
    if(time_handler.new_hour(event_duration)):
        if (time_handler.get_hour_name() == "Evening"):
            $ sky_time = 2
        elif (time_handler.get_hour_name() == "Night"):
            $ sky_time = 3
        elif (time_handler.get_hour_name() == "Morning"):
            $ sky_time = 0
        else:
            $ sky_time = 1
    else:
        "(It's late, you have to go to bed)"
    return

label new_day:
    $ time_handler.new_day()
    $ sky_time = 0
    call check_event
    return

label check_event:
    return
