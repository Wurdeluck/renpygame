label scene_1:

    s "Ага, поверил. Ну и бредятина."

    play sound "audio/flush.wav"

    scene bg swamp_scene_1

    show shrek happy with zoomin:
        zoom 1.5

    play music "audio/somebody.mp3" volume 0.7 loop

    s "Ух вот это я чилю конечно"

    s "Планирую чилить тут как следует"

    "И он чилил изо всех сил"

    transform bigzoomfromleft:
        zoom 1 alpha 1 xalign 0.0
        linear 4.0 zoom 2 alpha 0 xalign 1.0

    transform bigzoomfromright:
        zoom 1 alpha 1 xalign 1.0
        linear 4.0 zoom 2 alpha 0 xalign 0.0

    transform bigzoomfrombottom:
        zoom 1.0 xalign 0.5 yalign 1
        linear 4.0 zoom 2 xalign 0.5 yalign 0.3

    show shrek shock at bigzoomfromleft

    "Вот тут он играет в дотку с братанами"

    show shrek smug at bigzoomfromright

    "А тут дует сладкий колюмбасик ммм двойное яблоко "

    hide shrek

    show shrek happy at bigzoomfrombottom

    "Играет на гитаре музыкант талант красавчик одним словом"

    menu break_chill:
        "Желаете прервать чилл Максима?"
        "Да":
            stop music fadeout 5.0
            hide shrek
            hide bg
            show black
            "Максим мирно спал и не догадывался, что его ждет дальше, в между
            тем история начала стремительно развиваться"
            return
        "Нет":
            "Так и закончилась его история. Максим ни о чем не жалел и умер
            счастливым."
            hide shrek
            show text "КОНЦОВКА: МНЕ И ТАК ЗАЕБОК" at truecenter
            with dissolve
            pause 1
            hide text
            with dissolve
            jump break_chill
    return
