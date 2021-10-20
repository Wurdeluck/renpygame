# scene 1

transform shrekzoom:
    zoom 2.0

transform bigzoomfromleft:
    zoom 1 alpha 1 xalign 0.0
    # linear 3.0 alpha 0 xalign 0.9 yalign 0.4 rotate 30
    linear 4.0 zoom 2 alpha 0 xalign 1.0

transform bigzoomfromright:
    zoom 1 alpha 1 xalign 1.0
    linear 4.0 zoom 2 alpha 0 xalign 0.0

transform bigzoomfrombottom:
    zoom 1.0 xalign 0.5 yalign 1
    linear 4.0 zoom 2 xalign 0.5 yalign 0.3

# scene 3
transform customzoom:
    zoom 0.3

transform forward_spin:
    subpixel True
    rotate 0
    linear 1.0 rotate 360
    repeat

transform popierdolilo:
    linear 1.0 xzoom 0.25 yzoom 1.5 xalign 0.1

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat


# scene 4
transform shake:
        ease .06 yoffset 24
        ease .06 yoffset -24
        ease .05 yoffset 20
        ease .05 yoffset -20
        ease .04 yoffset 16
        ease .04 yoffset -16
        ease .03 yoffset 12
        ease .03 yoffset -12
        ease .02 yoffset 8
        ease .02 yoffset -8
        ease .01 yoffset 4
        ease .01 yoffset -4
        ease .01 yoffset 0
        repeat

transform mirrorzoom:
    zoom 2.5

# scene 5

transform bedzoom:
    zoom 1.5

transform sasha_open:
    on hover:
        xalign 0.2 yalign 0.5
        linear 0.4 xalign 0.2 yalign 0.3
    on idle:
        xalign 0.2 yalign 0.3
        linear 0.4 xalign 0.2 yalign 0.5

transform ira_open:
    on hover:
        xalign 0.5 yalign 0.5
        linear 0.4 xalign 0.5 yalign 0.3
    on idle:
        xalign 0.5 yalign 0.3
        linear 0.4 xalign 0.5 yalign 0.5

transform vika_open:
    on hover:
        xalign 0.8 yalign 0.5
        linear 0.4 xalign 0.8 yalign 0.3
    on idle:
        xalign 0.8 yalign 0.3
        linear 0.4 xalign 0.8 yalign 0.5

transform customopacity:
    alpha 0.5

# scene_8

transform kriszoom:
    zoom 2.0


transform moving_around:
    parallel:
        linear randtime1() xalign 0.0
        linear randtime1() xalign 1.0
        repeat
    parallel:
        linear randtime2() yalign 0.0
        linear randtime2() yalign 1.0
        repeat

init python:
    import random

    def randx():
        return random.uniform(0, 1)

    def randy():
        return random.uniform(0, 1)

    def randtime1():
        return random.gauss(1.5, 0.5)

    def randtime2():
        return random.gauss(1.5, 0.5)
