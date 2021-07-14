from sys import argv
import requests
from lxml import etree as et
from lxml import html
from lxml import etree
from functools import reduce
from util import flatten,convertStr,convertListOfListToCsv

game_id = argv[1]

x = requests.get('https://hanab.live/export/'+game_id)
print(x.text)
# data = x.text

# # data = open('player_data.html').read()

# root = html.fromstring(data)
# results = root.get_element_by_id('history-table')

# tbody = list(filter(lambda i: i.tag=='tbody', results))[0]

# # print(tbody)
# l = [tr for tr in tbody]
# l = [processRow(tr) for tr in tbody]

# output=open(argv[2],'w', encoding="utf-8")

# output.write(convertListOfListToCsv(l))

# output.close()