import collections.abc
import operator

def stringify(l):
    return [str(i) for i in l]

def flatten(tup):
    vals = []
    for i in range(len(tup)):
        # print(i)
        if isinstance(tup[i], collections.abc.Sequence) and not isinstance(tup[i], str):
            vals.extend(flatten(tup[i]))
        else:
            vals.append(tup[i])
    return vals

def convertStr(tup):
    return [str(i) for i in tup]

def convertListOfListToCsv(l):
    return '\n'.join([','.join(stringify(k)) for k in l])

def calcNumSuits(name):
    numsuits = 6
    if 'No Variant' in name:
        numsuits = 5
    if 'Suits' in name:
        numsuits = ord(name[name.find('Suits')-2])-ord('0')
    return numsuits

def convertDictToList(dict):
    dictlist = []
    for key, value in dict.items():
        temp = [key,value]
        dictlist.append(temp)
    return dictlist

def sortBySecond(tups):
    return sorted(tups, key=operator.itemgetter(1), reverse=True)

def sortByThird(tups):
    return sorted(tups, key=operator.itemgetter(2), reverse=True)

def sortByKth(tups, k):
    return sorted(tups, key=operator.itemgetter(k), reverse=True)

dark_names = [
    'Black',
    'Gray',
    'Dark',
    'Cocoa',
    'Mix',
]

def isNonDark(variant):
    count = 0
    for i in dark_names:
        count+=variant.count(i)
    return (count == 0)

def isSingleDark(variant):
    count = 0
    for i in dark_names:
        count+=variant.count(i)
    return (count == 1)

def isDoubleDark(variant):
    count = 0
    for i in dark_names:
        count+=variant.count(i)
    return (count == 2)
