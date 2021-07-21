from sys import argv
from os import system

pairs = open(argv[1]).read().split('\n')
k = argv[2]

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

for f in filters:
    output = open('output/pairwise_statistics/overall_%s.csv'%('_'.join(("%sp %s"%(k,f)).strip().split(' '))), 'w')
    output.write('player1,player2,attempts,won_variants,attempts/win\n')
    output.close()

for pair in pairs:
    player1,player2,*ignore = pair.split(',')
    for f in filters:
        system('python3 pairwise_statistics.py %s %s %sp %s'%(player1,player2,k,f))
