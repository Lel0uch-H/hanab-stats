from sys import argv
from os import system

pairs = open(argv[1]).read().split('\n')

filters = [
    'doubledark',
    '6suits',
    '5suits',
    '6suits nondark',
    '5suits nondark',
    '6suits singledark',
    '5suits singledark',
    '4suits',
    '3suits',
    ''
]

for pair in pairs:
    player1,player2 = pair.split(',')
    for f in filters:
        system('python3 pairwise_statistics.py %s %s 2p %s'%(player1,player2,f))
