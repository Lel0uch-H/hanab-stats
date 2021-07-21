from sys import argv

pairs = open(argv[1]).read().split('\n')

output = open('output/pairwise_statistics.md', 'w')
output.write('# Pairwise statistics\n')

filters = [
    'doubledark',
    '6suits',
    '5suits',
    '6suits_nondark',
    '5suits_nondark',
    '6suits_singledark',
    '5suits_singledark',
    '4suits',
    '3suits',
    ''
]

for pair in pairs:
    player1,player2,*ignore = pair.split(',')
    for num_players in range(2,7):
        for f in filters:
            output.write('[')
            output.write("%s,%s %s"%(player1,player2,f))
            output.write(']')
            output.write('(https://github.com/Lel0uch-H/hanab-stats/blob/main/output/pairwise_statistics/pairwise_statistics_%s_%s_%dp_%s.csv)\n'%
                (player1,player2,num_players,f))

output.close()