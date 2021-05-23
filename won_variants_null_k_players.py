from sys import argv
from util import sortBySecond, convertListOfListToCsv

players = open(argv[1]).read().split('\n')
k = argv[2]


output_data = []

for player in players:
    won_vars=open('output/variant_wise_first_win/variant_wise_first_win_%s.csv'%player, encoding='utf-8').read().split('\n')
    won_vars = [i.split(',') for i in won_vars if i!='' and 'Null' in i.split(',')[0]  and i.split(',')[1] == k]
    output_data.append((player,len(won_vars)))

output_data = sortBySecond(output_data)

output = open('output/won_variants_null_%s_players.csv'%k,'w')
output.write(convertListOfListToCsv(output_data))
output.close()