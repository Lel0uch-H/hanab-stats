from sys import argv
from os import system

command = argv[1]
players = open(argv[2]).read().split('\n')
# print(players)
for player in players:
    system('python.exe .\%s.py %s .\output\%s.csv'%(command,player,player))