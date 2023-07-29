init python:
    bg_color_1 = "#aaffff"
    bg_color_2 = "#ffaaff"
    bg_color_c = bg_color_1

    def callback1(event, interact=True, **kwargs):
        if event == "begin":
            renpy.sound.play("audio/poing.wav")

    def callback2(event, interact=True, **kwargs):
        global bg_color_1, bg_color_2, bg_color_c
        if event == "slow_done":
            if bg_color_c == bg_color_1:
                bg_color_c = bg_color_2
            else:
                bg_color_c = bg_color_1

    def dyn_display(st, at, *args, **kwargs):
        global bg_color_c
        return (Solid(bg_color_c), 0.1)

image bg = DynamicDisplayable(dyn_display)
image ch:
    "default"
    zoom 0.75
    yoffset 200

define e = Character("Blair", callback=CallbackList(callback1, callback2))

label start:

    $ preferences.text_cps = 50

    scene bg
    show ch

    e "This is some dialogue."

    e "A sound plays when the dialogue starts."

    e "The background color changes when the dialogue ends."

    e "Pretty neat, huh?"

    return
