from sys import argv
from util import flatten,convertStr

l=open(argv[1]).read().split('\n')
l=l[:-2]
l=[i[:(i.find('#')-2)] for i in l]

def calcDeckCards(name, numsuits):
    count = numsuits*10
    dark_names = [
        'Black',
        'Gray',
        'Dark',
        'Cocoa',
        'Mix',
    ]
    for i in dark_names:
        count-=5*(name.count(i))
    if('Up or Down' in name):
        count-=numsuits
    return count

numstartcards = [0,0,5*2,5*3,4*4,4*5,3*6]
def calcPaceAndEfficiency(name,numplayers):
    numsuits = 6
    if 'No Variant' in name:
        numsuits = 5
    if 'Suits' in name:
        numsuits = ord(name[name.find('Suits')-2])-ord('0')
    numdeckcards = calcDeckCards(name,numsuits)
    pace = (numdeckcards-numstartcards[numplayers]+numplayers)-5*numsuits
    cs_factor = 1
    if('Clue Starved' in name):
        cs_factor = 2
    unusable_5s = (1 if (numplayers < 5) else 2)
    fives_clues = numsuits-unusable_5s
    if ('Throw' in name):
        fives_clues = 0
    efficiency = (5.0*numsuits)/(8+(pace+fives_clues)//cs_factor)
    # efficiency = "%.2f"%efficiency
    return (pace,efficiency)

def calcPaceAndEfficiencyAll(name):
    return [calcPaceAndEfficiency(name,num) for num in range(2,7)]

def calcDifficultyOverhead(name):
    score = 100
    if ('White' in name):
        score += 5
    if ('Rainbow' in name):
        score += 10
    if ('Prism' in name):
        score += 10
    if ('Gray' in name):
        score += 12
    if ('Deceptive-Ones' in name):
        score += 15
    if ('Deceptive-Fives' in name):
        score += 20
    if ('Pink' in name):
        score += 20
    if ('Muddy' in name):
        score += 20
    if ('Cocoa' in name):
        score += 20
    if ('Ambiguous' in name):
        score += 20
    if ('Alternating' in name):
        score += 20
    if ('Dual-Color' in name):
        score += 25
    if ('Omni' in name):
        score += 25
    if ('Up or Down' in name):
        score += 30
    if ('Brown' in name):
        score += 30
    if ('Null' in name):
        score += 35
    if ('Throw' in name):
        score += 40
    if ('Special Mix' in name):
        score += 75
    return score

l=[(i,calcPaceAndEfficiencyAll(i),calcDifficultyOverhead(i)) for i in l]

l=[flatten(i) for i in l]
l=[convertStr(i) for i in l]

l=[','.join(i) for i in l]

print('\n'.join(l))
