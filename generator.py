# http://xgu.ru/wiki/Jinja2
import pickle
from jinja2 import Template


def render_main(inv):
    template = Template(open('trials.investigations.template.html', 'r', encoding='utf8').read())
    f = open('index.html', 'w', encoding='utf8')
    f.write(template.render(inv=inv))
    f.close()


def render_card(card):
    template = Template(open('trials.card.template.html', 'r', encoding='utf8').read())
    f = open(card['file'], 'w', encoding='utf8')
    f.write(template.render(card=card))
    f.close()

inv=pickle.load(open("2015.p", "rb"))
render_main(inv)
# render_card(inv[0])
for i in inv:
    render_card(i)


