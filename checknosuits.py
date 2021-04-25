from sys import argv

l=open(argv[1]).read().split('\n')
l=l[:-2]
l=[i[:(i.find('#')-1)] for i in l]

for i in l:
    if 'Suits' not in i:
        print(i)