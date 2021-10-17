label scene_2:
    play sound "audio/doorbell.wav"

    scene bg swamp_scene_2 with dissolve

    show shrek mad at left:
        zoom 2.0
    with dissolve

    s "Кто это там? Я никого не жду, должно быть, это соседи сверху"

    play audio "audio/doorbell.wav"

    play audio [ "<silence .5>", "audio/doorbell.wav" ]

    s "Придется посмотреть кто же там пришел"

    play sound "audio/dooropen.wav"

    show donkey normal at right:
        zoom 2.0
    with dissolve

    d "Привет Максим!"

    s "Привет ???{w} А ты кто?"

    d "Меня вперед отправили, чтобы угли поставить. Я вот купил 25, они вроде
    норм. Еще табака немного взял, маст хэв, мануал, короче все как ты любишь"

    s "Да я вообще думал сейчас на гитаре поиграть. Один."

    d "Ого, прикольно, а ты на гитаре играешь?"

    s "Я не в настроении сейчас тусить"

    d "Да мы сейчас настроимся как следует, у меня тут 'нелюбимый алкоголь Максима'"

    s "Слушай иди нахуй а"

    d "Ахаха это как тот мем Максим иди нахуй только ты Максим поэтому ты идешь нахуй получается"

    show screen stop_torture

    $ possible_questions = ["А почему ты седой?",
                            "А почему квартира такая маленькая?",
                            "А нахуя в Зеленых горках купил, Южные ворота же лучше?",
                            "А где учишься?",
                            "А где работаешь?",
                            "А почему не в офисе?",
                            "А дальше чем думаешь заниматься?",
                            "А как в Томске оказался?",
                            "А как вообще в компанию попал?",
                            "То есть вы все друзья тут?",
                            "А часто вы так собираетесь?",
                            "А соседи не беспокоят?",
                            "А сам ты откуда?",
                            "Расскажи мне о своей семье",
                            "А ты сова или жаворонок?",
                            "Кого ты больше люишь - кошек или собак?",
                            "А сколько жмешь?",
                            "А какой твой любимый цвет?"]

    $ possible_answers = ["Иди нахуй", "УХОДИ С МОЕГО БОЛОТА", "Да ты заебал", "Не твое дело"]

    label infinite_loop:
        python:
            random_question = possible_questions.pop(0) if possible_questions else "Ой скажи еще что-нибудь у тебя такой приятный голос"
        d "[random_question]"
        python:
            random_answer = renpy.random.choice(possible_answers)
        s "[random_answer]"

        jump infinite_loop

    label finish_scene_2:

        hide screen stop_torture

        d "Копец ты интересный Максим"

        s "..."

        play audio "audio/doorbell.wav"

        d "О а вот и ребятки"

        return
