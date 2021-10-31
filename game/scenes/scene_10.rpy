label scene_10:
    scene bg forest
    show shrek normal at right, shrekzoom
    show vika normal at center, vikazoom
    show donkey normal at left, donkeyzoom
    with dissolve

    play sound "audio/scene_10_nature.mp3" volume 0.2 loop

    s "Жаль что пришлось убегать так быстро, что мы не успели взять билеты на автобус."

    v "Ребят, я шарю за автостоп, со мной быстро до Томска доберемся."

    d "Мне кажется так даже интереснее."

    s "Я рад что ты перестал говорить цитатами."

    play music "audio/scene_10_glam.mp3" volume 0.3 loop

    tn "ХА-ХАА, ПОХОЖЕ ВЫ, ДЕТИШКИ, НЕ ЗНАЕТЕ, ЧЕМ ОПАСНА ЭТА ДОРОГА."

    d "Кто здесь?"

    tn "ЭТО Я - РОБИН ГУД!"

    hide shrek normal
    hide vika normal

    show vika normal:
        xzoom -1.0
        xalign 0.2
        yalign 1.0
        zoom 0.7
    show shrek normal:
        xalign 0.4
        yalign 1.0
        zoom 1.8

    show robinhood at right
    with dissolve

    rg_ "И МОИ ЛЮДИ!"

    # with dissolve
    # hide robinhood_idle

    show luda at right
    with dissolve

    rg "ЭТО МОЯ ДОРОГА, МАЛЬЦЫ!"

    v "Почему ты на нас кричишь?"

    hide shrek normal
    show shrek protec:
        xalign 0.4
        yalign 1.0
        zoom 0.3

    s "От девушки отошел быстра"

    rg "ЗА ТАКУЮ ДЕРЗОСТЬ Я ЗАБЕРАЮ ТВОЙ МИНИСК."

    play sound "<from 0.5 to 2.7>audio/shrek_roar.mp3" volume 0.1
    s "AAAaaAAAaAAAAAAaaaaaa."

    hide shrek normal
    with dissolve

    d "Братан без миниска все еще братан, а вот без души - продаван."

    v "Не нервничай, справимся. Теперь нас 2 на 2."

    lf "Ехеехех...  Ctrl + C, Ctrl + V + V + V + V + V + V"
    hide luda
    show luda at right
    show expression "images/characters/Randoms/luda_idle.png" as luda2 at luda2zoom
    show expression "images/characters/Randoms/luda_idle.png" as luda3 at luda3zoom
    with dissolve
    # show luda_idle onlayer "overlay"

    v "Ойёёёй... сказала бы я, если бы не выросла с двумя младшими сестрами."

    hide vika normal
    show vika fight at vikafightzoom
    with dissolve

    v "А ну подходи по одной!"


    d "Он прячется за спинами своих людей! Найди его и тогда мы сможем победить!"

    hide vika normal
    hide donkey normal
    hide robinhood
    hide luda
    hide luda2
    hide luda3
    with dissolve

    call screen game_rangedweapon

    label after_fight:

        show robinhood_idle at center
        with dissolve

        rg_ "Извините я больше не буду( Хотите подвезу до больнички? У вас тут парень страдает."

        show shrek nominisk at right, shrekzoom
        with dissolve

        play sound "<from 0.5 to 2.7>audio/shrek_roar.mp3" volume 0.1
        s "АААааАААаАААаА больнааааа"

        show vika normal at left, vikafightzoom
        with dissolve

        stop music fadeout 3.0
        stop sound fadeout 3.0

        v "Да, подвезите нас пожалуйста. Так уж и быть, поухаживаю за тобой."

        s "{image=emoji}"

        return
