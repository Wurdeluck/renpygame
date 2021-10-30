label scene_14:
    scene background_scene_4
    show shrek mad at left, shrekzoom
    show farquaad normal at right
    with dissolve

    play music "audio/final_fight.mp3" volume 0.2 noloop

    s "Ты не выполнила свою часть сделки, а значит, я могу тусить с Викой сколько захочу!"

    show farquaad normal at right, farquaadflip

    ik "Мне Вика тоже нравится, я тебе ее не отдам!"

    # битва?

    v "Я вообще-то личность и сама буду решать с кем мне тусить."

    show kris fly at top, krisdoublezoom
    with dissolve

    kr "РРррРРРРрр кто моего Викосека украл, ты??"

    menu decision:
        "Кто украл Викосека?"
        "Это все она":
            jump continue
        "Это был я":
            s "Это был я"

            show shrek mad:
                pause 2.0
                alpha 0.0

            show kris fly:
                xalign 0.4
                yalign 1.0
                linear 1.0 rotate -60
            play sound [ "<silence 0.5>", "audio/nom_minecraft.mp3" ]
            kr "Ам"

            play sound "<from 4 to 9.5>audio/sad_allstar.mp3"
            hide shrek mad
            hide farquaad normal
            hide kris fly
            show black
            show notsomebody:
                yalign 0.3
                xalign 0.5
            show end notsomebody at top
            with dissolve
            pause 3
            hide end notsomebody
            hide notsomebody
            hide black
            show shrek mad at left, shrekzoom
            show farquaad normal at right
            show kris fly at top, krisdoublezoom
            with dissolve
            jump decision

    label continue:
        s "Это все она"

        show farquaad:
            pause 2.7
            alpha 0.0

        show kris fly:
            linear 0.5 xzoom -1.0
            xalign 0.4
            yalign 0.6
            linear 0.5 xalign 0.9 yalign 0.7
            linear 1.0 rotate 60
        play sound [ "<silence 1.3>", "audio/nom_minecraft.mp3" ]

        kr "Ам"

        hide kris fly
        hide farquaad
        with dissolve

        s "Вика"

        play music "audio/endmusic.wav" volume 1.0 noloop

        show vika normal at right, vikazoom
        with dissolve

        v "Что?"

        s "Ну Замок из стекла же правда отстой"

        v "Я не это хочу услышать"

        s "Вика, ты согласна жить вместе на моем болоте?"

        v "Да"

        e "Ураааа"

        v "Выплюнь Иру и будем тусеееть"

        hide shrek mad
        hide vika normal
        with dissolve

        show black
        show end happy at truecenter
        with dissolve
        stop music fadeout 3.0
        pause 3
        hide end notsomebody
        hide notsomebody
        hide black

        show shrek happy at flyingaround
        show vika normal at flyingaround
        show luda at flyingaround
        show donkey normal at flyingaround, donkeyzoom
        show leha_idle at flyingaround
        show zekac_idle at flyingaround, popierdolilo
        show zekab_idle at flyingaround
        show farquaad normal at flyingaround
        show mirror normal at flyingaround

        play music "audio/scene_14_believer.mp3" volume 0.5 loop

        menu the_end:
            "Закончить игру?"
            "Да":
                return
            "Нет":
                jump the_end
