label scene_6:
    image background_scene_6:
      zoom 1.5
      "images/backgrounds/bg duloc_scene_6.jpg"

    scene background_scene_6

    show farquaad normal at left
    with dissolve

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
        if not score:
            ik "Ты что, совсем тупой?"
            $ score = 0
            jump dragndrop_scene_6
        else:
            jump continue_scene_6

    label continue_scene_6:

        ik "Все верно."

        s "А на болото тогда кто?"

        ik "Ты, ты на болото, но позже. А теперь пиздуйте отсюда."

        return
