import random
import sys
from random import randint
import os
from colorama import Fore, Back, Style
import argparse




print("""powered by
██████╗░██╗██╗░░░██╗
██╔══██╗██║██║░░░██║
██████╔╝██║╚██╗░██╔╝
██╔══██╗██║░╚████╔╝░
██║░░██║██║░░╚██╔╝░░
╚═╝░░╚═╝╚═╝░░░╚═╝░░░
╔╗─╔╗──────╔╗──────╔╗─╔╗──╔╗───╔╗
║║─║║──────║║──────║║─║║─╔╝╚╗──║║
║╚═╝╠══╦═══╣╚═╦╦═╗─║╚═╝╠═╩╗╔╬══╣║
║╔═╗║╔╗╠══║║╔╗╠╣╔╗╗║╔═╗║╔╗║║║║═╣║
║║─║║╔╗║║══╣╚╝║║║║║║║─║║╚╝║╚╣║═╣╚╗
╚╝─╚╩╝╚╩═══╩══╩╩╝╚╝╚╝─╚╩══╩═╩══╩═╝
""")
print(Fore.RED + """
   {1}--Правила
   {2}--Информация о сообществе
   {3}--Твой номер в отеле
   {99}-Exit
 """)
choice = input("Alastor~#")
os.system('clear')
if choice == "1":
   alastor()
elif choice == "2":
      andalastor()
elif choice == "3":
         andalastoryes()
elif choice == "99":
            sys.exit()
elif choice == "":
               menu()
else:
                  menu()
                  def "1"():
                     print("""Язык и возрастное ограничение.
 ↪Язык сообщества - русский. 
В следствии чего, диалоги исключительно на других языках и на транслите будут считаться за нарушение, а также посты/викторины/записи и прочее, с состовляющей только на иностранном языке.
◈Исключением являются: изображения с надписями или же комиксы; использование коротких, общеизвестных фраз; оформление профиля.""")
                     print("""Оффтоп 
↪Это материал(контент), не относящийся к той или иной тематике.
Наше сообщество посвящено «Hazbin Hotel» и в целом творчеству Вивьен Медрано, посторонний контент будет являться оффтопом.
Его проявление является нарушением.""")
                     print("""Спам/Флуд
↪Чрезмерное распространение чего-либо неинформативного, сопровождающееся неоднократными повторениями.
Это нарушение делится на две группы; спам в чатах, и общий спам.""")
                     print("""Агрессия
↪Любая форма неприемлемого поведение, зачастую направленного на нанесение физического, вербального, психологического или морального вреда другому.
Агрессивное поведение по отношению к другим, будь то участник или же администратор, строго запрещено.""")
                     print("""Бунт
↪Это активное, действенное сопротивление существующей власти с целью свержения, отмены ее влияния, волеизъявления и авторитета, установленных ею законов и порядков с целью последующего установления собственной власти, выражающей и воплощающей собственные интересы, устремления и волеизъявления.
Под «властью», само собой, подразумевается администрация нашего сообщества.""")
                     print("""Непристойные материалы.
↪Материалы, нерекомендуемые к их просмотру и огласке, они могут вызвать дискомфорт или шокирующию реакцию у человека.""")
                     print("""Реклама
↪Направление в маркетинговых коммуникациях, в рамках которого производится распространение информации для привлечения внимания к объекту рекламирования с целью формирования или поддержания интереса к нему.
В нашем сообществе строго запрещена реклама, и разрешение на неё уже не выдают.""")
                     print("""Ненормативная лексика
↪Нецензурные выражения, непечатная брань или непристойная лексика - сегмент браннойречи языка, включающий вульгарные бранные выражения, мат.
Подобная лексика у нас допустима, но строго с цензурой и без злоупотребления. Нарушением также будет считаться мат на транслите и с разделением букв символами.""")
                     print("""Попрошайничество
↪Осознанные действия, направленные на получение желаемого, тем самым выпрашивая у других.
Данный вид деятельности запрещён.""")
                     print("""Мери Сью.
↪Мери Сью, или же Марти Стью, это персонаж, которого автор наделил гипертрофированными положительными качествами, множеством способностей, везением, и зачастую идеальной внешностью. Нередко к ним приплетают вид или же способности какого либо канонного персонажа. 
В нашем сообществе запрещены Мери Сью.""")
                     print("""Плагиат
↪Выдача чужого творения за свое или использование в своих трудах чужого произведения без указания автора. Это кража чужих работ, присваивая их авторство себе.""")
                     print("""Авторское право
↬Интеллектуальное право на какое-либо произведение. Автор своего творения имеет следующие права: исключительное право на произведение, право авторства, право автора на имя, право на неприкосновенность произведения, право на обнародование произведения.""")
                     print("""Пропаганда
↪Повторяющееся на регулярной основе, воздействие на людей, как отдельно взятых, так и объединённых в различные группы и общности, с целью формирования определённых взглядов и систем ценностей.
Проще говоря, распространение чего-либо с целью привлечь сторонников.""")
                     print("""Ложные сведения
↬Недостоверная или же лживая информация о чем-либо или о ком. Также, это может быть выдача себя за того кем человек не является.""")
                     print:("""Рейд 
↬Термины к "рейду" могут быть различными , в нашем случае - это "нападение" одного лица или группы лиц на сообщество с той или иной целью. Также рейдом будет считаться применение ботов.""")
                     print("""Общие чаты. 
↪Средство обмена сообщениями по социальной сети amino в режиме реального времени.
Некая "комната" для общения. В отличии от личных и приватных чатов, в общем чате могут общаться все участники сообщества, без какого-либо приглашения.
И конечно же, данные комнатки для общения должны следовать правилам.""")
                     print("""На что нужно административное разрешение.
Продажа. 
↪В amino возможны различные продажи, но, естественно, с амино-валютой.
В нашем сообществе продажная деятельность допустима только с разрешения лидера.
Продажи за другие валюты, кроме amino-коинов, запрещены.
Мероприятия
↪Организованное действие или совокупность действий, направленных на осуществление определенной цели. Имеется ввиду именно мероприятия посвященные развлечению. Подобные мероприятия как, конкурс, лотерея или квест время от времени проводятся в различных сообществах, не только администрацией, но и участниками. На проведение своего мероприятия нужно так же лидерское разрешение.
Организации
↪Объединение определённого количества людей, взаимодействующих и взаимовлияющих друг на друга для достижения или выполнения конкретных целей, выполняя разные обязанности.
На создание своей организации/группы, надо получить разрешение лидера.
Общение с администрацией.
↬Любое обращение к члену администрации должно быть уважительное и не должно нести в себе какого-либо рода агитационные действия на агрессив, негатив и т.п. Также исключены оскорбления, агрессия, троллинг и т.д.
В личном чате вы можете использовать свободную форму общения с членом администрации, но только если получили на это согласие самого члена администрации.""")
                  def "2"():
                     print("""Ссылка: http://aminoapps.com/c/OtelKhazbin
О мультсериале: Ад страдает от перенаселения и сам решает эту проблему, регулярно истребляя своих граждан. Принцесса Ада Чарли хочет найти альтернативное решение без массовой бойни. Она открывает отель, цель которого чтобы грешники исправились и попали в Рай. Преданный партнёр и лучшая подруга Чарли, Вегги, и их первый клиент, звезда фильмов для взрослых Энджел Даст, поддерживают её мнение. Но когда могучий грешник, Аластор, известный как «Радио-демон», предлагает принцессе Ада помощь, её сумасшедшая мечта получает шанс стать былью.""")
                  def "3"():
                     print('Ваш номер в отеле:', randint(1,666))
            
