label scene_1:

    s "Ага, поверил. Ну и бредятина."

    play sound "audio/flush.wav"

    scene background_scene_1

    show shrek happy with zoomin:
        zoom 1.5

    play music "audio/scene_1_somebody.mp3" volume 0.5 loop

    s "Ух вот это я чилю конечно"

    s "Планирую чилить тут как следует"

    n "И он чилил изо всех сил"

    show shrek dota at bigzoomfromleft

    n "Вот тут он играет в дотку с братанами"

    show shrek hookah at bigzoomfromright

    n "А тут дует сладкий колюмбасик ммм двойное яблоко"

    hide shrek

    show shrek guitar at bigzoomfrombottom

    n "Играет на гитаре музыкант талант красавчик одним словом"

    menu break_chill:
        "Желаете прервать чилл Максима?"
        "Да":
            stop music fadeout 4.0
            hide shrek
            hide bg
            show black
            n "Максим мирно спал и не догадывался, что его ждет дальше, а между
            тем история начала стремительно развиваться."
            return
        "Нет":
            n "Так и закончилась его история. Максим ни о чем не жалел и умер
            счастливым."
            hide shrek guitar
            show black
            show end zaebok at truecenter
            with dissolve
            pause 3
            hide end zaebok
            hide black
            show shrek dota:
                xalign 1.2
                yalign 0.4
                rotate 30
            with dissolve
            jump break_chill
    return
