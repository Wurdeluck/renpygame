label scene_4:
    scene background_scene_4
    show farquaad normal at left
    show pryana normal at right, shrekzoom
    with dissolve

    play music "audio/scene_4_castles.mp3" volume 0.1 loop 

    ik "Я хочу спать"

    sk "Давайте все успокоимся и все мирно урегулируем"

    show farquaad normal at left, shake:
        linear 1.0 zoom 1.2

    ik "{b}Да я не хочу успокаиваться, у меня болит голова от кальяна и Макар свалил куда-то! Он же едва ноги переставляет!{/b}"

    sk "Макар ведь не один вышел, а со всеми, ничего с ним не случится."

    ik "{b}Да ты видел в каком он состоянии вышел? Он в моих ботинках ушел!{/b}"

    sk "Сейчас мы его приведем. Одна нога здесь другая там."

    hide pryana normal with dissolve

    show mirror normal at right, mirrorzoom
    with dissolve

    ik "{b}Где ты ходишь, я вообще-то волнуюсь!{/b}"

    m "Ну Ир ну я же вот вышел в вышку я тебе супчик взял."

    ik "{b}Да какой супчик, время 5 утра!{/b}"

    m "Сырный"

    show farquaad normal at left:
        linear 1.0 zoom 1.0

    ik "Ну если сырный тогда ладно."

    ik "Спать пойдем?"

    m "ЭЭээ какой спать я к Максиму тусить поеду."

    show farquaad normal:
        linear 1.0 zoom 1.2

    ik "Так что вы сразу у своего {i}Максима{/i} не собирались тогда?"

    m "Он не любит тусить, его нужно долго раскачивать..."

    ik "Ладно. Проехали. Ты сделал то что я просила?"

    m "Хррррр...."

    $ renpy.play('audio/punch.opus')
    with vpunch

    ik "Макар! Я с тобой разговариваю!"

    stop music fadeout 4.0

    m "ммм что да я проснулся"

    ik "Ты поискал девушку Максиму, чтобы она была классная веселая умная и любила тусить?"

    m "Да, вот они слева направо."

    return
