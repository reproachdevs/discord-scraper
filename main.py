import requests,base64,glob,json
from os import system,walk
from time import sleep
from random import choice
from colorama import Fore
from shutil import copyfileobj


b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTYELLOW_EX
rw = Fore.LIGHTWHITE_EX

def clear():
    system('cls')

def title(text):
    system('title '+ text)

def getImagePath():
    file_path_type = ["ChangeToken/Images/*.jpg"]
    images = glob.glob(choice(file_path_type))
    random_image = choice(images)
    file_path = str(random_image).replace('\\','/')
    return file_path

def getImages(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
        return str(b64_string).replace('b\'','')
    
clear()
title(f'Discord Username ^& PFP ^& Bio Scraper  ^|  Made by reproach')
logo = ("""
   
    _ __ ___ _ __    ___  ___ _ __ __ _ _ __   ___ _ __ 
   | '__/ _ \ '_ \  / __|/ __| '__/ _` | '_ \ / _ \ '__|
   | | |  __/ |_) | \__ \ (__| | | (_| | |_) |  __/ |   
   |_|  \___| .__/  |___/\___|_|  \__,_| .__/ \___|_|   
            | |                        | |              
            |_|                        |_|              
                                          
""")

class Tools:
    def __init__(self, want_proxy: bool):
        if want_proxy: self.proxies = open('proxies.txt','r',encoding='utf-8').read().splitlines()
        self.usernames = open('Scrapes/usernames.txt','r',encoding='utf-8').read().splitlines()
        self.token = json.load(open('config.json','r',encoding='utf-8'))['account_token']
        self.xsup = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1MTYzOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
        
        self.scraped_counter = 0
        self.param = {
            "limit": 100
        }
        
        self.p = Fore.LIGHTMAGENTA_EX
        self.w = Fore.LIGHTWHITE_EX
        self.b = Fore.LIGHTBLUE_EX
        self.g = Fore.LIGHTGREEN_EX
        self.r = Fore.LIGHTRED_EX
        self.c = Fore.LIGHTCYAN_EX
        self.y = Fore.LIGHTYELLOW_EX
        
        title(f'Discord Username ^& PFP ^& Bio Scraper  ^| Total Scraped: {self.scraped_counter}  ^|  Made by reproach')
        if self.token == 'enter account token': 
            print(f'{self.b}[{self.p}Debug Mode{self.b}] {self.w}[{self.y}i{self.w}] Error -> Enter Account Token in config.json!')
            sleep(9999)
    def scrapeInfo(self,channelid: str, want_proxy: bool):
        file_number = len(next(walk('Scrapes/Images/'))[2])
        
        while True:
            try:
                headers = {
                    'accept': '*/*',
                    'authorization': self.token,
                    'cache-control': 'no-cache',
                    'pragma': 'no-cache',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-super-properties': self.xsup,
                }
                r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages',params=self.param,headers=headers)

                for info in r.json():

                    username = info['author']['username']
                    userid = info['author']['id']
                    userpfp = info['author']['avatar']
                    if username not in self.usernames:
                        try:
                            self.usernames.append(username)
                        except:
                            continue
                        r2 = requests.get(url=f'https://cdn.discordapp.com/avatars/{userid}/{userpfp}.jpg?size=512',stream=True)
                        if want_proxy:
                            proxy = choice(self.proxies)
                            proxies = {
                                "http": f'http://{proxy}'
                            }
                            
                            headers = {
                                "accept": "*/*",
                                "accept-encoding": "gzip, deflate, br",
                                'authorization': self.token,
                                "dnt": "1",
                                "sec-fetch-dest": "empty",
                                "sec-fetch-mode": "cors",
                                "sec-fetch-site": "same-origin",
                                "sec-gpc": "1",
                                "x-debug-options": "bugReporterEnabled",
                                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
                                "x-super-properties": self.xsup
                            }
                            
                            r3 = requests.get(url=f'https://discord.com/api/v9/users/{userid}/profile',headers=headers, proxies=proxies, timeout=10)
                            try:
                                userbio = r3.json()['user']['bio']
                            except KeyError:
                                print(f'{self.b}[{self.p}Debug Mode{self.b}] {self.w}[{self.y}i{self.w}] Error -> {self.r}No biography')
                                userbio = False
                            except requests.exceptions.JSONDecodeError as e:
                                print(r3.text)
                                print(f'{self.b}[{self.p}Debug Mode{self.b}] {self.w}[{self.y}i{self.w}] Error -> {self.r}Rate Limited!')
                                userbio = False
                                
                        if want_proxy:
                            print(f' {self.b}[{self.p}reproach{self.b}] {self.w}[{self.g}+{self.w}] Username, PFP and Bio of the account {self.c}{username}{self.w} are scraped.')
                        else:
                            print(f' {self.b}[{self.p}reproach{self.b}] {self.w}[{self.g}+{self.w}] Username and PFP of the account {self.c}{username}{self.w} are scraped.')

                        file_number += 1
                        self.scraped_counter += 1
                        title(f'Discord Username ^& PFP ^& Bio Scraper  ^|  Total Scraped: {self.scraped_counter}  ^|  Made by reproach')
                        if userpfp != None:
                            with open(f'Scrapes/Images/images-{file_number}.jpg','wb') as down_file:
                                copyfileobj(r2.raw, down_file)
                                
                        else:
                            file_number -= 1
                        with open('Scrapes/usernames.txt','a',encoding='utf-8') as file:
                            file.write(f"{username}\n")                       
                        if want_proxy and userbio != False:
                            if userbio != '[]' and not "\n" in userbio and not 'discord.gg/' in userbio and "" != userbio and not '.gg/' in userbio:
                                with open('Scrapes/bio.txt','a',encoding='utf-8') as file:
                                    file.write(f"{userbio}\n")
                self.param = {
                        'before': r.json()[-1]['id'],
                        'limit': 100
                    }
            except Exception as e:
                if 'Unauthorized'in r.text: 
                    print(f' {self.b}[{self.p}Debug Mode{self.b}] {self.w}[{self.y}i{self.w}] Error -> {self.r}Token Invalid! Change token in \'config.json\'')
                    sleep(10)
                    break
                else:
                    print(f' {self.b}[{self.p}Debug Mode{self.b}] {self.w}[{self.y}i{self.w}] Error -> {self.r}{str(e).capitalize()}')
                sleep(5)

print(logo)
while True:
    print(f"""
{b}[{w}1{b}]{rw} Username & PFP & Bio Scraper
{b}[{w}2{b}]{rw} Escape
    """)
    user_choice = int(input('> '))
    if user_choice == 1:
        print(f"\n{b}[{w}?{b}]{rw} Channel ID: ")
        channel_id = input('> ')
        print(f"\n{b}[{w}?{b}]{rw} Do you want to use a proxy? (y/n)")
        print(f"{b}[{w}*{b}]{rw} WARNING: If you don't want to use it, the program won't collect the bio!")
        want_proxy = input('> ')
        if want_proxy.lower() == 'y':
            want_proxy = True
        elif want_proxy.lower() == 'n':
            want_proxy = False
        clear()
        print(logo)
        tool = Tools(want_proxy)
        tool.scrapeInfo(channel_id, want_proxy)
    elif user_choice == 2:
        print("Exiting...")
        sleep(3)
        break
