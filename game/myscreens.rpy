# scene 2
screen stop_torture():
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            textbutton "Прервать" action Jump("finish_scene_2")

# scene 3
screen croud():
    showif leha == 1:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.835
            ypos 0.2
            focus_mask True
            auto "characters/Randoms/leha_%s.png"
            hovered [Play("sound", "audio/leha.mp3")]
            action Jump("hide_leha")

    showif zekab == 1:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.9
            ypos 0.5
            focus_mask True
            at zekabzoom
            auto "characters/Randoms/zekab_%s.png"
            hovered [Play("sound", "audio/zekab.mp3")]
            action Jump("hide_zekab")

    showif zekac == 1:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.85
            ypos 0.5
            focus_mask True
            auto "characters/Randoms/zekac_%s.png"
            hovered [Play("sound", "audio/zekac.mp3")]
            action Jump("hide_zekac")
            at customzoom

# scene 4

# Давайте поможем выбрать девушку Максиму! Как вы думаете, какая из них подходит больше всего?

screen choose_naumenko():
    showif sasha == 1:
        imagebutton:
            auto "characters/Randoms/sashanaumenko_%s.png"
            hovered [Play("sound", "audio/sasha.mp3")]
            at sasha_open, customzoom
            action Jump("hide_sasha")

    showif ira == 1:
        imagebutton:
            auto "characters/Randoms/iranaumenko_%s.png"
            hovered [Play("sound", "audio/ira.mp3")]
            at ira_open, customzoom
            action Jump("hide_ira")

    showif vika == 1:
        imagebutton:
            auto "characters/Randoms/vikanaumenko_%s.png"
            hovered [Play("sound", "audio/vika.mp3")]
            at vika_open, customzoom
            action Jump("hide_vika")

# scene 6

init python:

    result = {"Вику":0, "Шрека":0, "тусу":0}

    def char_dragged(drags, drop):

        char = drags[0].drag_name

        if not drop:
            result[char] = 0
            return

        place = drop.drag_name
        result[char] = place
        if 0 not in result.values():
            return True

screen war_draft():

    imagebutton:
        idle im.FactorScale("images/characters/dragndrop/swamp.png", 0.2)
        action Null()
        hovered [Play("sound", "audio/swamp.mp3")]
        xpos 600 ypos 200


    imagebutton:
        idle im.FactorScale("characters/dragndrop/makarHouse.png", 1.0)
        action Null()
        hovered [Play("sound", "audio/makar_house.mp3")]
        xpos 900 ypos 300

    imagebutton:
        idle im.FactorScale("characters/dragndrop/fuckoff.jpg", 0.5)
        action Null()
        hovered [Play("sound", "audio/fuckoff.mp3")]
        xpos 1200 ypos 200

    imagebutton:
        idle im.FactorScale("characters/dragndrop/kras.png", 1.0)
        action Null()
        hovered [Play("sound", "audio/kras.mp3")]
        xpos 1400 ypos 200

    # Группа drag гарантирует, что персонажей можно перетащить на места.
    draggroup:

        # Наши персонажи.
        drag:
            drag_name "Шрека"
            child im.FactorScale("characters/dragndrop/shrek.png", 0.4)
            hovered [Play("sound", "audio/shrek.mp3")]
            droppable False
            dragged char_dragged
            xpos 800 ypos 600

        drag:
            drag_name "тусу"
            child im.FactorScale("characters/dragndrop/party.png", 0.2)
            hovered [Play("sound", "audio/party.mp3")]
            droppable False
            dragged char_dragged
            xpos 950 ypos 600

        drag:
            drag_name "Вику"
            child im.FactorScale("characters/dragndrop/vika.png", 0.2)
            hovered [Play("sound", "audio/vikaname.mp3")]
            droppable False
            dragged char_dragged
            xpos 1200 ypos 600

        # Места, куда можно направить персонажей.
        drag:
            drag_name "на болото"
            child im.FactorScale("characters/dragndrop/swamp.png", 0.3)
            draggable False
            xpos 600 ypos 200
        drag:
            drag_name "на хату Макара"
            child im.FactorScale("characters/dragndrop/makarHouse.png", 1.0)
            draggable False
            xpos 900 ypos 300
        drag:
            drag_name "нахуй"
            child im.FactorScale("characters/dragndrop/fuckoff.jpg", 0.5)
            draggable False
            xpos 1200 ypos 200
        drag:
            drag_name "в Красноярск"
            child im.FactorScale("characters/dragndrop/kras.png", 1.0)
            draggable False
            xpos 1400 ypos 200
