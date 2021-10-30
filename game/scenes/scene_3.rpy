label scene_3:
    scene background_scene_3
    show hookah:
        xalign 0.65
        yalign -0.1
        zoom 0.8
    show shrek wait:
        xalign 0.4
        yalign 0.8
    with dissolve


    play sound "audio/dooropen.wav"

    s "ДА КТО ЕЩЕ ПРИШЕЛ?!"

    play music "<from 1 to 3>audio/noisypeople.wav" volume 1.3 noloop

    play sound "<from 3>audio/noisypeople.wav" volume 0.5 loop

    play music "audio/scene_3_friends.mp3" volume 0.1 loop

    $ zekab = 1
    $ leha = 1
    $ zekac = 1

    e "ООоо Мааксееем мы пришли тусииииить."

    "Максим был недоволен, но решил, что он лично встретит каждого гостя,
    щелкнув на него мышкой."


    label choose_screen_scene_3:

        if zekab == 0 and leha == 0 and zekac == 0:
            $ renpy.jump("all_done")

        call screen croud

        label all_done:
            hide shrek
            show shrek mad at center, shrekzoom
            with dissolve
            play sound "<from 0.5 to 2.7>audio/shrek_roar.mp3" volume 0.1
            s "НУ ВСЕ Я СГОРЕЛ НАХУЙ"
            play sound "<from 0.5 to 2.7>audio/shrek_roar.mp3" volume 0.1
            s "КАКОГО ХРЕНА ВЫ ВСЕ СЮДА ПРИШЛИ"
            play sound "<from 0.5 to 2.7>audio/shrek_roar.mp3" volume 0.1
            s "ЭТО МОЕ БОЛОТОООО"

            show donkey normal at right, donkeyzoom
            with dissolve

            d "Блееен я Макара забыл взять. Ща я на таксе туда и обратно."

            hide donkey normal
            with dissolve

            hide shrek mad
            show shrek wait hand at center
            with dissolve

            s "Я с тобой. Брат, ты за старшего!"

            vk "Конечно, братишка!"

            show donkey normal:
                zoom 0.5
                rotate 0
                xalign 2.0
                yalign 0.5
                linear 3.0 rotate -45
            stop music fadeout 3.0
            stop sound fadeout 3.0

            d "Там такси уже ожидает, давайте быстрее."

            s "Да выхожу, выхожу."

            show black
            show text "В это время у Макара" at truecenter
            with dissolve
            pause 1
            return

        label hide_leha:
            show leha normal at right, lehazoom
            l "О здарова. Я тут наливочку принес, ты угощайся.
            Я еще калик думаю забить, люблю как следует подуть"
            $ leha = 0
            hide leha normal
            show leha_idle:
                xalign 0.25
                yalign 0.0
                zoom 0.5
            jump choose_screen_scene_3

        label hide_zekab:
            show zekab_idle at right, osevenzoom
            zb "Смари че могу"
            show zekab_idle:
                parallel:
                    linear 1.0 xalign 1.0
                    linear 1.0 xalign 0.0
                    repeat
                parallel:
                    linear 1.3 yalign 1.0
                    linear 1.3 yalign 0.0
                    repeat
                parallel:
                    zoom 0.7
                    rotate_pad False
                    rotate 0
                    linear 4.0 rotate -360
                    repeat
            zb "Хоба"
            hide zekab_idle
            show zekab_idle at bounce:
                xalign 0.7
                yalign 0.05
                zoom 0.25
            $ zekab = 0
            jump choose_screen_scene_3

        label hide_zekac:
            show zekac_idle at right, zekaczoom
            zc "Здарова"
            zc "Сразу скажу - мне на смену завтра поэтому я ненадолгооооОООо....."
            show zekac_idle at popierdolilo
            zc "Ладно, спизданул, я здесь до утра. Чувствую углями пахнет - ну так я первый в очереди значит"
            hide zekac_idle
            show zekac_idle:
                zoom 0.5
                xzoom 0.25 yzoom 1.5
                xalign 0.1
                yalign 0.4
            $ zekac = 0
            jump choose_screen_scene_3
