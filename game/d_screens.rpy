##############################################3
######### ПЕРВЫЙ ЭПИЗОД СКРИНЫ ###############3
##############################################3

###### Картинки для экранов первого эпизода##########

##Осмотр детской комнаты в доме Тамары.

define krovat_idle = 'images/ep1_screens/detskaya/krovat_idle.png'
define krovat_hover = 'images/ep1_screens/detskaya/krovat_hover.png'

define komod_idle = 'images/ep1_screens/detskaya/komod_idle.png'
define komod_hover = 'images/ep1_screens/detskaya/komod_hover.png'

define sunduk_idle = 'images/ep1_screens/detskaya/sunduk_idle.png'
define sunduk_hover = 'images/ep1_screens/detskaya/sunduk_hover.png'

define kover_idle = 'images/ep1_screens/detskaya/kover_idle.png'
define kover_hover = 'images/ep1_screens/detskaya/kover_hover.png'

## Задний двор Тамары. Если вы понимаете о чём я ;)


define dorozhka_idle = 'images/ep1_screens/tamara_dvor/dorozhka_idle.png'
define dorozhka_hover = 'images/ep1_screens/tamara_dvor/dorozhka_hover.png'

define fasad_doma_idle = 'images/ep1_screens/tamara_dvor/fasad_doma_idle.png'
define fasad_doma_hover = 'images/ep1_screens/tamara_dvor/fasad_doma_hover.png'

define krysha_doma_idle = 'images/ep1_screens/tamara_dvor/krysha_doma_idle.png'
define krysha_doma_hover = 'images/ep1_screens/tamara_dvor/krysha_doma_hover.png'

define ogorod_idle = 'images/ep1_screens/tamara_dvor/ogorod_idle.png'
define ogorod_hover = 'images/ep1_screens/tamara_dvor/ogorod_hover.png'

define zabor_idle = 'images/ep1_screens/tamara_dvor/zabor_idle.png'
define zabor_hover = 'images/ep1_screens/tamara_dvor/zabor_hover.png'

## Кухня Тамары. Здесь понимать ничего не надо.

define kamin_idle = 'images/ep1_screens/tamara_kuhnya/kamin_idle.png'
define kamin_hover = 'images/ep1_screens/tamara_kuhnya/kamin_hover.png'

define generator_idle = 'images/ep1_screens/tamara_kuhnya/generator_idle.png'
define generator_hover = 'images/ep1_screens/tamara_kuhnya/generator_hover.png'

define knizhki_idle = 'images/ep1_screens/tamara_kuhnya/knizhki_idle.png'
define knizhki_hover = 'images/ep1_screens/tamara_kuhnya/knizhki_hover.png'

define plita_idle = 'images/ep1_screens/tamara_kuhnya/plita_idle.png'
define plita_hover = 'images/ep1_screens/tamara_kuhnya/plita_hover.png'

define stol_idle = 'images/ep1_screens/tamara_kuhnya/stol_idle.png'
define stol_hover = 'images/ep1_screens/tamara_kuhnya/stol_hover.png'

#################################################


screen tri_truby():
    imagemap:
        ground "images/ep1_screens/back_tt.png"
        hover "images/ep1_screens/hover_tt.png"

        hotspot(202, 11, 360, 696):
            action Jump("left_hole")# left hole
            hovered SetVariable('down_txt', 'Пойти в левую трубу')
            unhovered SetVariable('down_txt', ' . . . ')

        hotspot(669, 67, 228, 520):
            action Jump("center_hole")# center hole
            hovered SetVariable('down_txt', 'Пойти в центральную трубу')
            unhovered SetVariable('down_txt', ' . . . ')
        
        hotspot(989, 113, 162, 368):
            action Jump("right_hole")#right hole
            hovered SetVariable('down_txt', 'Пойти в правую трубу')
            unhovered SetVariable('down_txt', ' . . . ')

    use down_text_label


screen light_or_sound(): #ПУТЬ НА БЕСИКА ИЛИ К АЛЕ С АНЕЙ.
    image "images/ep1_screens/back_light_or_sound.png"

    use down_text_label

    #textbutton "Пойти на свет" xalign 0.66 yalign 0.5 action Jump("meet_monstergirls"), Hide('light_or_sound')
    # textbutton "Пойти на шорох" xalign 0.33 yalign 0.5 action Jump("besik_end"), Hide('light_or_sound')
    use arrow(360, 360, 'besik_end', rotate_this(180), 'Пойти на звук')
    use arrow(720, 360, 'meet_monstergirls', rotate_this(0), 'Пойти на свет')


screen hallinto_screen(): ## зал в доме Тамары, откуда можем пройти на кухню, в коридор_трех_комнат или в подвал.

    image 'images/hall.png'

    use down_text_label

    use arrow(80, 317, 'levo', rotate_this(180), 'Пойти влево')
    use arrow(1048, 342, 'pravo', rotate_this(0), 'Пойти вправо')
    use arrow(600, 317, 'podval', rotate_this(135), 'Пойти в подвал')



screen koridor_screen(): ## коридор трёх комнат.

    image 'images/koridor.png'

    use down_text_label

    use mini_vhod(180, 309, 'dbtabl', 'Дверь без таблички')
    use mini_vhod(600, 309, 'dtabl', 'Дверь с табличкой')
    use mini_vhod(1020, 309, 'podkova', 'Дверь с подковой')

    use arrow(12, 526, 'hallinto', rotate_this(180), '-Вернуться в зал-')

#bubble_look(
# x y  -- Абсолютные позиции в пикселах 
# label_name -- имя лейбла, куда перепрыгнем при нажатии, txt='. . .' -- текст в полоске внизу.
#idle_image, hover_image)

screen detskaya_osmotr():

    use bubble_look(964, 346, 'd_krovat', 'Кроватка!', krovat_idle, krovat_hover)
    use bubble_look(592, 299, 'd_komod', 'Осмотреть комод', komod_idle, komod_hover)
    use bubble_look(407, 368, 'd_sunduk', 'Что в сундучке?', sunduk_idle, sunduk_hover)
    use bubble_look(1170, 59, 'd_kover', 'Ковёр, жаль что не самолёт', kover_idle, kover_hover)

    use arrow(30, 490, 'pravo', rotate_this(180), '-Выйти в коридор-')
    use down_text_label



screen dvor_tamara():

    use bubble_look(0, 531, 'dvor_dorozhka', "Осмотреть дорожку", dorozhka_idle, dorozhka_hover)
    use bubble_look(0, 268, 'dvor_zabor', 'Осмотреть забор', zabor_idle, zabor_hover)
    use bubble_look(0, 0, 'dvor_krysha', "Осмотреть крышу дома", krysha_doma_idle, krysha_doma_hover)
    use bubble_look(296, 97, 'dvor_fasad_doma', "Осмотреть фасад дома", fasad_doma_idle, fasad_doma_hover)
    use bubble_look(562, 336, 'dvor_ogorod', "Осмотреть огород", ogorod_idle, ogorod_hover)

    use mini_vhod(127, 150, 'dom_tamara', '-Зайти в дом-')
    use down_text_label


screen kuhnya_smotr():

    use bubble_look(871, 0, 'k_generator', 'Что это?..', generator_idle, generator_hover) # генератор вероятности
    use bubble_look(744, 63, 'k_shkaf', 'Книги в шкафу', knizhki_idle, knizhki_hover) # книжки
    use bubble_look(0, 421, 'k_stol', 'Слюнки текут!..', stol_idle, stol_hover) # стол
    use bubble_look(727, 344, 'k_plita', 'Газовая плита?..', plita_idle, plita_hover) # плита
    use bubble_look(54, 137, 'k_kamin', 'Как тепло от камина!', kamin_idle, kamin_hover) # камин

    use arrow(1100, 490, 'hallinto', rotate_this(0), '-Выйти из кухни-')
    use down_text_label

########################################
########### ЭПИЗОД ДВА СКРИНЫ ##########
########################################


screen zighouse_escape():

    imagemap:
        ground "images/ep2_screens/zighouse_escape_ground.png"
        hover "images/ep2_screens/zighouse_escape_hover.png"

        hotspot(350, 34, 290, 650):
            action Jump("center_door")# Прыгаем в централ_доор на плохую концовку
            hovered SetVariable('down_txt', 'В дверь напротив!')
            unhovered SetVariable('down_txt', ' . . . ')

        hotspot(645, 0, 318, 711):
            action Jump("zighouseproda")# Просто идём дальше.
            hovered SetVariable('down_txt', 'В правую дверь!')
            unhovered SetVariable('down_txt', ' . . . ')

    use down_text_label
    
##############################################3
####### Технические штуки -- э к р а н ы #####3
##############################################


#screen zaebalo:
#    text '[dvor_flag]' size 30


# Крутим как хотим и что хотим через эту трансу. Х - градусы
transform rotate_this(x):
    rotate x



screen arrow(x, y, label_name, tf='', txt=' . . . '): # tf обозначиает вид трансформации.
    imagebutton:
        xpos x
        ypos y
        idle 'images/ep1_screens/strelka.png'
        hover 'images/ep1_screens/strelka_hover.png'
        action Jump(label_name), SetVariable('down_txt', txt)
        if tf != '':
            at tf
        hovered SetVariable('down_txt', txt)
        unhovered SetVariable('down_txt', ' . . . ')


#--------------------------------------------
#------------------------------------------
# он шоу задаёт НАЧАЛЬНОЕ значение даун_тексту, тем самым РЕШАЕТ проблему
# со старым значением текста в НОВОМ скрине
# Используй это везде, где есть даун_текст_лейбл

#on 'show' action SetVariable('down_txt', ' . . . ')
#on 'hide' action SetVariable('down_txt', ' . . . ')
#!! А можно просто поместить его в сам скрин даун_текст_лейбл и ок всё робит...
#------------------------------------------------------

screen down_text_label:
    # Эта хрень вроде избавляет от проблемы ниже.
    on 'show' action SetVariable('down_txt', ' . . . ')
    on 'hide' action SetVariable('down_txt', ' . . . ')

    #Трабла в том, что при переход на  новый скрин,
    #где юзается онный текст, он показывает текст ИЗ СТАРОГО скрина, что не гуд.
    image 'gui/button/choice_idle_background.png':
        xalign 0.5
        yalign 0.955
    text down_txt xalign 0.5 yalign 0.95


screen mini_lupa(x, y, label_name, txt= ' . . .'): # кнопка Лупы для скринов.
    imagebutton:
        xpos x
        ypos y
        idle 'images/ep1_screens/mini_lupa.png'
        hover 'images/ep1_screens/mini_lupa_hover.png'
        action Jump(label_name), SetVariable('down_txt', txt)
        hovered SetVariable('down_txt', txt)
        unhovered SetVariable('down_txt', ' . . . ')


screen mini_vhod(x, y, label_name, txt='. . .'): #кнопка Входа для скринов
    imagebutton:
        xpos x
        ypos y
        idle 'images/ep1_screens/enter_idle.png'
        hover 'images/ep1_screens/enter_hover.png'
        action Jump(label_name), SetVariable('down_txt', txt)
        hovered SetVariable('down_txt', txt)
        unhovered SetVariable('down_txt', ' . . . ')


screen bubble_look(x, y, label_name, txt='. . .', idle_image, hover_image): #Основа для облачков предметов на выбор (испольузется почти везде, кек)
    imagebutton:
        xpos x
        ypos y
        idle idle_image
        hover hover_image
        action Jump(label_name), SetVariable('down_txt', txt)
        hovered SetVariable('down_txt', txt)
        unhovered SetVariable('down_txt', ' . . . ')



############################################
## ВЫБОР РЕЙТИНГА В САМОМ НАЧАЛЕ
############################################

screen rating_choice:
    image 'images/black_background.png'
    vbox:

        xalign 0.5
        yalign 0.3

        text 'Игра содержит сцены насилия.' size 32:
            at center
        text '{i}Изменить пункт цензуры можно и в настройкайх игры{/i}' size 20:
            at center

    textbutton 'Включить цензуру (13+)':
        xalign 0.2
        yalign 0.5
        action SetVariable('censor', True), Play('sound', 'anin_zvuk.wav'), Return(True)
    textbutton 'Отключить цензуру (18+)':
        xalign 0.8
        yalign 0.5
        action SetVariable('censor', False), Play('sound', 'mus_intronoise.ogg'), Return(True)

#transform sukablyat: 
#    alpha 1.0
#    xalign 0.5
#    yalign 0.5
#    time 3.0
#    linear 2.0 alpha 0.0


screen after_rate_choice:

    if censor:
        text 'Цензура включена':
            color '#FFFFFF'
            size 50
            at sukablyat

    else:
        text 'Цензура отключена':
            color '#dc143c'
            size 50
            at sukablyat

    timer 4.0 action Return(False)


