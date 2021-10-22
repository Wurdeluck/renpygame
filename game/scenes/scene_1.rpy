label scene_1:

    s "Ага, поверил. Ну и бредятина."

    play sound "audio/flush.wav"

    scene background_scene_1

    show shrek happy with zoomin:
        zoom 1.5

    play music "audio/scene_1_somebody.mp3" volume 0.5 loop

    s "Ух вот это я чилю конечно"

    s "Планирую чилить тут как следует"

    "{i}И он чилил изо всех сил{/i}"

    show shrek dota at bigzoomfromleft

    "{i}Вот тут он играет в дотку с братанами{/i}"

    show shrek hookah at bigzoomfromright

    "{i}А тут дует сладкий колюмбасик ммм двойное яблоко{/i}"

    hide shrek

    show shrek guitar at bigzoomfrombottom

    "{i}Играет на гитаре музыкант талант красавчик одним словом{/i}"

    menu break_chill:
        "Желаете прервать чилл Максима?"
        "Да":
            stop music fadeout 4.0
            hide shrek
            hide bg
            show black
            "{i}Максим мирно спал и не догадывался, что его ждет дальше, а между
            тем история начала стремительно развиваться{/i}"
            return
        "Нет":
            "{i}Так и закончилась его история. Максим ни о чем не жалел и умер
            счастливым.{/i}"
            hide shrek guitar
            show text "КОНЦОВКА: МНЕ И ТАК ЗАЕБОК" at truecenter
            with dissolve
            pause 1
            hide text
            show shrek dota:
                xalign 1.2
                yalign 0.4
                rotate 30
            with dissolve
            jump break_chill
    return
