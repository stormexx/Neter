#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sp
from net_check import is_connected
from colors import *
from banner import banner
from bar import bar


def printer(title, data):
    print(
        cyan("[") + light_green("*") + reset() + cyan("]") + " \033[36m" + title + ": " + light_red("\033[5m < " + str(
            data) + " >\033[0m"))


def net_test():
    os.system("clear")
    banner()
    try:
        while True:

            print("                         [1] Start\n                        [99] Exit\n")
            cmd = input(
                light_red("neter@stormex")
                + light_green(" »")
                + reset()
            )
            os.system("clear")
            banner()

            if cmd != "":
                if cmd == "1":
                    os.system("clear")
                    banner()
                    if is_connected():
                        print(light_green("[✔] INTERNET CONNECTION"))
                        print(cyan("[+] Starting..."))
                        servers = []
                        speed = sp.Speedtest()
                        speed.get_servers(servers)
                        speed.get_best_server()
                        speed.download(threads=None)
                        speed.upload(threads=None)
                        bar()
                        os.system("clear")
                        banner()
                        x = speed.results.dict()

                        d = round(x.get("download") / 1000000, 2)
                        u = round(x.get("upload") / 1000000, 2)
                        p = round(x.get("ping"))
                        c = (x.get("client"))

                        # Ping
                        def ping():
                            if p >= 250:
                                return light_red(str(p)) + reset()
                            elif 60 <= p < 250:
                                return light_yellow(str(p)) + reset()
                            elif p < 60:
                                return light_green(str(p)) + reset()

                        # Speed of download
                        def download():
                            if d < 3:
                                return light_red(str(d)) + reset()
                            elif 3 <= d <= 5.5:
                                return light_yellow(str(d)) + reset()
                            elif d > 5.5:
                                return light_green(str(d)) + reset()

                        # Speed of upload
                        def upload():
                            if u < 0.8:
                                return light_red(str(u)) + reset()
                            elif 0.8 <= u <= 1.5:
                                return light_yellow(str(u)) + reset()
                            elif u > 1.5:
                                return light_green(str(u)) + reset()

                        print("")
                        print(
                            cyan("[") + light_red("-") + reset() + cyan("]\033[36mNetwork Test"))
                        print(light_green("    └──") + reset(), "\033[0m Ping:", ping(), "ms | Download:", download(),
                              "Mbit/s | Upload:", upload(),
                              "Mbit/s")

                        printer("IP", c.get("ip"))
                        printer("Provider", c.get("isp"))
                        printer("Country", c.get("country"))

                    else:
                        print(light_red("[✘] CHECK YOUR INTERNET CONNECTION!"))
                    print("\n")
                    cmd = input(light_red(">>> Do you want to restart again (Y/n) ? ")
                                + reset())
                    while not (cmd == "Y" or cmd == "n"):
                        os.system("clear")
                        banner()
                        cmd = input(light_red(">>> Do you want to restart again (Y/n) ? ")
                                    + reset())
                    if cmd == "Y":
                        os.system('clear')
                        net_test()
                    elif cmd == "n":
                        os.system("clear")
                        banner()
                        exit()
                if cmd == "99":
                    os.system("clear")
                    banner()
                    exit()



    except():
        print("")


net_test()
