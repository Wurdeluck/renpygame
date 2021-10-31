label scene_13:
    scene background_scene_4
    show farquaad normal at left
    show vika normal at right, vikazoom
    with dissolve

    play music "audio/scene_13_hallelujah.mp3" volume 0.3 loop

    ik "Ну как Вика, тебе нравится тусить у нас?"

    v "Да, мне весело."

    ik "Такое ощущение что тебе не очень весело. Давай всех выгоним и почилим только вдвоем?"

    v "Мне все равно..."

    hide bg duloc_scene_4
    hide farquaad normal
    hide vika normal
    with dissolve

    scene background_scene_1
    show black:
        alpha 0.9
    show shrek sad at left, shrekzoom
    show leha normal:
        xalign 0.6
        yalign 0.8
        zoom 0.7
    show zekab_idle:
        xalign 0.8
        yalign 0.8
        zoom 0.5
    show zekac_idle:
        xalign 1.0
        yalign 0.8
        zoom 0.5
    with dissolve

    s "Мде, никого Ира отсюда не выгнала, все так же тусят как и раньше."

    s "Ну и ладно"

    e "Чего притих, Максим? Почему ты такой грустный?"

    s "Лучше скажите, почему электричества нет? У меня телефон сел."

    e "Мы слишком громко тусили и нам отключили свет. Пара дней уже прошла."

    s "Всего пара дней. А как будто вечность..."

    e "Расскажи, что случилось?"

    s "Я встретил самую прекрасную девушку в мире, но мы поссорились и теперь я буду жить один на болоте, а она тусить у Макара."

    e "Ты уверен, что это то, чего ты действительно хочешь?"

    s "Нет..."

    show mirror normal at center, mirrorzoom

    m "Максим, я знаю, что нужно делать"

    hide mirror normal
    show mirror empty at center, mirrorzoom

    play sound "<to 3>audio/skypecall.mp3" volume 0.4

    pause 3

    hide mirror empty
    show mirror dimas at center, mirrorzoom

    dz "Здарова Максим"

    s "Привет Димас. У меня проблема, я обидел девушку и не знаю что теперь делать."
    stop music fadeout 3.0

    dz "Ох Максим. Беги к ней быстрее!"

    hide shrek sad
    show shrek angry:
        xalign -0.5
        yalign 1.0
    with dissolve

    s "Спасибо Димас!"

    hide mirror dimas
    play sound "audio/skype_hangup.mp3" volume 0.4
    play music "audio/brainstorm.mp3" volume 0.2 loop

    s "Но я не могу вызвать такси! Кто-нибудь может вызвать?"

    e "Света же нет, какие телефоны?"

    s "О нет..."

    vk "Посторонитесь-ка"

    show valek normal at right, drekzoom

    vk "Я на тачке, давай подвезу."

    e "Ураа!"

    e "Дрэк! Дрэк! Дрэк!"

    s "Спасибо, я этого не забуду."

    vk "Тогда в путь!"

    hide shrek normal
    hide valek normal

    stop music fadeout 3.0

    e "Ты сможешь, Максим! Мы за тобой следом!"

    return
