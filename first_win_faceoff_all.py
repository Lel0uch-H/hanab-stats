from sys import argv
from os import system

command = 'first_win_faceoff'
players = open(argv[1]).read().split('\n')
for player1 in players:
    for player2 in players:
        if player1 < player2:
            system('python.exe .\%s.py %s %s'%(command,player1,player2))