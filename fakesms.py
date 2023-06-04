import os
import time
import platform
import base64
import requests
import termcolor
from colorama import Fore, Style
from pyqtcolor import *

colorama.deinit()
banner = Center.XCenter("""
                _______ _    _  _______     ____  __  __ ______
               / /  ___/ \  | |/ / ____|   / ___||  \/  / ___\ \`
              | || |_ / _ \ | ' /|  _| ____\___ \| |\/| \___ \| |
             < < |  _/ ___ \| . \| |__|_____|__) | |  | |___) |> >
              | ||_|/_/   \_\_|\_\_____|   |____/|_|  |_|____/| |
               \_\                                           /_/
                            \n\n
""")

def check_net1():
    print(termcolor.colored("[*] Checking Internet Connection:", 'cyan'))
    url = "https://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print(Fore.GREEN + "[*] Connected to the Internet")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
        menu()
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(Fore.RED + '[*] No Internet Connection....')


def menu():
    ans = True
    while ans:
        print(termcolor.colored("""
      1. Usage
      2. Send SMS
      3. Exit/Quit
      """, 'yellow'))
        ans = input(termcolor.colored("Choose From Given Options: ", 'cyan'))
        if ans == "1":
            print("\033c")
            usage1()
        elif ans == "2":
            print("\033c")
            main_check1()
        elif ans == "3":
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            print(Fore.GREEN + "\n[+] Thanks For Using Fake-SMS! See You Tomorrow")
            ans = None
        else:
            print(Fore.RED + "\n[+] Not Valid Choice Try again")


def usage1():
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    print(termcolor.colored('''
      1. Your Country Code Must Be without +
      2. Country Code Example: 91
      3. Your Phone Number Must be Start Without 0
      4. Full Usage: 913443210111

      ..........NOTE: Only One Text Message Is Allowed Per Day...........

      ''', 'magenta'))


def main_check1():
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    x = input(termcolor.colored("\n[*] Enter Your Number: ", 'green'))
    y = input(termcolor.colored("\n[*] Enter Your Message: ", 'blue'))
    message = base64.b64decode('aHR0cHM6Ly90ZXh0YmVsdC5jb20vdGV4dA=='.encode('ascii')).decode('ascii')
    resp =
