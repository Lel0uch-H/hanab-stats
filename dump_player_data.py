from sys import argv
import requests
from lxml import etree as et
from lxml import html
from lxml import etree
from functools import reduce
from util import flatten,convertStr,convertListOfListToCsv

player_name = argv[1]

def processRow(tr):
    l = [i.text_content() for i in tr]
    l = [l[0],l[1],l[2],l[3],l[5]]
    l[-1] = l[-1].strip()
    l[-1] = l[-1].split(',')
    l[-1] = [i.strip() for i in l[-1]]
    return flatten(l)

x = requests.get('https://hanab.live/history/'+player_name)
# print(x.text)
data = x.text

# data = open('player_data.html').read()

root = html.fromstring(data)
results = root.get_element_by_id('history-table')

tbody = list(filter(lambda i: i.tag=='tbody', results))[0]

# print(tbody)
l = [tr for tr in tbody]
l = [processRow(tr) for tr in tbody]

output=open(argv[2],'w', encoding="utf-8")

output.write(convertListOfListToCsv(l))

output.close()