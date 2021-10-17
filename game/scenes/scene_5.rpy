label scene_5:
    scene bg svoya_igra
    play music "audio/millioner.mp3"

    $ ira = 1
    $ vika = 1
    $ sasha = 1

    label choose_screen_scene_5:

        scene bg svoya_igra

        call screen choose_naumenko

        label hide_ira:
            play sound "audio/wrong.mp3"
            $ ira = 0
            show bg duloc_scene_4
            show farquaad normal at left, customzoom
            show mirror at right
            with dissolve
            i "Видно же что хорошая деваха, почему неет?"

            m "Она учитель в Красноярске, она не любит тусить 24 на 7"
            hide farquaad normal
            hide mirror
            hide bg duloc_scene_4
            with dissolve
            jump choose_screen_scene_5

        label hide_sasha:
            play sound "audio/wrong.mp3"
            $ sasha = 0
            show bg duloc_scene_4
            show farquaad normal at left, customzoom
            show mirror at right
            with dissolve
            i "Да вот же, спортивная, на фотках улыбается, что не так?"

            m "Сорян, мой косяк, у нее уже есть молодой человек"
            hide farquaad normal
            hide mirror
            hide bg duloc_scene_4
            with dissolve
            jump choose_screen_scene_5

        label hide_vika:
            $ vika = 0
            play sound "audio/correct.mp3"
            show bg duloc_scene_4
            show farquaad normal at left, customzoom
            show mirror at right
            with dissolve
            i "Ага! Да, мне кажется, это идеальный вариант"

            m "Единственное что она в Красноярске..."

            i "Серьезно? Надо срочно привезти ее сюда. Макар, езжай!"

            m "Неее я не могу я пьяненький"

            i "Да, это я вижу.{w} Что же делать..."

            show shrek mad at center
            with dissolve

            s "Почему в моем доме толпа каких-то чуваков в странных костюмах???"

            i "Максиим, привееет"

            m "Макси - им"

            s "Я хочу просто мирно сидеть у себя дома :("

            i "Максим, есть идея, как все исправить. План такой..."

            stop music fadeout 5.0

            hide farquaad normal
            hide mirror
            hide shrek mad
            hide bg duloc_scene_4
            with dissolve
            return
