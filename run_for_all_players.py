from sys import argv
from os import system

command = argv[1]
players = open(argv[2]).read().split('\n')
output_dir = argv[3]

# print(players)
for player in players:
    system('python3 ./%s.py %s ./output/%s/%s.csv'%(command,player,output_dir,player))