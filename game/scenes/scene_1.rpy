label scene_1:

    s "Ага, поверил. Ну и бредятина."

    play sound "audio/flush.wav"

    image background_scene_1:
      zoom 1.5
      "images/backgrounds/bg swamp_scene_1_alter.jpg"

    scene background_scene_1

    show shrek happy with zoomin:
        zoom 1.5

    play music "audio/somebody.mp3" volume 0.7 loop

    s "Ух вот это я чилю конечно"

    s "Планирую чилить тут как следует"

    "И он чилил изо всех сил"

    show shrek dota at bigzoomfromleft

    "Вот тут он играет в дотку с братанами"

    show shrek hookah at bigzoomfromright

    "А тут дует сладкий колюмбасик ммм двойное яблоко "

    hide shrek

    show shrek guitar at bigzoomfrombottom

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
            show shrek dota:
                xalign 1.2
                yalign 0.4
                rotate 30
            with dissolve
            jump break_chill
    return
