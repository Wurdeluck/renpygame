label scene_10:
    scene bg forest
    show shrek normal at right, shrekzoom
    show vika normal at center, customzoom
    show donkey normal at left, donkeyzoom
    with dissolve

    v "Ребят, я шарю за автостоп, со мной быстро до Томска доберемся."

    s "Жаль что пришлось убегать так быстро, что мы не успели взять билеты на автобус."

    d "Мне кажется так даже интереснее."

    s "Я рад что ты перестал говорить цитатами."

    tn "ХА-ХАА, ПОХОЖЕ ВЫ, ДЕТИШКИ, НЕ ЗНАЕТЕ, ЧЕМ ОПАСНА ЭТА ДОРОГА."

    d "Кто здесь?"

    tn "ЭТО Я - РОБИН ГУД!"

    show robinhood_idle at center, customzoom
    with dissolve

    rg_ "И МОИ ЛЮДИ!"

    hide robinhood_idle
    with dissolve

    show luda_idle at center, ludazoom
    with dissolve

    rg "ЭТО МОЯ ДОРОГА, МАЛЬЦЫ!"

    v "Почему ты на нас кричишь?"

    s "Хе-хе, маловато ты людей набрал, нас-то трое."

    rg "ЗА ТАКУЮ ДЕРЗОСТЬ Я ЗАБЕРАЮ ТВОЙ МИНИСК."

    s "AAAaaAAAaAAAAAAaaaaaa."

    hide shrek normal
    with dissolve

    d "Братан без миниска все еще братан, а вот без души - продаван."

    v "Не нервничай, справимся. Теперь бой равный."

    lf "Ехеехех...  Ctrl + C, Ctrl + V + V + V + V + V + V"
    hide luda_idle
    show luda_idle at ludazoom, multiply

    v "Ойёёёй... сказала бы я, если бы не выросла с двумя младшими сестрами. А ну подходи по одной!"

    d "Он прячется за спинами своих людей! Найди его и тогда мы сможем победить!"

    hide vika normal
    hide donkey normal
    with dissolve

    call screen game_rangedweapon

    show robinhood_idle at center, customzoom
    with dissolve

    rg "Извините я больше не буду( Хотите подвезу до больнички? У вас тут парень страдает."

    show shrek nominisk at right
    with dissolve

    s "АААааАААаАААаА больнааааа"

    show vika normal at left, customzoom
    with dissolve

    v "Да, подвезите нас пожалуйста."

    return
