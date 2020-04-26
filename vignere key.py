#!/usr/bin/env python
# coding: utf-8

# In[ ]:
banner = """\u001b[36m
 █████▄  ██▀███   ▄▄▄       ▄████  ▒█████    ███▄ ▄███    ▄███    ▓▓▄     █ 
▒██▀ ██▌▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▒██▒  ██▒▓██▒▀█▀█ █▒▒██   ██ ▄ ██ ▀█   █ 
░██   █▌▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒██░  ██▒▓██    ▓██░▒██   ▀█▄▓ ██  ▀█ ██▒
░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▒█░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░   ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░ ░  ░   ░░   ░   ░   ▒   ░ ░   ░ ░ ░ ░ ▒  ░      ░     ░   ▒      ░   ░ ░ 
   ░       ░           ░  ░      ░     ░ ░         ░         ░  ░         ░ 
 ░                                                                          
                            
                           \u001b[32m - coded with <3 For CTF's by Shivanshu Sharma\u001b[0m 
    """
print(banner)

a = input('Enter cipher text: ')
b = input('Enter key: ')
a = a.lower()
b = b.lower()
c = ''
j=0
for i in a:
    if not ord('a') <= ord(i) <= ord('z'):
        c += i
    else:
        first = ord(i) - ord('a')
        second = ord(b[j]) - ord('a')
        c += chr((first - second) % 26 + ord('a'))
        j += 1
    if j == len(b):
        j = 0
print ('The plain text: '+ c)

