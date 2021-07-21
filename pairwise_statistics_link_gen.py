from sys import argv

pairs = open(argv[1]).read().split('\n')

output = open('output/pairwise_statistics.md', 'w')
output.write('# Pairwise statistics\n')

filters = [
    '_doubledark',
    '_6suits',
    '_5suits',
    '_6suits_nondark',
    '_5suits_nondark',
    '_6suits_singledark',
    '_5suits_singledark',
    '_4suits',
    '_3suits',
    ''
]

for num_players in range(2,7):
    for f in filters:
        output.write('[')
        output.write("overall %dp%s"%(num_players,f))
        output.write(']')
        output.write('(https://github.com/Lel0uch-H/hanab-stats/blob/main/output/pairwise_statistics/overall_%dp%s.csv)<br/>\n'%
            (num_players,f))

for pair in pairs:
    player1,player2,*ignore = pair.split(',')
    for num_players in range(2,7):
        for f in filters:
            output.write('[')
            output.write("%s,%s %dp%s"%(player1,player2,num_players,f))
            output.write(']')
            output.write('(https://github.com/Lel0uch-H/hanab-stats/blob/main/output/pairwise_statistics/pairwise_statistics_%s_%s_%dp%s.csv)<br/>\n'%
                (player1,player2,num_players,f))

output.close()