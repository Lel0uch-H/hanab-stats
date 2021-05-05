from sys import argv

player1 = argv[1]
player2 = argv[2]

def buildScoreSet(player):
    l=open('output/variant_wise_first_win/variant_wise_first_win_%s.csv'%player).read().split('\n')
    l=[i.split(',') for i in l]
    return l

output=open('output/variant_diff_%s_%s.csv'%(player1,player2), 'w')

idx1,idx2=0,0
l1,l2 = buildScoreSet(player1), buildScoreSet(player2)

while idx1 < len(l1) and idx2 < len(l2):
    if (str(l1[idx1][0:2]) == str(l2[idx2][0:2])):
        idx1 += 1
        idx2 += 1
    elif (str(l1[idx1][0:2]) < str(l2[idx2][0:2])):
        output.write(','.join(l1[idx1]))
        output.write('\n')
        idx1 += 1
    else:
        idx2 += 1

output.close()