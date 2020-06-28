label besik_end:

      scene avtovo_zvuk
      A "Интересно, что там за шум."
      A "Быть может, я не один тут застрял?"
      A "В таком случае, мне необходимо проверить!"
      "Я решил предупредить спасателей, крикнув:"
      A "Подождите, пожалуйста! Я сейчас!"
      "Крикнув это, я направился в сторону шороха."
      play sound "shagi_yopta.mp3"
      $ renpy.pause (3.0)
      scene zvuk with dissolve
      "Я осторожно ступаю в сторону звука, подсвечивая себе путь телефоном."
      stop sound
      A "Не похоже, чтобы здесь кто-то был..."
      A "Я, конечно же, в курсе о слуховых галлюцинациях, но, как мне кажется, для такого я ещё слишком молод."
      "Дойдя до середины станции, я огляделся."
      "Передо мной вырос...
       ЦВЕТОК?"
      stop music fadeout 3
      play music "theme_besik.mp3" fadeout 1
      show besik_usual:
           xalign 0.5
           yalign 0.4
      with dissolve

      B "А? Кто здесь?"

      hide besik_usual
      show besik_good:
           xalign 0.5
           yalign 0.4
      with dissolve
      B "О-о-о, человек. Рад тебя здесь приветствовать!"

      Bs "Я Бесик. Цветок Бесик. Я живу здесь уже до-о-о-олгие годы."
      hide besik_good
      show besik_smile:
           xalign 0.5
           yalign 0.4
      with dissolve

      Bs "Как ты попал сюда?"
      A "А-А-А-А-А! ГОВОРЯЩИЙ ЦВЕТОК!"
      hide besik_smile
      show besik_patrik:
           xalign 0.5
           yalign 0.4
      with dissolve and vpunch

      Bs "А-А-А! ГОВОРЯЩИЙ ЧЕЛОВЕК!?"
      hide besik_patrik
      show besik_podozrevaet1:
           xalign 0.5
           yalign 0.4
      with dissolve

      Bs "Приятно?"
      hide besik_podozrevaet1
      show besik_podozrevaet2:
           xalign 0.5
           yalign 0.4
      with dissolve

      Bs "Отвечай на вопрос, НЕВЕЖА!"
      A "Простите..."
      "Не смотря на испуг, я решил продолжить разговор с... Цветком."
      Ch "Меня зовут Чарли. Я человек. И, похоже, что либо меня разыгрывают, либо я всё ещё сплю."
      Ch "Бесик, верно?"
      hide besik_podozrevaet2
      show besik_podozrevaet1:
           xalign 0.5
           yalign 0.4
      with dissolve

      Bs "Ну, допустим.."
      Ch "Не подскажешь, как отсюда выбраться?"
      hide besik_podozrevaet1
      show besik_uhodish:
           xalign 0.5
           yalign 0.4
      with dissolve

      Bs "Уже уходишь?..."
      "Бесик внезапно поменялся в лице."

      Bs "Ты хоть представляешь, в какую ситуацию сейчас вляпался?!"

      Bs "Ты пришёл сюда с твёрдой уверенностью, что тебе здесь помогут."

      Bs "Но ты даже не додумался предположить своей скудной пустой головушкой, что здесь всё может быть не так радужно и хорошо, как в твоём родном мире."
      Ch "П.. Простите ещё раз. Я просто... Я пойду, пожалуй!"
      "Я попытался развернуться и убежать в направлении приближающегося фонарика предполагаемых спасателей, но что-то обвило мою ногу."
      Ch "Ай!"
      hide besik_uhodish
      show besik_fuck:
           xalign 0.5
           yalign 0.4
      with dissolve

      Bs "Не торопись."

      Bs "Твоя душа..."

      Bs "Ты знаешь, что здесь происходит, не так ли?"
      hide besik_fuck
      show besik_fuck2:
           xalign 0.5
           yalign 0.4
      with dissolve

      Bs "Ты просто хочешь видеть, как я мучаюсь!"

      Bs "Да, это определённо был ты! Я узнал тебя.."
      stop music fadeout 4
      play music "hunt_besik.mp3" fadeout 5
      hide besik_fuck2
      show besik_oret:
           xalign 0.5
           yalign 0.4
      with dissolve

      Bs "Да как ты смеешь!?"
      "Бесик перешёл на крик. Это всёрьёз начало меня пугать. Я решил попробовать его успокоить."
      Ch "П-Погоди, ты наверное..!"
      show besik_oret:
           xalign 0.5
           yalign 0.4
      with vpunch

      Bs "Ни слова больше! Вы все одинаковые! Вы, люди, можете только всё портить!"

      Bs "Глупый человек!"

      Bs "Я точно узнал твою душу!"

      Bs "Finito la comedia!"

      Bs "Сейчас свершится моя месть!"

      Bs "Наглый, подлый, бездушный воришка!"

      Bs "КАК!{w=0.3}
          ЖЕ!{w=0.3}
          ТЫ!{w=0.3}
          МЕНЯ!"
      hide besik_oret
      show besik_besitsa:
           xalign 0.5
           yalign 0.4
      with dissolve
      stop music fadeout 1

      Bs "Б{w=0.3}
          Е{w=0.3}
          С{w=0.3}
          И{w=0.3}
          Ш{w=0.3}
          Ь!!!"
      Ch "Ой-йо..."
      play sound "punch.wav"
      hide besik_besitsa with vpunch
      scene black_background
      $ renpy.pause (0.5)
      play sound "bad_end_laugh.mp3"
      $ renpy.pause (1.0)
      play sound "punch.wav"
      $ renpy.pause (1.0)
      play sound "punch.wav"
      $ renpy.pause (1.0)
      play sound "punch.wav"
      $ renpy.pause (1.0)
      play sound "punch.wav"
      $ renpy.pause (1.0)
      play sound "punch.wav"
      $ renpy.pause (1.0)
      play music "mus_gameover.ogg"
      scene ending1 with dissolve
      $ renpy.pause (20.0)
      return
