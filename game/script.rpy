# Вы можете расположить сценарий своей игры в этом файле.

# Стиль с обводкой
style default:
    outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

# Определение персонажей игры.
define s = Character('Шрек', color="#0cb131")

define d = Character("Андрей", color="#4f3b0d")
# define d = DynamicCharacter('d_name', image='donkey', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#4f3b0d")

define e = Character("Все", color ="#371540")

define l = Character("Лёха", color ="#4a4118")

define zb = Character("Жека Белоглазов", color ="#4a4118")

define zc = Character("Жека Чупин", color ="#4a4118")

define zc = Character("Жека Чупин", color ="#4a4118")

define i = Character("Ира", color ="#a21919")

define m = Character("Макар", color ="#08041a")

define sk = Character("Капрал", color ="#abb627")

define ds = Character("Данька", color="#4f3b0d")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    """Здесь должно быть милое видео с нарезкой со свадьбы, где автор рассказывает
    про проклятие Фионы и пророчество и т.д."""

    call scene_1

    call scene_2

    call scene_3

    call scene_4

    call scene_5

    "ВСЕ!"

    return
