#!/usr/bin/env python
# coding: utf-8

# By -- Bl4cKc34sEr
# Might be the smallest code u would have seen 😂....
banner = """\u001b[36m
 █████▄  ██▀███   ▄▄▄       ▄████  ▒█████    ███▄ ▄███    ▄███    ▓▓▄     █ 
▒██▀  █▌▓██   ██ ▒████▄     ██▒  ▒ ▒██▒  ██▒▓██▒▀█▀█ █▒▒██   ██ ▄ ██ ▀█   █ 
░██ ▒ █▌▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒██░  ██▒▓██    ▓██░▒██   ▀█▄▓ ██  ▀█ ██▒
░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒ ▒▓███▀▒░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▒█░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░   ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒ 
 ░ ░  ░   ░░   ░   ░   ▒   ░ ░   ░ ░ ░ ░ ▒  ░      ░     ░   ▒      ░     ░ 
   ░       ░           ░  ░      ░     ░ ░         ░         ░  ░         ░ 
 ░                                                                          
                            
                           \u001b[32m - coded with <3 For CTF's by Shivanshu Sharma\u001b[0m 
    """
print(banner)
a=input()
bytearray.fromhex(a).decode()

# OR you can try this too....

##  bytearray.fromhex(input()).decode()



