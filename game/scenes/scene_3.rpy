label scene_3:
    scene bg swamp_scene_3 with dissolve
    show shrek shock with dissolve

    s "ДА КТО ЕЩЕ ПРИШЕЛ"

    play sound "audio/dooropen.wav"

    play music "<from 1 to 3>audio/noisypeople.wav" volume 1

    e "ООоо Мааксееем мы пришли тусииииить"

    play music "audio/noisypeople.wav" volume 0.5 loop

    $ zekab = 1
    $ leha = 1

    label before_screen:

        if zekab == 0 and leha == 0:
            $ renpy.jump("all_done")

        call screen croud

        label all_done:
            "НУ ВСЕ Я СГОРЕЛ НАХУЙ"
            return

        label hide_leha:
            show leha full at left
            l "О здарова. Я тут наливочку принес, ты угощайся.
            Я еще калик думаю забить, все будет в лучшем виде"
            $ leha = 0
            show leha full at right:
                zoom 0.25
            jump before_screen

        label hide_zekab:
            "Ytnnnn"
            $ zekab = 0
            jump before_screen
