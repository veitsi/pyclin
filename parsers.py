import re, pickle


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

def find_shorter_tile(a):
    i=a.find("код дослідження")
    return a[:i]

a = '''Рандомізоване, подвійне-сліпе, плацебо-контрольоване, багатоцентрове  дослідження  фази  ІІІ  для  оцінки ефективності (підтримання ремісії) та безпеки препарату етролізумаб у порівнянні з плацебо у пацієнтів з активним виразковим колітом середнього або важкого ступеня, які раніше не застосовували інгібітори фактору некрозу пухлини, код дослідження GA29102, версія 4 від 22 серпня 2014 року'
'''

assert findid() == 'PVD-202'



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
                'shorter_title':find_shorter_tile(title),
                'zayavnik': zayavnik,
                'sponsor': sponsor,
                'druglist': druglist,
                'responder': responder,
                'tocompare': tocompare,
                'bonus': bonus
                }
        rez.append(card)
        num = f.readline()
    f=open("2015.p", "wb")
    pickle.dump(rez, f)
    f.close()
    return rez

# inv=create_object_from_txt()
# print(inv[2])