from sys import argv
import os

script = argv
name = str(script(0))

cmd = 'start payload.txt'
os.system(cmd)
os.mkdir('C:\clone')
os.system(r"copy payload.txt C:\clone")
os.system(rf"copy {name} C:\clone")


