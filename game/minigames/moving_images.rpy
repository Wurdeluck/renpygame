transform move_slide:
    linear 2.0 xalign 0.0 yalign 0.5
    linear 2.0 xalign 1.0 yalign 0.5
    repeat

init python:
    renpy.music.register_channel ("ch_one", "sfx", False)

screen game_rangedweapon:

    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "images/characters/Randoms/robinhood_%s.png"
        action [Play("ch_one", "audio/minecraft_oof.mp3"), Jump("winning")] at move_slide, customzoom


    $ count = [x for x in range(30)]

    for item in enumerate(count):
        imagebutton:
            xalign 0.5
            yalign 0.5
            auto "images/characters/Randoms/luda_%s.jpg"
            action Play("ch_one", "audio/roblox_oof.mp3") at moving_around, customzoom

label winning:
    d "Ура! Теперь начнется настоящая битва!"

    v "Да какая битва, ему одного удара хватило."

    return

label failure:
    d "Неет, это "

    return
