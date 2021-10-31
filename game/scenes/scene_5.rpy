label scene_5:
    scene bg svoya_igra
    play music "audio/millioner.mp3" volume 0.5

    $ ira = 1
    $ vika = 1
    $ sasha = 1

    label choose_screen_scene_5:

        scene bg svoya_igra

        call screen choose_naumenko

        label hide_ira:
            play sound "audio/wrong.mp3" volume 0.3
            $ ira = 0
            show farquaad bed at left, bedzoom
            show mirror disgust at right, mirrorzoom
            with dissolve
            ik "Видно же что хорошая деваха, почему неет?"

            m "Она учитель в Красноярске, она не любит тусить 24 на 7"
            hide farquaad bed
            hide mirror disgust
            with dissolve
            jump choose_screen_scene_5

        label hide_sasha:
            play sound "audio/wrong.mp3" volume 0.3
            $ sasha = 0
            show farquaad bed at left, bedzoom
            show mirror disgust at right, mirrorzoom
            with dissolve
            ik "Да вот же, спортивная, на фотках улыбается, что не так?"

            m "Сорян, мой косяк, у нее уже есть молодой человек"
            hide farquaad bed
            hide mirror disgust
            with dissolve
            jump choose_screen_scene_5

        label hide_vika:
            $ vika = 0
            play sound "audio/correct.mp3" volume 0.3
            show farquaad bed at left, bedzoom
            show mirror normal at right, mirrorzoom
            with dissolve
            ik "Ага! Да, мне кажется, это идеальный вариант"

            m "Единственное что она в Красноярске..."

            ik "Серьезно? Надо срочно привезти ее сюда. Макар, езжай!"

            m "Неее я не могу я пьяненький"

            ik "Да, это я вижу. Что же делать..."

            show shrek mad:
                xalign -0.4
                yalign 0.5
                rotate 45
                zoom 1.5
            with dissolve

            s "Почему в моем доме толпа каких-то чуваков в странных костюмах???"

            ik "Максиим, привееет"

            m "Макси - им"

            stop music fadeout 3.0

            s "Я хочу просто мирно сидеть у себя дома :("

            ik "Максим, есть идея, как все исправить. План такой..."

            hide farquaad bed
            hide mirror normal
            hide shrek mad
            with dissolve
            return
