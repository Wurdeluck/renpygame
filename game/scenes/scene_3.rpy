label scene_3:
    scene bg swamp_scene_3
    show shrek wait at center
    with dissolve

    s "ДА КТО ЕЩЕ ПРИШЕЛ"

    play sound "audio/dooropen.wav"

    play music "<from 1 to 3>audio/noisypeople.wav" volume 1.3 noloop

    play music "<from 3>audio/noisypeople.wav" volume 0.5 loop

    $ zekab = 1
    $ leha = 1
    $ zekac = 1

    e "ООоо Мааксееем мы пришли тусииииить"

    hide shrek
    show shrek wait:
        zoom 0.7
        xalign 0.4
        yalign 0.3

    label choose_screen_scene_3:

        if zekab == 0 and leha == 0 and zekac == 0:
            $ renpy.jump("all_done")

        call screen croud

        label all_done:
            hide shrek
            show shrek mad at center:
                zoom 2.0
            with dissolve
            s "НУ ВСЕ Я СГОРЕЛ НАХУЙ"
            s "КАКОГО ХРЕНА ВЫ ВСЕ СЮДА ПРИШЛИ"
            s "ЭТО МОЕ БОЛОТОООО"
            show donkey normal:
                zoom 2.0
                rotate 0
                xalign 1.6
                yalign 0.5
                linear 5.0 rotate -45
            with dissolve
            d "Блееен я Макара забыл взять. Ща я на таксе туда и обратно"
            s "Я с тобой"
            stop music fadeout 5.0
            show black
            show text "В это время у Макара" at truecenter
            with dissolve
            pause 1
            return

        label hide_leha:
            show leha_idle at left
            l "О здарова. Я тут наливочку принес, ты угощайся.
            Я еще калик думаю забить, люблю как следует подуть"
            $ leha = 0
            hide leha_idle
            show leha_idle:
                xalign 0.3
                yalign 0.6
                zoom 0.25
            jump choose_screen_scene_3

        label hide_zekab:
            show zekab_idle at left
            zb "Смари че могу"
            show zekab_idle:
                parallel:
                    linear 1.0 xalign 0.0
                    linear 1.0 xalign 1.0
                    repeat
                parallel:
                    linear 1.3 yalign 1.0
                    linear 1.3 yalign 0.0
                    repeat
                parallel:
                    rotate_pad False
                    rotate 0
                    linear 4.0 rotate 360
                    repeat
            zb "Хоба"
            hide zekab_idle
            show zekab_idle at bounce:
                xalign 0.1
                yalign 0.1
                zoom 0.25
            $ zekab = 0
            jump choose_screen_scene_3

        label hide_zekac:
            show zekac_idle at left
            zc "Здарова"
            zc "Сразу скажу - мне на смену завтра поэтому я ненадолгооооОООо....."
            show zekac_idle at popierdolilo
            zc "Ладно, спизданул, я здесь до утра. Чувствую углями пахнет - ну так я первый в очереди значит"
            hide zekac
            show zekac_idle:
                zoom 0.5
                xzoom 0.25 yzoom 1.5
                xalign 0.1
                yalign 0.4
            $ zekac = 0
            jump choose_screen_scene_3
