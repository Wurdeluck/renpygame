label scene_6:

    scene background_scene_6

    show farquaad normal at left
    show blackboard:
        xalign 0.8
        yalign 1.0
    with dissolve

    play music "audio/VidaLoca.mp3" volume 0.1 loop

    ik "Слушай внимательно."

    ik """
    {cps=1000}Ты, Максим, должен будешь съездить в Красноярск и привезти мне Вику.
    Ее охраняет дракон, поэтому так просто тебе не справиться.
    В таком случае я заберу всех челиков из твоего болота и ты сможешь провести
    остаток своих дней в покое.{/cps}{nw}
    """

    ik "Понял?"

    s "Понял."

    ik "Повтори."

    hide farquaad
    show dasha at left, dashazoom
    with dissolve

    dp "Давайте поможем Максиму вспомнить план действий! Перетащите каждого персонажа в соответствующее место."

    dp "Кстати, персонажей можно отправлять в одно и то же место."

    dp "Бонус: одна из комбинаций открывает секретную концовку."

    hide dasha
    show farquaad normal at left
    with dissolve

    label dragndrop_scene_6:

        call screen war_draft

        python:
            concatinated = "Получается, "
            shrek_dest = result["Шрека"]
            vika_dest = result["Вику"]
            party_dest = result["тусу"]
            score = 0
            if shrek_dest == "в Красноярск":
                score += 1
            if vika_dest == "на хату Макара":
                score += 1
            if party_dest == "нахуй":
                score += 1
            if shrek_dest == party_dest == vika_dest:
                concatinated += "все должны отправиться {}".format(party_dest)
            elif shrek_dest != party_dest and shrek_dest != vika_dest and party_dest != vika_dest:
                concatinated += "Шрека - {0}, Вику - {1}, ну а тусу - {2}".format(shrek_dest, vika_dest, party_dest)
            elif shrek_dest == vika_dest:
                concatinated += "Шрека и Вику - {0}, ну а тусу - {1}".format(vika_dest, party_dest)
            elif shrek_dest == party_dest:
                concatinated += "Шрека и тусу - {0}, а Вику, значит, {1}".format(party_dest, vika_dest)
            elif vika_dest == party_dest:
                concatinated += "Вику и тусу надо отправить {0}, а я иду {1}".format(party_dest, shrek_dest)

        s "[concatinated]"
        $ result = {"Вику":0, "Шрека":0, "тусу":0}
        $ score = True if score == 3 else False
        $ final = shrek_dest == party_dest == vika_dest == "нахуй"
        if final:
            ik "Ты чего наделал..."
            "Так и закончилась их история. Они все отправились нахуй."
            hide farquaad normal
            show black
            show end fuckoff at truecenter
            with dissolve
            play sound "<to 2.8>audio/whatchasay.mp3"
            pause 3
            hide end fuckoff
            hide black
            show farquaad normal at left
            with dissolve
            jump dragndrop_scene_6
        if not score:
            ik "Ты что, совсем тупой?"
            $ score = 0
            jump dragndrop_scene_6
        else:
            jump continue_scene_6

    label continue_scene_6:

        stop music fadeout 4.0

        ik "Все верно."

        s "А на болото тогда кто?"

        ik "Ты, ты на болото, но позже. А теперь пиздуйте отсюда."

        return
