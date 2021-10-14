# scene 1

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
