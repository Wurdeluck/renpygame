label scene_9:
    scene bg kras
    show shrek normal at left, shrekzoom
    show vika normal at right, vikazoom

    s "Поехали в Томск."

    v "Не хочу, мне и здесь нравится."

    s "Аааээээ"

    "Хорошие мысли часто преследовали Максима, но он был быстрее. Он подумал, что лучшим способом заманить Вику в Томск будет соблазнить ее."

    e "Давайте поможем Максиму соблазнить Вику! Для этого выберите те фразы, которые, как вы думаете, соблазнили бы Вику."

    e "..."

    e "..."

    e "Отлично!"

    s "Вика!"


    menu scene_9_question_1:
        "Подкат про шахматы":
            show shrek corner at left, shrekcornerzoom
            show vika normal at right, vikazoom
            with dissolve
            s "Смотрела ли ты Ход королевы?"

            v "Да, а что?"

            s "В шахматах ходят по очереди, а после меня ты не сможешь ходить по диагонали."

            v "Это было... Непонятно."
            hide shrek corner
            hide vika normal
            with dissolve
            jump scene_9_part_1
        "Подкат про беляш":
            show shrek corner at left, shrekcornerzoom
            show vika normal at right, vikazoom
            with dissolve
            s "Ты как беляш с вокзала."

            v "Почему?"

            s "Горячая, сочная и опасная."

            v "Даже слегка поэтично."
            hide shrek corner
            hide vika normal
            with dissolve
            jump scene_9_question_1

    label scene_9_part_1:
        menu scene_9_question_2:
            "Подкат в стихах":
                show shrek corner at left, shrekcornerzoom
                show vika normal at right, vikazoom
                with dissolve
                s "Луна ярко светит отражением в реке, неудобно держать пиво, ведь твоя рука в моей руке."

                v "???"

                s "Почему ты смотришь на меня так дико, Вика, я ведь симпатичнее таджика"

                v "Кто тебя позвал?"
                hide shrek corner
                hide vika normal
                with dissolve
                jump scene_9_question_2

            "Подкат наоборот":
                show shrek corner at left, shrekcornerzoom
                show vika normal at right, vikazoom
                with dissolve
                s "Теперь ты ко мне подкатываешь."

                v "Чего? А кхмм... Это у тебя меч в кармане или ты рад меня видеть?"

                s "Ох как романтично я согласен поехали в Томск."

                v "Ахахха нет."
                hide shrek corner
                hide vika normal
                with dissolve
                jump scene_9_part_2

    label scene_9_part_2:
        menu scene_9_question_3:
            "Всратый подкат":
                show shrek corner at left, shrekcornerzoom
                show vika normal at right, vikazoom
                with dissolve
                s "Ты как туалет."

                v "Так это уже обидно, я что, воняю?"

                s "Чем ты ближе, тем сильнее хочется."
                hide shrek corner
                hide vika normal
                with dissolve
                jump scene_9_question_3

            "Рабочий подкат 100\%":
                show shrek corner at left, shrekcornerzoom
                show vika normal at right, vikazoom
                with dissolve
                s "А давай мы просто потусим в Томске пару дней, там крутые чуваки, смотри видосик с тусы."

                v "АХАХАХАХАХ и правда смешно. Ладно, поехали. Но больше никаких подкатов."

                s "Даю слово"
                hide shrek corner
                hide vika normal
                with dissolve
                jump scene_9_part_3
    label scene_9_part_3:
        show shrek normal at left, shrekzoom
        show vika normal at right, vikazoom
        show donkey normal at center, donkeyzoom
        with dissolve
        d "Нельзя удержать силой дождь, человека и жизнь..."

        v "Он дурачок что ли?"

        s "Кажется он намекает, что нам пора бежать."

        show kris fly at top, kriszoom
        with dissolve

        kr "ВЫ КУДА ЭТО СОБРАЛИСЬ??"

        s "Уходим!"

        hide shrek normal
        hide vika normal
        hide donkey normal
        with dissolve
        show kris stay at truecenter, kriszoom
        kr "РРррРРРРРррррРРРРррРрррр"
        hide kris stay with dissolve
        return
