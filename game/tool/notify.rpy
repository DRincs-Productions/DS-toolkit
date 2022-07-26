init python:
    class NotifyEx(renpy.python.RevertableObject):
        """Notifications, to use: default ... = NotifyEx(msg="...", img="...")"""
        def __init__(self,
                    msg: str,
                    img: str
                    ):
            super(NotifyEx, self).__init__()
            self.msg = msg
            self.img = img
            self.remain = gui.notifyEx_delay


    def notifyEx(msg: str = None, img: str = None):
        notifications.append(NotifyEx(msg, img))
        if len(store.notifications) == 1:
            renpy.show_screen("notifyEx")


    def notifyExClean(value):
        if value in store.notifications:
            store.notifications.remove(value)
        if len(store.notifications) == 0:
            renpy.hide_screen("notifyEx")


    def notify(notific):
        """View defined notifications.
        to use: $ notify(...)"""
        notifications.append(NotifyEx(notific.msg, notific.img))
        if len(store.notifications) == 1:
            renpy.show_screen("notifyEx")

# Delay of visibility of a notification.
define gui.notifyEx_delay = 10.0
# Width of the images.
define gui.notifyEx_width = 64
# Height of the images.
define gui.notifyEx_height = 64

define gui.notifyEx_color = "#000000"

default notifications = []

style notify_text is default:
    color gui.notifyEx_color
    yalign 0.5

style notify_hbox is default:
    ysize gui.notifyEx_height

screen notifyEx():

    zorder 100

    style_prefix "notify"

    vbox:
        for d in notifications:
            use notifyExInternal( d )
            # aerate a little.
            null height 5

screen notifyExInternal( n ):

    style_prefix "notify"

    frame at notify_appear:
        hbox:
            if not n.img is None:
                add n.img
            else:
                # Ensure that all the texts will be aligned.
                null width gui.notifyEx_width

            # aerate a little.
            null width 5

            if not n.msg is None:
                text n.msg

    timer 0.05 repeat True action [ SetField( n, "remain", n.remain - 0.05 ), If( n.remain <= 0, Function( notifyExClean, n ), NullAction() ) ]
