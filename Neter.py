#!/usr/bin/env python
# -*- coding: utf-8 -*-


from colorama import Fore, Style

import sp
import sys
import time

print("""\33[0m


███╗   ██╗███████╗████████╗███████╗██████╗ 
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗     ██║   █████╗  ██████╔╝
██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██╔══██╗
██║ ╚████║███████╗   ██║   ███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  \033[92mv1.0 \33[0m| \033[91m@stormex


""")


def progressBar():
    print("\33[0mLoading:")

    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")


def printer(title, data):
    print(
        Fore.CYAN + "[" + Style.BRIGHT + Fore.GREEN + "*" + Style.RESET_ALL + Fore.CYAN + "] \033[36m" + title + ": " + Fore.RED + "\033[5m < " + str(
            data) + " >\033[0m")


def net_test():
    servers = []
    speed = sp.Speedtest()
    speed.get_servers(servers)
    speed.get_best_server()
    speed.download(threads=None)
    speed.upload(threads=None)
    progressBar()
    x = speed.results.dict()

    d = round(x.get("download") / 1000000, 2)
    u = round(x.get("upload") / 1000000, 2)
    p = round(x.get("ping"))
    c = (x.get("client"))

    # Ping
    def ping():
        if p >= 250:
            return Style.BRIGHT + Fore.RED + str(p) + Style.RESET_ALL
        elif 60 <= p < 250:
            return Style.BRIGHT + Fore.YELLOW + str(p) + Style.RESET_ALL
        elif p < 60:
            return Style.BRIGHT + Fore.GREEN + str(p) + Style.RESET_ALL

    # Speed of download
    def download():
        if d < 3:
            return Style.BRIGHT + Fore.RED + str(d) + Style.RESET_ALL
        elif 3 <= d <= 5.5:
            return Style.BRIGHT + Fore.YELLOW + str(d) + Style.RESET_ALL
        elif d > 5.5:
            return Style.BRIGHT + Fore.GREEN + str(d) + Style.RESET_ALL

    # Speed of upload
    def upload():
        if u < 0.8:
            return Style.BRIGHT + Fore.RED + str(u) + Style.RESET_ALL
        elif 0.8 <= u <= 1.5:
            return Style.BRIGHT + Fore.YELLOW + str(u) + Style.RESET_ALL
        elif u > 1.5:
            return Style.BRIGHT + Fore.GREEN + str(u) + Style.RESET_ALL

    print(Fore.CYAN + "[" + Style.BRIGHT + Fore.RED + "-" + Style.RESET_ALL + Fore.CYAN + "] \033[36mNetwork Test")
    print(Fore.GREEN + "    └──" + Style.RESET_ALL, "\033[0m Ping:", ping(), "ms | Download:", download(),
          "Mbit/s | Upload:", upload(),
          "Mbit/s")

    printer("IP", c.get("ip"))
    printer("Provider", c.get("isp"))
    printer("Country", c.get("country"))


net_test()
