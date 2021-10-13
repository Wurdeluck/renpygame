screen stop_torture():
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            textbutton "Прервать" action Jump("finish_scene_2")


screen croud:
    showif leha == 1:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.7
            ypos 0.28
            focus_mask True
            idle "characters/Randoms/leha_idle.png"
            hover "characters/Randoms/leha_hover.png"
            action Jump("hide_leha")

    showif zekab == 1:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.8
            ypos 0.38
            focus_mask True
            idle "characters/Randoms/zekab_idle.png"
            hover "characters/Randoms/zekab_hover.png"
            hovered [Play("sound", "audio/doorbell.wav")]
            action Jump("hide_zekab")
