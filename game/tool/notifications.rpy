default against_notify = NotifyEx(msg="Is against a love affair with you", img="/images_tool/icon/notification/emblems-against.webp")
default fear_against_notify = NotifyEx(msg="Has too much fear of you for a love affair", img="/images_tool/icon/notification/relations-fear.webp")
# Characteristics
default increase_energy_notify = NotifyEx(msg="{color=#00ff00}{b}+{/b} Energy", img="/images_tool/icon/notification/characteristics-energy.webp")
default decrease_energy_notify = NotifyEx(msg="{color=#f00} {b}-{/b} Energy", img="/images_tool/icon/notification/characteristics-energy.webp")
default increase_willpower_notify = NotifyEx(msg="{color=#00ff00}{b}+{/b} Willpower", img="/images_tool/icon/notification/characteristics-willpower.webp")
default decrease_willpower_notify = NotifyEx(msg="{color=#f00} {b}-{/b} Willpower", img="/images_tool/icon/notification/characteristics-willpower.webp")
default increase_inhibition_notify = NotifyEx(msg="{color=#f00}{b}+{/b} Inhibition", img="/images_tool/icon/notification/characteristics-inhibition.webp")
default decrease_inhibition_notify = NotifyEx(msg="{color=#00ff00} {b}-{/b} Inhibition", img="/images_tool/icon/notification/characteristics-inhibition.webp")
default increase_addiction_notify = NotifyEx(msg="{color=#00ff00}{b}+{/b} Addictions", img="/images_tool/icon/notification/characteristics-addiction.webp")
default decrease_addiction_notify = NotifyEx(msg="{color=#f00} {b}-{/b} Addictions", img="/images_tool/icon/notification/characteristics-addiction.webp")
default increase_lust_notify = NotifyEx(msg="{color=#00ff00}{b}+{/b} Lust", img="/images_tool/icon/notification/characteristics-lust.webp")
default decrease_lust_notify = NotifyEx(msg="{color=#f00} {b}-{/b} Lust", img="/images_tool/icon/notification/characteristics-lust.webp")
# Relations
default increase_favour_notify = NotifyEx(msg="{color=#00ff00}{b}+{/b} Favour", img="/images_tool/icon/notification/relations-favour.webp")
default decrease_favour_notify = NotifyEx(msg="{color=#f00} {b}-{/b} Favour", img="/images_tool/icon/notification/relations-favour.webp")
default increase_love_notify = NotifyEx(msg="{color=#00ff00}{b}+{/b} Love", img="/images_tool/icon/notification/relations-love.webp")
default decrease_love_notify = NotifyEx(msg="{color=#f00} {b}-{/b} Love", img="/images_tool/icon/notification/relations-love.webp")
default increase_corruption_notify = NotifyEx(msg="{color=#00ff00}{b}+{/b} Corruption", img="/images_tool/icon/notification/relations-corruption.webp")
default decrease_corruption_notify = NotifyEx(msg="{color=#f00} {b}-{/b} Corruption", img="/images_tool/icon/notification/relations-corruption.webp")
default increase_anger_notify = NotifyEx(msg="{color=#f00}{b}+{/b} Anger", img="/images_tool/icon/notification/relations-anger.webp")
default decrease_anger_notify = NotifyEx(msg="{color=#00ff00} {b}-{/b} Anger", img="/images_tool/icon/notification/relations-anger.webp")
default increase_friendship_notify = NotifyEx(msg="{color=#00ff00}{b}+{/b} Friendship", img="/images_tool/icon/notification/relations-friendship.webp")
default decrease_friendship_notify = NotifyEx(msg="{color=#f00} {b}-{/b} Friendship", img="/images_tool/icon/notification/relations-friendship.webp")
default increase_fear_notify = NotifyEx(msg="{color=#f00}{b}+{/b} Fear", img="/images_tool/icon/notification/relations-fear.webp")
default decrease_fear_notify = NotifyEx(msg="{color=#00ff00} {b}-{/b} Fear", img="/images_tool/icon/notification/relations-fear.webp")

init python:
    ## Notifications
    # to use: default ... = NotifyEx(msg="...", img="...")
    class NotifyEx( renpy.python.RevertableObject ):
        def __init__( self, msg, img ):
            super(NotifyEx, self).__init__()
            self.msg = msg
            self.img = img
            self.remain = gui.notifyEx_delay
    ## view undefined notifications
    # to use: $ notifyEx(msg="...")
    # to use: $ notifyEx(msg="...", img="...")
    # to use: $ notifyEx(img="...")
    def notifyEx( msg=None, img=None ):
        notifications.append( NotifyEx( msg, img ) )
        if len( store.notifications ) == 1: renpy.show_screen( "notifyEx" )
    def notifyExClean( value ):
        if value in store.notifications: store.notifications.remove( value )
        if len( store.notifications ) == 0: renpy.hide_screen( "notifyEx" )
    ## view defined notifications
    # to use: $ notify(...)
    def notify( n ):
        notifications.append( NotifyEx( n.msg, n.img ) )
        if len( store.notifications ) == 1: renpy.show_screen( "notifyEx" )

# Delay of visibility of a notification.
define gui.notifyEx_delay = 10.0
# Width of the images.
define gui.notifyEx_width = 64
# Height of the images.
define gui.notifyEx_height = 64

default notifications = []

style notify_text is default:
    # color "#49aae6"
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
