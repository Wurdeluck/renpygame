# Вы можете расположить сценарий своей игры в этом файле.

# Бэкграунды

image background_scene_1:
    zoom 1.5
    "images/backgrounds/bg swamp_scene_1_alter.jpg"

image background_scene_3:
    zoom 0.5
    "images/backgrounds/bg scene_3.jpg"

image background_scene_4:
    zoom 1.5
    "images/backgrounds/bg duloc_scene_4.jpg"

image background_scene_6:
    zoom 1.85
    "images/backgrounds/bg duloc_scene_6.jpg"


# Стиль с обводкой
style default:
    outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

# Определение персонажей игры.
define s = Character('Шрек', color="#0cb131")

define d = Character("Осёл", color="#4f3b0d")
# define d = DynamicCharacter('d_name', image='donkey', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#4f3b0d")

define e = Character("Все", color ="#371540")

define l = Character("Лёха", color ="#4a4118")

define zb = Character("Жека Белоглазов", color ="#4a4118")

define zc = Character("Жека Чупин", color ="#4a4118")

define ik = Character("Лорд Фаркуад", color ="#a21919")

define m = Character("Зеркало", color ="#371fa2")

define sk = Character("Печеня", color ="#abb627")

define kr = Character("Драконша", color="#631567")

define v = Character("Фиона", color="#30adaa")

define tn = Character("Таинственный незнакомец", color="#2b6c1d")

define rg_ = Character("РОБИН ГУД", color="#210f67")

define rg = Character("РОБИН ГУД (И ЕГО ЛЮДИ)", color="#210f67")

define lf = Character("РОБИН ГУД (И ЕГО ЛЮДИ)", color="#228620")

define dz = Character("Димас", color="#7f2c86")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    """Здесь должно быть милое видео с нарезкой со свадьбы, где автор рассказывает
    про проклятие Фионы и пророчество и т.д."""

    call scene_1 from _call_scene_1

    call scene_2 from _call_scene_2

    call scene_3 from _call_scene_3

    call scene_4 from _call_scene_4

    call scene_5 from _call_scene_5

    call scene_6 from _call_scene_6

    call scene_7 from _call_scene_7

    call scene_8 from _call_scene_8

    call scene_9 from _call_scene_9

    call scene_10 from _call_scene_10

    call scene_11 from _call_scene_11

    call scene_12 from _call_scene_12

    call scene_13 from _call_scene_13

    call scene_14 from _call_scene_14

    "ВСЕ!"

    return
