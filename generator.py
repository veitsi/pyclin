# http://xgu.ru/wiki/Jinja2
import re, pickle
from jinja2 import Template


def ser_to_file():
    card = {'id': 'N/A000',
            'title': 'title',
            'sponsor': 'sponsor'
            }
    pickle.dump(card, open("save.p", "wb"))


def ser_from_file():
    card = pickle.load(open("save.p", "rb"))
    print(card)


def findid(a='a, bc код дослідження PVD-202, від 16 грудня 2014'):
    pattern = re.compile(r'код дослідження \S+[,\s]')
    # result = re.match(r'', a)
    result = re.search(pattern, a)
    if result is not None:
        return result.group(0)[16:-2]


assert findid() == 'PVD-202'
a = '''Рандомізоване, подвійне-сліпе, плацебо-контрольоване, багатоцентрове  дослідження  фази  ІІІ  для  оцінки ефективності (підтримання ремісії) та безпеки препарату етролізумаб у порівнянні з плацебо у пацієнтів з активним виразковим колітом середнього або важкого ступеня, які раніше не застосовували інгібітори фактору некрозу пухлини, код дослідження GA29102, версія 4 від 22 серпня 2014 року'
'''


def render_card(file='card0.html', card={'id': 'N/A000',
                                         'title': 'title',
                                         'sponsor': 'sponsor'
                                         }):
    template = Template(open('card.template.html', 'r', encoding='utf8').read())
    f = open(file, 'w', encoding='utf8')
    f.write(template.render(card=card))
    f.close()


# render_card()

def create_object_from_txt():
    rez = []
    f = open('2015.txt', 'r', encoding='utf8')
    num = f.readline()
    while num:
        file = 'cards/card' + num[:-1] + ".html"
        title = f.readline()
        id = findid(title)
        if id is None or len(id) < 3:
            id = 'N/A-' + num[:-1] + 'AZCE'
        zayavnik = f.readline()
        sponsor = f.readline()
        druglist = f.readline()
        responder = f.readline()
        tocompare = f.readline()
        bonus = f.readline()
        card = {'num': num,
                'id': id,
                'file': file,
                'title': title,
                'zayavnik': zayavnik,
                'sponsor': sponsor,
                'druglist': druglist,
                'responder': responder,
                'tocompare': tocompare,
                'bonus': bonus
                }
        # render_card(file, card)
        rez.append(card)
        num = f.readline()
    f=open("2015.p", "wb")
    pickle.dump(rez, f)
    f.close()
    return rez

# create_object_from_txt()
inv = pickle.load(open("2015.p", "rb"))
# # for i in inv:
# #     print((i['id']))
#
# template = Template(open('main.template.html', 'r', encoding='utf8').read())
# f = open('index.html', 'w', encoding='utf8')
# f.write(template.render(inv=inv))
# f.close()
