# scene 2
screen stop_torture():
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            textbutton "Прервать" action Jump("finish_scene_2")

# scene 3
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
            hovered [Play("sound", "audio/leha.mp3")]
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
            hovered [Play("sound", "audio/zekab.mp3")]
            action Jump("hide_zekab")

    showif zekac == 1:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.7
            focus_mask True
            idle "characters/Randoms/zekac_idle.png"
            hover "characters/Randoms/zekac_hover.png"
            hovered [Play("sound", "audio/zekac.mp3")]
            action Jump("hide_zekac")
            at customzoom

# scene 4

# Давайте поможем выбрать девушку Максиму! Как вы думаете, какая из них подходит больше всего?

screen choose_naumenko:
    showif sasha == 1:
        imagebutton:
            idle "characters/Randoms/sashanaumenko_idle.png"
            hover "characters/Randoms/sashanaumenko_idle.png"
            at sasha_open, customzoom
            action Jump("hide_sasha")

    showif ira == 1:
        imagebutton:
            idle "characters/Randoms/iranaumenko_idle.png"
            hover "characters/Randoms/iranaumenko_idle.png"
            at ira_open, customzoom
            action Jump("hide_ira")

    showif vika == 1:
        imagebutton:
            idle "characters/Randoms/vikanaumenko_idle.png"
            hover "characters/Randoms/vikanaumenko_idle.png"
            at vika_open, customzoom
            action Jump("hide_vika")

# scene 6

init python:

    result = {"Вику":0, "Шрека":0, "тусу":0}

    def char_dragged(drags, drop):

        if not drop:
            return

        char = drags[0].drag_name
        place = drop.drag_name

        result[char] = place
        if 0 not in result.values():
            return True

screen war_draft:
    # Группа drag гарантирует, что персонажей можно перетащить на места.
    draggroup:

        # Наши персонажи.
        drag:
            drag_name "Шрека"
            child "characters/dragndrop/shrek.png"
            droppable False
            dragged char_dragged
            xpos 100 ypos 100

        drag:
            drag_name "тусу"
            child "characters/dragndrop/party.png"
            droppable False
            dragged char_dragged
            xpos 300 ypos 200

        drag:
            drag_name "Вику"
            child "characters/dragndrop/vika.png"
            droppable False
            dragged char_dragged
            xpos 500 ypos 300

        # Места, куда можно направить персонажей.
        drag:
            drag_name "на болото"
            child "characters/dragndrop/swamp.png"
            draggable False
            xpos 600 ypos 100
        drag:
            drag_name "на хату Макара"
            draggable False
            child "characters/dragndrop/makarHouse.png"
            xpos 800 ypos 300
        drag:
            drag_name "нахуй"
            draggable False
            child "characters/dragndrop/fuckoff.png"
            xpos 1000 ypos 500
        drag:
            drag_name "в Красноярск"
            draggable False
            child "characters/dragndrop/kras.png"
            xpos 1200 ypos 600
